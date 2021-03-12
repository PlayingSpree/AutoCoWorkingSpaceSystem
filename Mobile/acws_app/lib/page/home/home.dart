import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import '../../app_style.dart';
import '../../app_transition_route.dart';
import '../../app_util.dart';
import '../history/history.dart';
import 'reserve.dart';
import 'subscribe.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  var _memberResponse;
  var _roomResponse;

  Future<void> _downloadData() async {
    var memberResponse =
        await httpGetRequest('/coworkingspace/subscription/me/', context);
    var roomResponse =
        await httpGetRequest('/meetingroom/booking/?future', context);
    setState(() {
      _memberResponse = memberResponse;
      _roomResponse = roomResponse;
    });
  }

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
                if (_memberResponse == null)
                  Text('')
                else if (_memberResponse['member_duration'] < 0)
                  Text('ยังไม่ได้เป็นสมาชิก')
                else if (_memberResponse['member_duration'] == 0)
                  Text('สมาชิกหมดอายุ')
                else
                  Text(
                      'สมาชิกสิ้นสุด: ${DateFormat.yMd().format(DateTime.parse(_memberResponse['member_date_end']))} (${_memberResponse['member_duration']} วัน)'),
                SizedBox(height: 8),
                if (_memberResponse != null)
                  _memberResponse['member_duration'] > 0
                      ? Card(
                          child: ListTile(
                            leading: Icon(Icons.lock_open),
                            title: Text('ปลดล็อคประตู'),
                            onTap: () {
                              Navigator.of(context).push(SlideLeftRoute(
                                  exitPage: this.widget,
                                  enterPage:
                                      Subscribe())); // TODO Unlock QR Code
                            },
                          ),
                        )
                      : SizedBox.shrink(),
                Card(
                  child: ListTile(
                    leading: Icon(Icons.person),
                    title: _memberResponse == null ||
                            _memberResponse['member_duration'] < 0
                        ? Text('สมัครสมาชิก Co-working Space')
                        : Text('ต่ออายุสมาชิก'),
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
                if (_roomResponse != null && _roomResponse.length > 0)
                  SizedBox(height: 8),
                Column(
                  children: [
                    for (var item in _roomResponse ?? [])
                      MeetingRoomHistoryListItem(item: item)
                  ],
                )
              ],
            ),
          ),
        )
      ],
    );
  }
}
