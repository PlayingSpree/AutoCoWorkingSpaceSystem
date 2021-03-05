import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:shared_preferences/shared_preferences.dart';

import 'app_config.dart' as appConfig;

Future<dynamic> httpGetRequest(String url, BuildContext context) async {
  final token = appConfig.AppData.authToken;
  var response = await http.get(appConfig.serverUrl + url, headers: {
    'accept': 'application/json',
    'Content-Type': 'application/json; charset=UTF-8',
    HttpHeaders.authorizationHeader: 'Token ' + token
  }).timeout(const Duration(seconds: 6));
  if (response.statusCode == 200) {
    return json.decode(utf8.decode(response.bodyBytes));
  } else if (response.statusCode == 403) {
    if (response.body == '{"detail":"Invalid token."}') {
      final prefs = await SharedPreferences.getInstance();
      prefs.remove('authToken');
      Navigator.pushReplacementNamed(context, '/login');
    }
  } else {
    throw Exception(response.body);
  }
  return null;
}

Future<dynamic> httpRequest(String url, var body, BuildContext context,
    {String method = 'post'}) async {
  final token = appConfig.AppData.authToken;
  var methodFunction;
  switch (method) {
    case 'put':
      methodFunction = http.put;
      break;
    case 'patch':
      methodFunction = http.patch;
      break;
    default:
      methodFunction = http.post;
  }
  http.Response response = await methodFunction(appConfig.serverUrl + url,
          headers: {
            'accept': 'application/json',
            'Content-Type': 'application/json; charset=UTF-8',
            HttpHeaders.authorizationHeader: 'Token ' + token
          },
          body: jsonEncode(body))
      .timeout(const Duration(seconds: 6));
  if (response.statusCode >= 200 && response.statusCode < 300) {
    return json.decode(utf8.decode(response.bodyBytes));
  } else if (response.statusCode == 403) {
    if (response.body == '{"detail":"Invalid token."}') {
      final prefs = await SharedPreferences.getInstance();
      prefs.remove('authToken');
      Navigator.pushReplacementNamed(context, '/login');
    }
  } else {
    throw Exception(response.body);
  }
  return null;
}
