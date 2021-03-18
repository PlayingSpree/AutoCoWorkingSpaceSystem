import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../app_style.dart';
import '../../app_transition_route.dart';
import '../../app_util.dart';
import 'edit_detail.dart';

class ProfilePage extends StatefulWidget {
  @override
  _ProfilePageState createState() => _ProfilePageState();
}

class _ProfilePageState extends State<ProfilePage> {
  var _response;

  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/auth/user/', context);
    setState(() {
      _response = response;
    });
  }

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
          _response == null
              ? ListTile(leading: Icon(Icons.person, size: 48))
              : ListTile(
              title: Text(
                  '${_response['first_name']} ${_response['last_name']}'),
              leading: Icon(Icons.person, size: 48),
              isThreeLine: true,
              subtitle:
              Text('${_response['email']}\n${_response['phone']}')),
          Padding(
            padding: const EdgeInsets.fromLTRB(12, 0, 0, 6),
            child: Text(
              'การตั้งค่า',
              style: AppTextStyle.HeaderText,
            ),
          ),
          ListTile(
            title: Text('แก้ไขข้อมูลผู้ใช้'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator
                  .of(context)
                  .push(SlideLeftRoute(
                  exitPage: this.widget,
                  enterPage: EditDetail(
                      name:
                      '${_response['first_name']} ${_response['last_name']}',
                      phone: _response['phone'],
                      callback: _downloadData)));
              },
          ),
          Divider(),
          ListTile(
            title: Text('เปลี่ยนรหัสผ่าน'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator.of(context).push(SlideLeftRoute(
                  exitPage: this.widget, enterPage: EditDetail()));
            },
          ),
          Divider(),
          ListTile(
            title: Text('รายงานปัญหา'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator.of(context).push(SlideLeftRoute(
                  exitPage: this.widget,
                  enterPage: EditDetail(
                      name:
                      '${_response['first_name']} ${_response['last_name']}',
                      phone: _response['phone'])));
            },
          ),
          Divider(),
          ListTile(
            title: Text(
              'ลงชื่อออก',
              style: TextStyle(color: Theme
                  .of(context)
                  .errorColor),
            ),
            onTap: () async {
              final prefs = await SharedPreferences.getInstance();
              prefs.remove('authToken');
              Navigator.pushReplacementNamed(context, '/login');
            },
          ),
          Divider()
        ],
      ),
    );
  }
}
