import 'package:acws_app/app_style.dart';
import 'package:acws_app/page/home/widget_card_detail_button.dart';
import 'package:flutter/material.dart';

class Reserve extends StatefulWidget {
  @override
  _ReserveState createState() => _ReserveState();
}

class _ReserveState extends State<Reserve> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('จอง Meeting Room'),
        ),
        body: ListView(padding: const EdgeInsets.all(8.0), children: [
          Column(
            children: [
              Text('วันและเวลาที่จอง', style: AppTextStyle.HeaderText),
              SizedBox(height: 8),
              Card(
                child: ListTile(
                  leading: Icon(Icons.date_range),
                  title: Text('วันเสาร์ 31/12/2022'),
                  onTap: () {},
                ),
              ),
              SizedBox(height: 8),
              Row(
                children: [
                  Expanded(
                    child: Card(
                      child: ListTile(
                        leading: Icon(Icons.schedule),
                        title: Text('13:00'),
                        onTap: () {},
                      ),
                    ),
                  ),
                  SizedBox(width: 48, child: Center(child: Text('ถึง'))),
                  Expanded(
                    child: Card(
                      child: ListTile(
                        leading: Icon(Icons.schedule),
                        title: Text('16:00'),
                        onTap: () {},
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(height: 8),
              Text('เลือกประเภทห้องประชุม', style: AppTextStyle.HeaderText),
              SizedBox(height: 8),
              CardDetailButton(
                  '4 Person Meeting Room',
                  'รายละเอียด Lorem ipsum dolor sit amet, consectetur adipiscing elit.\nห้องสำหรับ 4 คน',
                  '99 ฿ / 1 ชม.',
                  onPressed: () => {})
            ],
          )
        ]));
  }
}
