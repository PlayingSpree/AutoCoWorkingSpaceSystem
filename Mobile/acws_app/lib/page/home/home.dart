import 'package:acws_app/app_style.dart';
import 'package:acws_app/app_transition_route.dart';
import 'package:acws_app/page/home/reserve.dart';
import 'package:acws_app/page/home/subscribe.dart';
import 'package:flutter/material.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(8.0),
      children: [
        Card(
          margin: const EdgeInsets.all(4.0),
          color: Colors.white70,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: [
                Text('Co-working Space Member', style: AppTextStyle.HeaderText),
                SizedBox(height: 8),
                Text('ยังไม่ได้เป็นสมาชิก'),
                SizedBox(height: 8),
                Card(
                  child: ListTile(
                    leading: Icon(Icons.person),
                    title: Text('สมัครสมาชิก Co-working Space'),
                    onTap: () {
                      Navigator.of(context).push(SlideLeftRoute(
                          exitPage: this.widget, enterPage: Subscribe()));
                    },
                  ),
                ),
              ],
            ),
          ),
        ),
        Card(
          margin: const EdgeInsets.all(4.0),
          color: Colors.white70,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: [
                Text('Meeting Room',
                    style:
                        TextStyle(fontSize: 20, fontWeight: FontWeight.w500)),
                SizedBox(height: 8),
                Card(
                  child: ListTile(
                    leading: Icon(Icons.schedule),
                    trailing: Icon(Icons.arrow_forward),
                    title: Text('จองห้องประชุม'),
                    onTap: () {
                      Navigator.of(context).push(SlideLeftRoute(
                          exitPage: this.widget, enterPage: Reserve()));
                    },
                  ),
                ),
              ],
            ),
          ),
        )
      ],
    );
  }
}
