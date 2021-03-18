import 'package:flutter/material.dart';

import '../../app_style.dart';
import '../../app_transition_route.dart';
import '../../app_util.dart';
import 'payment.dart';
import 'card_detail_button.dart';

class Subscribe extends StatefulWidget {
  @override
  _SubscribeState createState() => _SubscribeState();
}

class _SubscribeState extends State<Subscribe> {
  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  var _response;

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/coworkingspace/package/', context);
    setState(() {
      _response = response;
    });
  }

  void _goToPayment(var package) {
    Navigator.of(context).push(SlideLeftRoute(
        exitPage: this.widget,
        enterPage: PaymentPage(
            title: package['name'],
            detail: package['detail'],
            detailList: {'ระยะเวลา': '${package['duration']} วัน'},
            price: package['price'],
            paymentFor: PaymentFor.member,
            data: {'package': package['id']})));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('สมัครสมาชิก Co-working Space'),
        ),
        body: ListView(padding: const EdgeInsets.all(8), children: [
          Column(
            children: [
              Text('เลือกระยะเวลาสมาชิก', style: AppTextStyle.HeaderText),
              SizedBox(height: 8)
            ],
          ),
          AnimatedCrossFade(
              duration: const Duration(milliseconds: 200),
              crossFadeState: _response == null
                  ? CrossFadeState.showFirst
                  : CrossFadeState.showSecond,
              firstChild: SizedBox(
                height: 48,
                child: Center(
                  child: CircularProgressIndicator(
                      valueColor: new AlwaysStoppedAnimation<Color>(
                          Theme.of(context).primaryColor)),
                ),
              ),
              secondChild: Column(children: [
                for (var package in _response ?? [])
                  CardDetailButton(package['name'], package['detail'],
                      '${package['price']} ฿ / ${package['duration']} วัน',
                      onPressed: () {
                    _goToPayment(package);
                  })
              ]))
        ]));
  }
}
