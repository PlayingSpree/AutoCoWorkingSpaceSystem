import 'package:flutter/material.dart';
import '../../app_util.dart';

class ReportProblem extends StatefulWidget {
  final int user;

  ReportProblem({Key key, @required this.user}) : super(key: key);

  @override
  _ReportProblemState createState() => _ReportProblemState();
}

class _ReportProblemState extends State<ReportProblem> {
  final _formKey = GlobalKey<FormState>();
  final _nameText = TextEditingController();
  bool _wait = false;
  int problemID = 1;

  var _response;
  List<DropdownMenuItem<int>> _list;

  @override
  void initState() {
    super.initState();
    _downloadData();
  }

  Future<void> _downloadData() async {
    var response = await httpGetRequest('/feedback/problem/type/', context);
    setState(() {
      _response = response;
      print(response);
      _list = response.map<DropdownMenuItem<int>>((var value) {
        return DropdownMenuItem<int>(
          value: value['id'],
          child: Row(
            children: [
              Text(value['name']),
              SizedBox(width: 8),
              Text(value['detail'],
                  style: Theme.of(context).textTheme.bodyText2)
            ],
          ),
        );
      }).toList();
    });
  }

  @override
  void dispose() {
    _nameText.dispose();
    super.dispose();
  }

  Future<void> _update() async {
    FocusScope.of(context).unfocus();
    if (_formKey.currentState.validate()) {
      setState(() {
        _wait = true;
      });

      try {
        await httpRequest(
                '/feedback/problem/',
                {
                  'user': widget.user,
                  'text': _nameText.text,
                  'type': problemID
                },
                context,
                method: 'post')
            .timeout(const Duration(seconds: 6));
      } catch (e) {
        print(e);
        ScaffoldMessenger.of(context).hideCurrentSnackBar();
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(
          content: Text('เครือค่ายมีปัญหา กรุณาลองใหม่ภายหลัง'),
        ));
      } finally {
        setState(() {
          _wait = false;
        });
        await showDialog<void>(
          context: context,
          barrierDismissible: false,
          builder: (BuildContext context) {
            return AlertDialog(
              title: Text('รายงานสำเร็จ'),
              actions: <Widget>[
                TextButton(
                  child: Text('OK'),
                  onPressed: () {
                    Navigator.pop(context);
                  },
                ),
              ],
            );
          },
        );
        Navigator.pop(context);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('รายงานปัญหา'),
        ),
        body: Form(
          key: _formKey,
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                Text('ประเภทปัญหา',
                    style: Theme.of(context).textTheme.headline6),
                DropdownButtonFormField(
                  hint: Text('เลือกประเภทปัญหา'),
                  items: _list ?? [],
                  onChanged: (newValue) {
                    setState(() {
                      problemID = newValue;
                    });
                  },
                ),
                SizedBox(height: 12),
                Text('รายละเอียดปัญหา',
                    style: Theme.of(context).textTheme.headline6),
                SizedBox(height: 12),
                Expanded(
                  child: TextFormField(
                    controller: _nameText,
                    keyboardType: TextInputType.multiline,
                    maxLines: null,
                    decoration: const InputDecoration(
                      labelText: 'รายละเอียดปัญหา',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                SizedBox(height: 12),
                SizedBox(
                  width: double.infinity,
                  height: 40,
                  child: ElevatedButton(
                      onPressed: _wait ? null : _update,
                      child: Visibility(
                        child: Text('รายงานปัญหา',
                            style: TextStyle(
                              fontSize: 20.0,
                            )),
                        replacement: CircularProgressIndicator(),
                        visible: !_wait,
                      )),
                ),
              ],
            ),
          ),
        ));
  }
}
