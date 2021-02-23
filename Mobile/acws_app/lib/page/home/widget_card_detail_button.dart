import 'package:acws_app/app_style.dart';
import 'package:flutter/material.dart';

class CardDetailButton extends StatelessWidget {
  const CardDetailButton(
    this.title,
    this.detail,
    this.price, {
    Key key,
    this.onPressed,
  }) : super(key: key);

  final String title;
  final String detail;
  final String price;
  final Function onPressed;

  @override
  Widget build(BuildContext context) {
    return Card(
        color: Theme.of(context).primaryColorLight,
        child: Column(children: [
          Padding(
            padding: const EdgeInsets.only(top: 16.0),
            child: Text(title, style: AppTextStyle.HeaderText),
          ),
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 4),
            child: Text(detail, textAlign: TextAlign.center),
          ),
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: SizedBox(
              width: double.infinity,
              height: 48,
              child: ElevatedButton(
                child: Text(price, style: TextStyle(fontSize: 16.0)),
                onPressed: onPressed,
              ),
            ),
          )
        ]));
  }
}
