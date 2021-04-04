import 'package:flutter/material.dart';
import '../../app_util.dart';

class EditPass extends StatefulWidget {
  final Function callback;

  EditPass(
      {Key key, this.callback})
      : super(key: key);

  @override
  _EditPassState createState() => _EditPassState();
}

class _EditPassState extends State<EditPass> {
  final _formKey = GlobalKey<FormState>();
  final _focusNodePhone = FocusNode();
  final _nameText = TextEditingController();
  final _phoneText = TextEditingController();
  bool _wait = false;

  @override
  void dispose() {
    _focusNodePhone.dispose();
    _nameText.dispose();
    _phoneText.dispose();
    super.dispose();
  }

  Future<void> _update() async {
    FocusScope.of(context).unfocus();
    if (_formKey.currentState.validate()) {
      setState(() {
        _wait = true;
      });

      try {
        if (_nameText.text.isEmpty) {}
        var name = _nameText.text.split(' ');
        var lastName = name.removeLast();
        if (name.isEmpty) {
          name.add(lastName);
          lastName = '';
        }

        await httpRequest(
                '/auth/user/',
                {
                  'first_name': name.join(),
                  'last_name': lastName,
                  'phone': _phoneText.text
                },
                context,
                method: 'put')
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
              title: Text('แก้ไขข้อมูลผู้ใช้สำเร็จ'),
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
        if (widget.callback != null) widget.callback();
        Navigator.pop(context);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('แก้ไขข้อมูลผู้ใช้'),
        ),
        body: Form(
          key: _formKey,
          child: Padding(
            padding: const EdgeInsets.all(24.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.start,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                TextFormField(
                  controller: _nameText,
                  decoration: const InputDecoration(
                    icon: Icon(Icons.person),
                    labelText: 'ชื่อ - นามสกุล',
                    border: OutlineInputBorder(),
                  ),
                  keyboardType: TextInputType.name,
                  validator: (String value) {
                    return null;
                  },
                  textInputAction: TextInputAction.next,
                  onEditingComplete: () {
                    _focusNodePhone.requestFocus();
                  },
                ),
                SizedBox(height: 12),
                TextFormField(
                  controller: _phoneText,
                  focusNode: _focusNodePhone,
                  decoration: const InputDecoration(
                    icon: Icon(Icons.phone),
                    labelText: 'เบอร์โทรศัพท์',
                    border: OutlineInputBorder(),
                  ),
                  keyboardType: TextInputType.phone,
                  validator: (String value) {
                    if (value.isNotEmpty &&
                        !RegExp(r"^[0-9]*$").hasMatch(value)) {
                      return 'เบอร์โทรศัพท์ไม่ถูกต้อง';
                    }
                    return null;
                  },
                  textInputAction: TextInputAction.done,
                  onEditingComplete: _update,
                ),
                SizedBox(height: 12),
                SizedBox(
                  width: double.infinity,
                  height: 40,
                  child: ElevatedButton(
                      onPressed: _wait ? null : _update,
                      child: Visibility(
                        child: Text('บันทึกข้อมูลผู้ใช้',
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
