import 'package:acws_app/app_style.dart';
import 'package:acws_app/page/home/widget_card_detail_button.dart';
import 'package:flutter/material.dart';

class Subscribe extends StatefulWidget {
  @override
  _ReserveState createState() => _ReserveState();
}

class _ReserveState extends State<Subscribe> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('สมัครสมาชิก Co-working Space'),
        ),
        body: ListView(padding: const EdgeInsets.all(8.0), children: [
          Column(
            children: [
              Text('เลือกระยะเวลาสมาชิก', style: AppTextStyle.HeaderText),
              SizedBox(height: 8),
              CardDetailButton(
                  '1 Week Co-working Space Member',
                  'รายละเอียด Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nเข้าใช้ Co-working Space ได้ 7 วัน',
                  '399 ฿ / 7 วัน',
                  onPressed: () => {})
            ],
          )
        ]));
  }
}
