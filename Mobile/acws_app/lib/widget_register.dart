import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'app_config.dart' as appConfig;

class RegisterForm extends StatefulWidget {
  const RegisterForm(
    this._toggleRegister, {
    Key key,
  }) : super(key: key);
  final Function _toggleRegister;

  @override
  _RegisterFormState createState() => _RegisterFormState();
}

class _RegisterFormState extends State<RegisterForm> {
  final _formKey = GlobalKey<FormState>();
  final FocusNode _focusNodePassword = FocusNode();
  final FocusNode _focusNodePasswordConfirm = FocusNode();
  final _emailText = TextEditingController();
  final _passwordText = TextEditingController();
  final _passwordConfirmText = TextEditingController();
  bool _obscureText = true;
  bool _waitLogin = false;
  String _invalidEmail;
  String _invalidPassword;

  @override
  void dispose() {
    _focusNodePassword.dispose();
    _focusNodePasswordConfirm.dispose();
    _emailText.dispose();
    _passwordText.dispose();
    _passwordConfirmText.dispose();
    super.dispose();
  }

  void _showSnackBar(String text) {
    Scaffold.of(context).hideCurrentSnackBar();
    Scaffold.of(context).showSnackBar(SnackBar(
      content: Text(text),
    ));
  }

  Future<void> _register() async {
    _invalidEmail = null;
    _invalidPassword = null;
    FocusScope.of(context).unfocus();
    if (_formKey.currentState.validate()) {
      setState(() {
        _waitLogin = true;
      });

      try {
        var response = await http
            .post(appConfig.serverUrl + '/auth/registration/',
                headers: <String, String>{
                  'Content-Type': 'application/json; charset=UTF-8',
                },
                body: jsonEncode(<String, String>{
                  'email': _emailText.text,
                  'password1': _passwordText.text,
                  'password2': _passwordConfirmText.text
                }))
            .timeout(const Duration(seconds: 6));
        if (response.statusCode == 201) {
          var token = jsonDecode(response.body)['key'];
          final prefs = await SharedPreferences.getInstance();
          prefs.setString('authToken', token);
          appConfig.AppData.authToken = token;
          Navigator.pushReplacementNamed(context, '/main');
        } else if (response.statusCode == 400) {
          if (response.body.contains(
              'A user is already registered with this e-mail address.')) {
            _invalidEmail = 'E-mail ซ้ำ กรุณาใช้อีเมลอื่น';
            _formKey.currentState.validate();
          } else if (response.body.contains('Enter a valid email address.')) {
            _invalidEmail = 'E-mail ไม่ถูกต้อง';
            _formKey.currentState.validate();
          } else if (response.body.contains('"password1"')) {
            _invalidPassword = 'รหัสผ่านง่ายเกินไป กรุณาใช้รหัสผ่านอื่น';
            _formKey.currentState.validate();
            Exception(response.body);
          } else {
            throw Exception(response.body);
          }
        } else {
          throw Exception(
              'Request Error Code : ${response.statusCode}/n ${response.body}');
        }
      } catch (e) {
        print(e);
        _showSnackBar('เครือค่ายมีปัญหา กรุณาลองใหม่ภายหลัง');
      } finally {
        setState(() {
          _waitLogin = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
        key: _formKey,
        child: Column(children: <Widget>[
          //Text('สมัครบัญชีผู้ใช้', style: TextStyle(fontSize: 24)),
          //SizedBox(height: 12),
          TextFormField(
            controller: _emailText,
            decoration: const InputDecoration(
              icon: Icon(Icons.email),
              labelText: 'E-mail',
              border: OutlineInputBorder(),
              contentPadding: EdgeInsets.all(12.0),
            ),
            keyboardType: TextInputType.emailAddress,
            validator: (String value) {
              if (value.isEmpty) {
                return 'กรุนาใส่ E-mail';
              }
              if (!RegExp(
                      r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?)*$")
                  .hasMatch(value)) {
                return 'E-mail ไม่ถูกต้อง';
              }
              if (_invalidEmail != null) {
                return _invalidEmail;
              }
              return null;
            },
            textInputAction: TextInputAction.next,
            onEditingComplete: () {
              _focusNodePassword.requestFocus();
            },
          ),
          SizedBox(height: 12),
          TextFormField(
            controller: _passwordText,
            obscureText: _obscureText,
            focusNode: _focusNodePassword,
            decoration: InputDecoration(
              icon: Icon(Icons.lock),
              labelText: 'Password',
              border: OutlineInputBorder(),
              contentPadding: EdgeInsets.all(12.0),
              suffixIcon: IconButton(
                icon: Icon(
                  _obscureText ? Icons.visibility : Icons.visibility_off,
                ),
                onPressed: () {
                  setState(() {
                    _obscureText = !_obscureText;
                  });
                },
              ),
            ),
            validator: (String value) {
              if (value.isEmpty) {
                return 'กรุนาใส่รหัสผ่าน';
              }
              if (value.length < 8) {
                return 'รหัสผ่านต้องมีความยาวอย่างน้อย 8 ตัวอักษร';
              }
              if (RegExp(
                  r"^[0-9]*$")
                  .hasMatch(value)) {
                return 'รหัสผ่านต้องไม่เป็นตัวเลขอย่างเดียว';
              }
              if (_invalidPassword != null) {
                return _invalidPassword;
              }
              return null;
            },
            textInputAction: TextInputAction.next,
            onEditingComplete: () {
              _focusNodePasswordConfirm.requestFocus();
            },
          ),
          SizedBox(height: 12),
          TextFormField(
            controller: _passwordConfirmText,
            obscureText: _obscureText,
            focusNode: _focusNodePasswordConfirm,
            decoration: InputDecoration(
              icon: Icon(Icons.lock),
              labelText: 'Confirm Password',
              border: OutlineInputBorder(),
              contentPadding: EdgeInsets.all(12.0),
              suffixIcon: IconButton(
                icon: Icon(
                  _obscureText ? Icons.visibility : Icons.visibility_off,
                ),
                onPressed: () {
                  setState(() {
                    _obscureText = !_obscureText;
                  });
                },
              ),
            ),
            validator: (String value) {
              if (value.isEmpty) {
                return 'กรุนาใส่รหัสผ่านอีกครั้ง';
              } else if (value != _passwordText.text) {
                return 'รหัสผ่านไม่ตรงกัน';
              }
              return null;
            },
            onEditingComplete: _register,
          ),
          SizedBox(height: 12),
          SizedBox(
            width: double.infinity,
            height: 50,
            child: ElevatedButton(
                onPressed: _waitLogin ? null : _register,
                child: Visibility(
                  child: Text('Sign Up',
                      style: TextStyle(
                        fontSize: 20.0,
                      )),
                  replacement: CircularProgressIndicator(),
                  visible: !_waitLogin,
                )),
          ),
          SizedBox(height: 12),
          SizedBox(
            width: double.infinity,
            height: 40,
            child: OutlinedButton(
                onPressed: _waitLogin
                    ? null
                    : () {
                        FocusScope.of(context).unfocus();
                        widget._toggleRegister();
                      },
                child: Text('Login',
                    style: TextStyle(
                      fontSize: 20.0,
                    ))),
          )
        ]));
  }
}
