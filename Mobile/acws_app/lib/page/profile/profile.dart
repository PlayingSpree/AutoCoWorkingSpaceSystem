import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../app_style.dart';

class ProfilePage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Padding(
            padding: const EdgeInsets.only(left: 12),
            child: Text(
              'ข้อมูลผู้ใช้',
              style: AppTextStyle.HeaderText,
            ),
          ),
          NameCardWidget(),
          TextButton(
              onPressed: () async {
                final prefs = await SharedPreferences.getInstance();
                prefs.remove('authToken');
                Navigator.pushReplacementNamed(context, '/login');
              },
              child: Text(
                'Logout',
                style: TextStyle(color: Colors.red),
              )),
        ],
      ),
    );
  }
}

class NameCardWidget extends StatefulWidget {
  @override
  _NameCardWidgetState createState() => _NameCardWidgetState();
}

class _NameCardWidgetState extends State<NameCardWidget> {
  @override
  Widget build(BuildContext context) {
    return ListTile(
        title: Text('Firstname Lastname'),
        isThreeLine: true,
        subtitle: Text('email@email.com\n098-765-4321'));
  }
}
