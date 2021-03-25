import 'dart:async';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../../app_transition_route.dart';
import '../../app_util.dart';

class RemotePage extends StatefulWidget {
  @override
  _RemotePageState createState() => _RemotePageState();
}

class _RemotePageState extends State<RemotePage> {
  var _response;

  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/meetingroom/booking/?now', context);
    setState(() {
      _response = response;
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(8.0),
      children: [
        Center(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              'Meeting Room',
              style: Theme.of(context).textTheme.headline6,
            ),
          ),
        ),
        if ((_response ?? []).length == 0)
          Center(child: Text('ไม่มีห้องประชุมที่สามารถควบคุมได้ในขณะนี้'))
        else
          Column(
            children: [
              for (var item in _response ?? [])
                Card(
                  child: ListTile(
                    leading: Icon(Icons.meeting_room),
                    title: Text(item['room']['name']),
                    trailing: Icon(Icons.arrow_forward),
                    onTap: () {
                      Navigator.of(context).push(SlideLeftRoute(
                          exitPage: this.widget,
                          enterPage:
                              RemoteMeetingRoomPage(item['room']['id'])));
                    },
                  ),
                ),
            ],
          ),
      ],
    );
  }
}

class RemoteMeetingRoomPage extends StatefulWidget {
  RemoteMeetingRoomPage(this._room);

  final int _room;

  @override
  _RemoteMeetingRoomPageState createState() => _RemoteMeetingRoomPageState();
}

class _RemoteMeetingRoomPageState extends State<RemoteMeetingRoomPage> {
  var _response;

  @override
  void initState() {
    _loadRemote();
    super.initState();
  }

  Future<void> _loadRemote() async {
    try {
      var response =
          await httpGetRequest('/iot/room/${widget._room}/', context);
      setState(() {
        _response = response;
      });
    } catch (e) {
      print(e);
      Navigator.pop(context);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Meeting Room Remote'),
        ),
        body: _response == null
            ? Center(child: CircularProgressIndicator())
            : ListView.builder(
                padding: const EdgeInsets.all(8),
                itemCount: _response.length + 1,
                itemBuilder: (BuildContext context, int index) {
                  if (index == 0) {
                    return Card(
                      child: ListTile(
                        leading: Icon(Icons.lock_open),
                        title: Text('ปลดล็อกประตู'),
                        onTap: () {},
                      ),
                    );
                  } else {
                    index -= 1;
                    switch (_response[index]['type']) {
                      case 'Temp':
                        return DiscreteNumberRemote(
                            _response[index]['name'],
                            _response[index]['data']['temp'],
                            _response[index]['data_info']['temp']['min'],
                            _response[index]['data_info']['temp']['max'],
                            Icons.ac_unit,
                            '°C',
                            widget._room,
                            _response[index]['id'],
                            'temp');
                        break;
                      case 'ColorBrightnessLight':
                        return null; // TODO
                        break;
                      default:
                        return null;
                    }
                  }
                }));
  }
}

class DiscreteNumberRemote extends StatefulWidget {
  const DiscreteNumberRemote(
    this._label,
    this._value,
    this._min,
    this._max,
    this._icon,
    this._unit,
    this._room,
    this._iotId,
    this._iotDataKey, {
    Key key,
  }) : super(key: key);
  final String _label;
  final int _value;
  final int _min;
  final int _max;
  final IconData _icon;
  final String _unit;
  final int _room;
  final int _iotId;
  final String _iotDataKey;

  @override
  _DiscreteNumberRemoteState createState() =>
      _DiscreteNumberRemoteState(_value);
}

class _DiscreteNumberRemoteState extends State<DiscreteNumberRemote> {
  int _value;
  Timer _timer;

  _DiscreteNumberRemoteState(this._value);

  @override
  void initState() {
    super.initState();
  }

  void valueUpdate() {
    if (_timer == null || !_timer.isActive) {
      _timer = Timer(Duration(seconds: 1), sendUpdate);
    } else {
      _timer.cancel();
      _timer = Timer(Duration(seconds: 1), sendUpdate);
    }
  }

  Future<void> sendUpdate() async {
    try {
      await httpRequest(
          '/iot/room/${widget._room}/',
          {
            'iot_id': widget._iotId,
            'data': {widget._iotDataKey: _value}
          },
          context,
          method: 'put');
    } catch (e) {
      print(e);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
        child: Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Text(
            widget._label,
            style: Theme.of(context).textTheme.headline5,
          ),
        ),
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Ink(
                decoration: ShapeDecoration(
                  color: _value == widget._min
                      ? Theme.of(context).disabledColor
                      : Theme.of(context).primaryColor,
                  shape: CircleBorder(),
                ),
                child: IconButton(
                  icon: Icon(Icons.remove,
                      color: Theme.of(context).accentIconTheme.color),
                  onPressed: _value == widget._min
                      ? null
                      : () {
                          if (_value > widget._min) {
                            setState(() {
                              _value--;
                            });
                            valueUpdate();
                          }
                        },
                ),
              ),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Center(
                    child: Row(
                  children: [
                    if (widget._icon != null) Icon(widget._icon),
                    Text(
                      '${widget._icon == null ? '' : ' '}$_value ${widget._unit}',
                      style: Theme.of(context).textTheme.headline6,
                    ),
                  ],
                )),
              ),
              Ink(
                decoration: ShapeDecoration(
                  color: _value == widget._max
                      ? Theme.of(context).disabledColor
                      : Theme.of(context).primaryColor,
                  shape: CircleBorder(),
                ),
                child: IconButton(
                  icon: Icon(Icons.add,
                      color: Theme.of(context).accentIconTheme.color),
                  onPressed: _value == widget._max
                      ? null
                      : () {
                          if (_value < widget._max) {
                            setState(() {
                              _value++;
                            });
                            valueUpdate();
                          }
                        },
                ),
              ),
            ],
          ),
        ),
      ],
    ));
  }
}
