import 'package:flutter/material.dart';
import 'package:qr_flutter/qr_flutter.dart';

class QRCode extends StatelessWidget {
  const QRCode(
      {Key key, @required this.title, @required this.qrCodeData, this.detail})
      : super(key: key);

  final String title;
  final String detail;
  final String qrCodeData;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(title),
      ),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          QrImage(
            data: qrCodeData,
          ),
          this.detail != null ? Text(detail) : SizedBox.shrink()
        ],
      ),
    );
  }
}
