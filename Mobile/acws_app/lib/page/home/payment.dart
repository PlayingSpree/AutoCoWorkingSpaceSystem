import 'dart:io';
import '../../app_config.dart' as appConfig;
import 'package:flutter/material.dart';
import 'package:webview_flutter/webview_flutter.dart';

import '../../app_style.dart';
import '../../app_transition_route.dart';
import '../../app_util.dart';

enum PaymentFor { member, meetingRoom }

class PaymentPage extends StatelessWidget {
  const PaymentPage(
      {Key key,
      @required this.title,
      @required this.detail,
      @required this.detailList,
      @required this.price,
      @required this.paymentFor,
      @required this.data})
      : super(key: key);

  final String title;
  final String detail;
  final Map<String, String> detailList;
  final int price;
  final PaymentFor paymentFor;
  final Map<String, Object> data;

  List<Widget> _detailListBuilder() {
    List<Widget> list = [];
    detailList.forEach((k, v) {
      list.add(Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Text(k, style: TextStyle(fontSize: 16)),
          Text(v, style: TextStyle(fontSize: 16))
        ],
      ));
    });
    return list;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('จ่ายเงิน'),
        ),
        body: Column(
          children: [
            Card(
                margin: EdgeInsets.all(12),
                color: Theme.of(context).primaryColorLight,
                child: Column(children: [
                  Padding(
                    padding: const EdgeInsets.only(top: 16),
                    child: Text(title, style: AppTextStyle.HeaderText),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 8, 16, 4),
                    child: Text(detail, textAlign: TextAlign.center),
                  ),
                  Padding(
                    padding: const EdgeInsets.all(16),
                    child: Column(children: _detailListBuilder()),
                  ),
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text('ราคา', style: AppTextStyle.HeaderText),
                        Text('${price.toStringAsFixed(2)} ฿',
                            style: AppTextStyle.HeaderText)
                      ],
                    ),
                  )
                ])),
            Card(
                margin: EdgeInsets.all(12),
                color: Colors.white70,
                child: Column(children: [
                  Padding(
                    padding: const EdgeInsets.symmetric(vertical: 12),
                    child: Text('ตัวเลือกการชำระเงิน',
                        style: AppTextStyle.HeaderText),
                  ),
                  Column(
                    children: [
                      Padding(
                        padding: const EdgeInsets.fromLTRB(12, 0, 12, 12),
                        child: Card(
                          child: ListTile(
                            leading: Icon(Icons.credit_card),
                            title: Text('บัตรเครดิต / เดบิต'),
                            onTap: () {
                              Navigator.of(context).push(SlideLeftRoute(
                                  exitPage: this,
                                  enterPage: PaymentWebView(
                                    data: data,
                                    paymentFor: paymentFor,
                                    price: price,
                                  )));
                            },
                          ),
                        ),
                      ),
                    ],
                  ),
                ]))
          ],
        ));
  }
}

class PaymentWebView extends StatefulWidget {
  const PaymentWebView(
      {Key key,
      @required this.price,
      @required this.paymentFor,
      @required this.data})
      : super(key: key);

  @override
  PaymentWebViewState createState() => PaymentWebViewState();

  final int price;
  final PaymentFor paymentFor;
  final Map<String, Object> data;
}

class PaymentWebViewState extends State<PaymentWebView> {
  @override
  void initState() {
    super.initState();
    // Enable hybrid composition.
    if (Platform.isAndroid) WebView.platform = SurfaceAndroidWebView();
  }

  Future<void> _makePayment(String card) async {
    var body = widget.data;
    body["card_token"] = card;
    String url;
    switch (widget.paymentFor) {
      case PaymentFor.member:
        url = '/coworkingspace/subscription/';
        break;
      case PaymentFor.meetingRoom:
        url = '/meetingroom/booking/';
        break;
    }
    try {
      var response = await httpRequest(url, body, context);
      await _showDialog('การชำระเงินสำเร็จ');
      Navigator.popUntil(context, ModalRoute.withName('/main'));
    } catch (e) {
      await _showDialog('การชำระเงินล้มเหลว',e.toString());
      Navigator.pop(context);
    }
  }

  Future<void> _showDialog(String title, [String text]) async {
    return showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text(title),
          content: text == null ? null : Text(text),
          actions: <Widget>[
            TextButton(
              child: Text('OK'),
              onPressed: () {
                Navigator.pop(context);
              },
            ),
          ],
        );
      },
    );
  }

  JavascriptChannel _callbackJavascriptChannel(BuildContext context) {
    return JavascriptChannel(
        name: 'FlutterCallback',
        onMessageReceived: (JavascriptMessage message) {
          _makePayment(message.message);
        });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('ชำระเงิน บัตรเครดิต / เดบิต'),
        ),
        body: WebView(
          initialUrl: appConfig.serverUrl +
              '/payment/form/?amount=${widget.price * 100}',
          javascriptMode: JavascriptMode.unrestricted,
          javascriptChannels:
              <JavascriptChannel>[_callbackJavascriptChannel(context)].toSet(),
        ));
  }
}
