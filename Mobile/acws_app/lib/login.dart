import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:flutter_facebook_login/flutter_facebook_login.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'app_config.dart' as appConfig;
import 'widget_register.dart';
import 'icons/social_icons.dart';

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
  bool _registerForm = false;
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

  void _loginComplete(String token) {
    appConfig.AppData.authToken = token;
    Navigator.pushReplacementNamed(context, '/main');
  }

  Future<void> _tokenCheck() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      final token = prefs.getString('authToken');
      if (token == null) {
        throw ('Cannot read token.');
      }
      var response = await http.get(appConfig.serverUrl + '/auth/user/',
          headers: {
            'accept': 'application/json',
            HttpHeaders.authorizationHeader: 'Token ' + token
          }).timeout(const Duration(seconds: 6));
      if (response.statusCode == 200) {
        await Future.delayed(Duration(seconds: 1));
        _loginComplete(token);
      } else if (response.statusCode == 403) {
        if (response.body.contains('"detail":"Invalid token."')) {
          _showSnackBar('Token ผิดพลาด กรุณา Login ใหม่อีกครั้ง');
          prefs.remove('authToken');
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

  Future<void> _login() async {
    _invalidEmail = false;
    FocusScope.of(context).unfocus();
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
        await _checkLoginResponse(response);
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

  Future _checkLoginResponse(http.Response response) async {
    if (response.statusCode == 200) {
      var token = jsonDecode(response.body)['key'];
      final prefs = await SharedPreferences.getInstance();
      prefs.setString('authToken', token);
      _loginComplete(token);
    } else if (response.statusCode == 400) {
      if (response.body
          .contains('Unable to log in with provided credentials.')) {
        _showSnackBar('E-mail และรหัสผ่านไม่ตรงกัน กรุณาตรวจสอบอีกครั้ง');
      } else if (response.body.contains('Enter a valid email address.')) {
        _invalidEmail = true;
        _formKey.currentState.validate();
      } else {
        throw Exception(response.body);
      }
    } else {
      throw Exception(
          'Request Error Code : ${response.statusCode}/n ${response.body}');
    }
  }

  Future<void> _loginFacebook() async {
    FocusScope.of(context).unfocus();
    setState(() {
      _waitLogin = true;
    });

    final facebookLogin = FacebookLogin();
    final result = await facebookLogin.logIn(['email']);

    switch (result.status) {
      case FacebookLoginStatus.loggedIn:
        try {
          var response = await http
              .post(appConfig.serverUrl + '/auth/facebook/',
                  headers: <String, String>{
                    'Content-Type': 'application/json; charset=UTF-8',
                  },
                  body: jsonEncode(<String, String>{
                    'access_token': result.accessToken.token,
                  }))
              .timeout(const Duration(seconds: 6));
          await _checkLoginResponse(response);
        } catch (e) {
          print(e);
          _showSnackBar('เครือค่ายมีปัญหา กรุณาลองใหม่ภายหลัง');
        } finally {
          setState(() {
            _waitLogin = false;
          });
        }
        break;
      case FacebookLoginStatus.cancelledByUser:
        _showSnackBar('ยกเลิกการ Login โดยผู้ใช้งาน');
        break;
      case FacebookLoginStatus.error:
        _showSnackBar('Login Error: ' + result.errorMessage);
        print(result.errorMessage);
        break;
    }
    setState(() {
      _waitLogin = false;
    });
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
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.all(Radius.circular(10))),
          child: AnimatedCrossFade(
            duration: const Duration(milliseconds: 200),
            firstCurve: Curves.easeIn,
            secondCurve: Curves.easeIn,
            crossFadeState: _registerForm
                ? CrossFadeState.showSecond
                : CrossFadeState.showFirst,
            firstChild: Form(
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
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton(
                      onPressed: _waitLogin ? null : _login,
                      child: Visibility(
                        child: Text('Login',
                            style: TextStyle(
                              fontSize: 24.0,
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
                              setState(() {
                                _registerForm = !_registerForm;
                              });
                            },
                      child: Text('Sign Up',
                          style: TextStyle(
                            fontSize: 16.0,
                          ))),
                ),
                SizedBox(height: 12),
                Text('OR',
                    style: TextStyle(
                      fontSize: 16.0,
                    )),
                SizedBox(height: 12),
                SizedBox(
                  width: double.infinity,
                  height: 40,
                  child: OutlinedButton(
                      onPressed: _waitLogin ? null : _loginFacebook,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Icon(SocialIcons.facebook,
                              size: 24, color: Color(0xFF1778F2)),
                          Text('Login with Facebook',
                              style: TextStyle(
                                color: Color(0xFF1778F2),
                                fontSize: 16.0,
                              )),
                          SizedBox(
                            width: 0,
                          )
                        ],
                      )),
                ),
                SizedBox(height: 12),
                SizedBox(
                  width: double.infinity,
                  height: 40,
                  child: OutlinedButton(
                      onPressed: _waitLogin ? null : _loginFacebook,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          Icon(SocialIcons.google,
                              size: 24, color: Color(0xFFDB4437)),
                          Text('Login with Google',
                              style: TextStyle(
                                color: Color(0xFFDB4437),
                                fontSize: 16.0,
                              )),
                          SizedBox(
                            width: 0,
                          )
                        ],
                      )),
                )
              ]),
            ),
            secondChild: RegisterForm(() {
              setState(() {
                _registerForm = !_registerForm;
              });
            }),
          ));
    }
  }
}
