import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';
import 'app_config.dart' as appConfig;

class LoginPage extends StatefulWidget {
  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.blueAccent,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text('Login Page', style: TextStyle(fontSize: 64)),
            LoginForm()
          ],
        ),
      ),
    );
  }
}

class LoginForm extends StatefulWidget {
  @override
  _LoginFormState createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  final _formKey = GlobalKey<FormState>();
  final FocusNode _focusNodePassword = FocusNode();
  final _emailText = TextEditingController();
  final _passwordText = TextEditingController();
  bool _obscureText = true;
  bool _waitLogin = false;
  bool _waitCheckToken = true;
  bool _invalidEmail = false;

  @override
  void initState() {
    _tokenCheck();
    super.initState();
  }

  @override
  void dispose() {
    _focusNodePassword.dispose();
    _emailText.dispose();
    _passwordText.dispose();
    super.dispose();
  }

  void _showSnackBar(String text) {
    Scaffold.of(context).hideCurrentSnackBar();
    Scaffold.of(context).showSnackBar(SnackBar(
      content: Text(text),
    ));
  }

  Future<void> _tokenCheck() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final token = prefs.getString('loginToken');
      if (token == null) {
        throw ('Cannot read token.');
      }
      var response = await http.get(appConfig.serverUrl + '/auth/user/',
          headers: {
            'accept': 'application/json',
            HttpHeaders.authorizationHeader: 'Token ' + token
          }).timeout(const Duration(seconds: 6));
      if (response.statusCode == 200) {
        _loginComplete(token);
      } else if (response.statusCode == 403) {
        if (response.body == '{"detail":"Invalid token."}') {
          _showSnackBar('Token ผิดพลาด กรุณา Login ใหม่อีกครั้ง');
          prefs.remove('loginToken');
        } else {
          throw Exception(
              '\nRequest Error Code: ${response.statusCode}\n ${response.body}');
        }
      }
    } catch (e) {
      print(e);
      if (e != 'Cannot read token.') {
        _showSnackBar('เครือค่ายมีปัญหา กรุณาลองใหม่ภายหลัง');
      }
      setState(() {
        _waitCheckToken = false;
      });
    }
  }

  void _loginComplete(String token) {
    appConfig.AppData.loginToken = token;
    Navigator.pushReplacementNamed(context, '/home');
  }

  Future<void> _login() async {
    _invalidEmail = false;
    if (_formKey.currentState.validate()) {
      setState(() {
        _waitLogin = true;
      });

      try {
        var response = await http
            .post(appConfig.serverUrl + '/auth/login/',
                headers: <String, String>{
                  'Content-Type': 'application/json; charset=UTF-8',
                },
                body: jsonEncode(<String, String>{
                  'email': _emailText.text,
                  'password': _passwordText.text
                }))
            .timeout(const Duration(seconds: 6));
        if (response.statusCode == 200) {
          var token = jsonDecode(response.body)['key'];
          final prefs = await SharedPreferences.getInstance();
          prefs.setString('loginToken', token);
          _loginComplete(token);
        } else if (response.statusCode == 400) {
          if (response.body ==
              '{"non_field_errors":["Unable to log in with provided credentials."]}') {
            _showSnackBar('E-mail และรหัสผ่านไม่ตรงกัน กรุณาตรวจสอบอีกครั้ง');
          } else if (response.body ==
              '{"email":["Enter a valid email address."]}') {
            _invalidEmail = true;
            _formKey.currentState.validate();
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
    if (_waitCheckToken) {
      return CircularProgressIndicator(
          valueColor: new AlwaysStoppedAnimation<Color>(Colors.white));
    } else {
      return Container(
        margin: const EdgeInsets.all(12.0),
        padding: const EdgeInsets.all(12.0),
        color: Colors.white,
        child: Form(
            key: _formKey,
            child: Column(children: <Widget>[
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
                  if (_invalidEmail ||
                      !RegExp(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,253}[a-zA-Z0-9])?)*$")
                          .hasMatch(value)) {
                    return 'กรุนาาตรวจสอบ E-mail อีกครั้ง';
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
                  return null;
                },
                onEditingComplete: _login,
              ),
              SizedBox(height: 12),
              SizedBox(
                width: 150,
                height: 50,
                child: ElevatedButton(
                    onPressed: _waitLogin ? null : _login,
                    child: Visibility(
                      child: Text('Login',
                          style: TextStyle(
                            fontSize: 20.0,
                          )),
                      replacement: CircularProgressIndicator(),
                      visible: !_waitLogin,
                    )),
              ),
              SizedBox(height: 12),
              SizedBox(
                width: 150,
                height: 50,
                child: OutlinedButton(
                    onPressed: () {},
                    child: Text('Sign Up',
                        style: TextStyle(
                          fontSize: 20.0,
                        ))),
              )
            ])),
      );
    }
  }
}