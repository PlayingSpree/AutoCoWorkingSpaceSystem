import 'package:flutter/material.dart';

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
  final FocusNode _focusNodePhone = FocusNode();
  final FocusNode _focusNodePassword = FocusNode();
  final FocusNode _focusNodePasswordConfirm = FocusNode();
  final _emailText = TextEditingController();
  final _phoneText = TextEditingController();
  final _passwordText = TextEditingController();
  final _passwordConfirmText = TextEditingController();
  bool _obscureText = true;
  bool _waitLogin = false;
  bool _invalidEmail = false;

  @override
  void dispose() {
    _focusNodePassword.dispose();
    _focusNodePasswordConfirm.dispose();
    _phoneText.dispose();
    _emailText.dispose();
    _passwordText.dispose();
    _passwordConfirmText.dispose();
    super.dispose();
  }

  Future<void> _register() async {
    _invalidEmail = false;
    _formKey.currentState.validate();
  }

  @override
  Widget build(BuildContext context) {
    return Form(
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
                return 'E-mail ไม่ถูกต้อง';
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
            controller: _phoneText,
            decoration: const InputDecoration(
              icon: Icon(Icons.phone),
              labelText: 'Phone Number',
              border: OutlineInputBorder(),
              contentPadding: EdgeInsets.all(12.0),
            ),
            keyboardType: TextInputType.phone,
            validator: (String value) {
              if (value.isEmpty) {
                return 'กรุนาใส่เบอร์โทรศัพท์';
              }
              if (!RegExp(r"^0[0-9]{9}$").hasMatch(value)) {
                return 'เบอร์โทรศัพท์ไม่ถูกต้อง';
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
                return 'กรุนาใส่รหัสผ่าน';
              } else if (value != _passwordText.text) {
                return 'รหัสผ่านไม่ตรงกัน';
              }
              return null;
            },
            onEditingComplete: _register,
          ),
          SizedBox(height: 12),
          SizedBox(
            width: 150,
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
            width: 150,
            height: 50,
            child: OutlinedButton(
                onPressed: () {
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
