import 'dart:convert';

import 'package:flutter/material.dart';

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
            Text('Meeting Room'),
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

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/coworkingspace/member/', context);
    setState(() {
      _response = response;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      // Let the ListView know how many items it needs to build.
      itemCount: _response.length,
      // Provide a builder function. This is where the magic happens.
      // Convert each item into a widget based on the type of item it is.
      itemBuilder: (context, index) {
        final item = _response[index];

        return ListTile(
          title: item.buildTitle(context),
          subtitle: item.buildSubtitle(context),
        );
      },
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
                          Icon(Icons.date_range,color: Colors.grey,size: 16,),
                          Text(' ${item['date_start']} - ${item['date_end']}')
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
