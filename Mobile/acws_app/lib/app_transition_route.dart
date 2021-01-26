import 'package:flutter/material.dart';

class SlideLeftRoute extends PageRouteBuilder {
  final Widget enterPage;
  final Widget exitPage;
  SlideLeftRoute({this.exitPage, this.enterPage})
      : super(
            pageBuilder: (
              BuildContext context,
              Animation<double> animation,
              Animation<double> secondaryAnimation,
            ) =>
                enterPage,
            transitionsBuilder: (
              BuildContext context,
              Animation<double> animation,
              Animation<double> secondaryAnimation,
              Widget child,
            ) =>
                SlideTransition(
                  position: new Tween<Offset>(
                    begin: const Offset(1.0, 0.0),
                    end: Offset.zero,
                  ).chain(CurveTween(curve: Curves.ease)).animate(animation),
                  child: child,
                ));
}
