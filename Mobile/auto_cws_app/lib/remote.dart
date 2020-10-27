import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import 'app_transition_route.dart';

class RemotePage extends StatefulWidget {
  @override
  _RemotePageState createState() => _RemotePageState();
}

class _RemotePageState extends State<RemotePage> {
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.all(8.0),
      children: [
        Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(4.0),
              child: Text(
                'Co-working Space',
                style: Theme.of(context).textTheme.headline6,
              ),
            ),
            Card(
              child: ListTile(
                leading: Icon(Icons.lock_open),
                title: Text('ปลดล็อกประตู Co-working Space'),
                onTap: () {},
              ),
            )
          ],
        ),
        Center(
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              'Meeting Room',
              style: Theme.of(context).textTheme.headline6,
            ),
          ),
        ),
        Card(
          child: ListTile(
            leading: Icon(Icons.meeting_room),
            title: Text('ห้องประชุม 401 (4 คน)'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {
              Navigator.of(context).push(SlideLeftRoute(
                  exitPage: this.widget, enterPage: RemoteMeetingRoomPage()));
            },
          ),
        ),
        Card(
          child: ListTile(
            leading: Icon(Icons.meeting_room),
            title: Text('ห้องประชุม 601 (6 คน)'),
            trailing: Icon(Icons.arrow_forward),
            onTap: () {},
          ),
        )
      ],
    );
  }
}

class RemoteMeetingRoomPage extends StatefulWidget {
  @override
  _RemoteMeetingRoomPageState createState() => _RemoteMeetingRoomPageState();
}

class _RemoteMeetingRoomPageState extends State<RemoteMeetingRoomPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('Meeting Room Remote'),
          bottom: PreferredSize(child: LinearProgressIndicator()),
        ),
        body: ListView(
          padding: const EdgeInsets.all(8.0),
          children: [
            Card(
              child: ListTile(
                leading: Icon(Icons.lock_open),
                title: Text('ปลดล็อกประตู'),
                onTap: () {},
              ),
            ),
            DiscreteNumberRemote('อุณหภูมิห้อง', 25, 20, 30)
          ],
        ));
  }
}

class DiscreteNumberRemote extends StatefulWidget {
  const DiscreteNumberRemote(
    this._label,
    this._value,
    this._min,
    this._max, {
    Key key,
  }) : super(key: key);
  final String _label;
  final int _value;
  final int _min;
  final int _max;
  @override
  _DiscreteNumberRemoteState createState() =>
      _DiscreteNumberRemoteState(_value);
}

class _DiscreteNumberRemoteState extends State<DiscreteNumberRemote> {
  int _value = 0;

  _DiscreteNumberRemoteState(this._value);
  @override
  Widget build(BuildContext context) {
    return Card(
        child: Column(
      children: [
        Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Icon(Icons.ac_unit),
              Text(
                widget._label,
                style: Theme.of(context).textTheme.headline5,
              ),
            ],
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
                          if (_value > widget._min)
                            setState(() {
                              _value--;
                            });
                        },
                ),
              ),
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Center(
                    child: Text(
                  '$_value °C',
                  style: Theme.of(context).textTheme.headline6,
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
                          if (_value < widget._max)
                            setState(() {
                              _value++;
                            });
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
