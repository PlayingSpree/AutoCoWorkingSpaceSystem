import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import '../../app_util.dart';

class HistoryPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 2,
      child: Scaffold(
        appBar: AppBar(
          flexibleSpace: Column(
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              TabBar(
                tabs: [
                  Tab(text: 'Meeting Room'),
                  Tab(text: 'Co-working Space'),
                ],
              ),
            ],
          ),
        ),
        body: TabBarView(
          children: [
            MeetingRoomHistory(),
            CoworkingSpaceHistory(),
          ],
        ),
      ),
    );
  }
}

class MeetingRoomHistory extends StatefulWidget {
  @override
  _MeetingRoomHistoryState createState() => _MeetingRoomHistoryState();
}

class _MeetingRoomHistoryState extends State<MeetingRoomHistory> {
  var _response;

  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/meetingroom/booking/', context);
    setState(() {
      _response = response;
    });
  }

  @override
  Widget build(BuildContext context) {
    return _response == null
        ? SizedBox.shrink()
        : ListView.builder(
            itemCount: _response.length,
            itemBuilder: (context, index) {
              var item = _response[index];
              return MeetingRoomHistoryListItem(item: item);
            },
          );
  }
}

class MeetingRoomHistoryListItem extends StatelessWidget {
  const MeetingRoomHistoryListItem({
    Key key,
    @required this.item,
  }) : super(key: key);

  final item;

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ListTile(
            visualDensity: VisualDensity(horizontal: 0, vertical: -4),
            title: Text(item['room']['name']),
            subtitle: Row(
              children: [
                Icon(
                  Icons.date_range,
                  color: Colors.grey,
                  size: 16,
                ),
                Text(
                    ' ${DateFormat.yMd().format(DateTime.parse(item['date_start']))}'),
                Icon(
                  Icons.access_time,
                  color: Colors.grey,
                  size: 16,
                ),
                Text(
                    ' ${DateFormat.Hm().format(DateTime.parse(item['date_start']).toLocal())} - ${DateFormat.Hm().format(DateTime.parse(item['date_end']).toLocal())}')
              ],
            ),
            trailing: Text('${item['amount']} ฿')),
        Divider()
      ],
    );
  }
}

class CoworkingSpaceHistory extends StatefulWidget {
  @override
  _CoworkingSpaceHistoryState createState() => _CoworkingSpaceHistoryState();
}

class _CoworkingSpaceHistoryState extends State<CoworkingSpaceHistory> {
  var _response;

  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  Future<void> _downloadData() async {
    var response =
        await httpGetRequest('/coworkingspace/subscription/', context);
    setState(() {
      _response = response;
    });
  }

  @override
  Widget build(BuildContext context) {
    return _response == null
        ? SizedBox.shrink()
        : ListView.builder(
            itemCount: _response.length,
            itemBuilder: (context, index) {
              var item = _response[index];
              return Column(
                children: [
                  ListTile(
                      visualDensity: VisualDensity(horizontal: 0, vertical: -4),
                      title: Text(item['package']['name']),
                      subtitle: Row(
                        children: [
                          Icon(
                            Icons.date_range,
                            color: Colors.grey,
                            size: 16,
                          ),
                          Text(
                              ' ${DateFormat.yMd().format(DateTime.parse(item['date_start']))} - ${DateFormat.yMd().format(DateTime.parse(item['date_end']))}')
                        ],
                      ),
                      trailing: Text('${item['package']['price']} ฿')),
                  Divider()
                ],
              );
            },
          );
  }
}
