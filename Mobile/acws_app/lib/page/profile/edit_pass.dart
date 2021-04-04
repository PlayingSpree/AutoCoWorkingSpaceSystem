import 'package:flutter/material.dart';
import '../../app_util.dart';

class EditPass extends StatefulWidget {
  EditPass({Key key}) : super(key: key);

  @override
  _EditPassState createState() => _EditPassState();
}

class _EditPassState extends State<EditPass> {
  final _formKey = GlobalKey<FormState>();
  final _focusNodePhone = FocusNode();
  final _pass1Text = TextEditingController();
  final _pass2Text = TextEditingController();
  bool _wait = false;

  @override
  void dispose() {
    _focusNodePhone.dispose();
    _pass1Text.dispose();
    _pass2Text.dispose();
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
                '/auth/password/change/',
                {
                  'new_password1': _pass1Text.text,
                  'new_password2': _pass2Text.text,
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
              title: Text('แก้ไขรหัสผ่านสำเร็จ'),
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
          title: Text('แก้ไขรหัสผ่าน'),
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
                  controller: _pass1Text,
                  obscureText: true,
                  keyboardType: TextInputType.visiblePassword,
                  decoration: const InputDecoration(
                    icon: Icon(Icons.lock),
                    labelText: 'รหัสผ่านใหม่',
                    border: OutlineInputBorder(),
                  ),
                  validator: (String value) {
                    if (value.isEmpty) {
                      return 'กรุนาใส่รหัสผ่าน';
                    }
                    if (value.length < 8) {
                      return 'รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร';
                    }
                    if (RegExp(r"^[0-9]*$").hasMatch(value)) {
                      return 'รหัสผ่านต้องไม่เป็นตัวเลขอย่างเดียว';
                    }
                    return null;
                  },
                  textInputAction: TextInputAction.next,
                  onEditingComplete: () {
                    _focusNodePhone.requestFocus();
                  },
                ),
                SizedBox(height: 12),
                TextFormField(
                  controller: _pass2Text,
                  focusNode: _focusNodePhone,
                  obscureText: true,
                  keyboardType: TextInputType.visiblePassword,
                  decoration: const InputDecoration(
                    icon: Icon(Icons.lock),
                    labelText: 'รหัสผ่านใหม่อีกครั้ง',
                    border: OutlineInputBorder(),
                  ),
                  validator: (String value) {
                    if (value.isEmpty) {
                      return 'กรุนาใส่รหัสผ่านอีกครั้ง';
                    } else if (value != _pass1Text.text) {
                      return 'รหัสผ่านไม่ตรงกัน';
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
                        child: Text('บันทึกรหัสผ่านใหม่',
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
