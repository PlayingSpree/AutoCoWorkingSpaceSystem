import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

class MemberPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Text(
            'Member',
            style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
          ),
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
