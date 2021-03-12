import 'package:acws_app/app_style.dart';
import 'package:acws_app/page/home/widget_card_detail_button.dart';
import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

import '../../app_transition_route.dart';
import '../../app_util.dart';
import 'payment.dart';

class Reserve extends StatefulWidget {
  @override
  _ReserveState createState() => _ReserveState();
}

class _ReserveState extends State<Reserve> {
  DateTime date;
  TimeOfDay timeStart;
  TimeOfDay timeEnd;
  String validationText;

  List<dynamic> _response;

  Future<void> selectDate() async {
    var pickedDate = await showDatePicker(
        context: context,
        firstDate: DateTime.now(),
        lastDate: DateTime.now().add(Duration(days: 365)),
        initialDate: date ?? DateTime.now());
    if (pickedDate == null || pickedDate == date) return;
    setState(() {
      date = pickedDate;
    });
    validateDateTime();
  }

  Future<void> selectTime(bool isStart) async {
    var pickedTime = await showTimePicker(
        context: context,
        initialTime: isStart
            ? timeStart ?? TimeOfDay(hour: 8, minute: 0)
            : timeEnd ?? TimeOfDay(hour: 16, minute: 0));
    if (pickedTime == null) return;

    setState(() {
      if (isStart)
        timeStart = pickedTime;
      else
        timeEnd = pickedTime;
    });
    validateDateTime();
  }

  void validateDateTime() {
    if (date == null || timeStart == null || timeEnd == null) return;
    var validateText;
    if (timeStart.hour >= timeEnd.hour && timeStart.minute >= timeEnd.minute) {
      validateText = 'กรุณาเลือกเวลาสิ้นสุดหลังเวลาเริ่ม';
    }
    if (date != null && timeStart != null && timeEnd != null) {
      DateTime now = DateTime.now();
      DateTime today = DateTime(now.year, now.month, now.day);
      if (date == today &&
          timeStart.hour < now.hour &&
          timeStart.minute < now.minute) {
        validateText = 'กรุณาเลือกเวลาเริ่มหลังเวลาปัจจุบัน';
      }
    }
    setState(() {
      _response = null;
      validationText = validateText;
    });
    if (validateText == null) {
      _downloadData();
    }
  }

  Future<void> _downloadData() async {
    List<dynamic> response = await httpGetRequest(
        '/meetingroom/type/?start=${_dateString(true, true)}&end=${_dateString(false, true)}',
        context);
    response.removeWhere((element) => element['available'] == 0);
    setState(() {
      _response = response;
    });
  }

  void _goToPayment(var roomType) {
    double duration = ((timeEnd.hour + timeEnd.minute / 60) -
        (timeStart.hour + timeStart.minute / 60));
    Navigator.of(context).push(SlideLeftRoute(
        exitPage: this.widget,
        enterPage: PaymentPage(
            title: roomType['name'],
            detail: roomType['detail'],
            detailList: {
              'วันที่จอง': '${DateFormat.EEEE().add_yMd().format(date)}',
              'เวลาที่จอง':
                  '${timeStart.format(context)} - ${timeEnd.format(context)}',
              'ระยะเวลา': '$duration ชม.',
              'ราคาต่อชั่วโมง': '${roomType['price']} ฿ / ชม.'
            },
            price: (roomType['price'] * duration).round(),
            paymentFor: PaymentFor.meetingRoom,
            data: {
              "room_type": roomType['id'],
              "date_start": _dateString(true),
              "date_end": _dateString(false)
            })));
  }

  String _dateString(bool start, [bool ignoreTimeZone = false]) {
    return DateTime(
                date.year,
                date.month,
                date.day,
                start ? timeStart.hour : timeEnd.hour,
                start ? timeStart.minute : timeEnd.minute)
            .toIso8601String() +
        (ignoreTimeZone ? '' : date.timeZoneName);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text('จอง Meeting Room'),
        ),
        body: ListView(padding: const EdgeInsets.all(8.0), children: [
          Column(
            children: [
              Text('วันและเวลาที่จอง', style: AppTextStyle.HeaderText),
              SizedBox(height: 8),
              Card(
                child: ListTile(
                  leading: Icon(Icons.date_range),
                  title: Text(date == null
                      ? 'เลือกวันที่จอง'
                      : DateFormat.EEEE().add_yMd().format(date)),
                  onTap: selectDate,
                ),
              ),
              SizedBox(height: 8),
              Row(
                children: [
                  Expanded(
                    child: Card(
                      child: ListTile(
                        leading: Icon(Icons.schedule),
                        title: Text(timeStart == null
                            ? 'เริ่ม'
                            : timeStart.format(context)),
                        onTap: () => selectTime(true),
                      ),
                    ),
                  ),
                  SizedBox(width: 48, child: Center(child: Text('ถึง'))),
                  Expanded(
                    child: Card(
                      child: ListTile(
                        leading: Icon(Icons.schedule),
                        title: Text(timeEnd == null
                            ? 'สิ้นสุด'
                            : timeEnd.format(context)),
                        onTap: () => selectTime(false),
                      ),
                    ),
                  ),
                ],
              ),
              SizedBox(height: 8),
              if (validationText != null)
                Text(validationText,
                    style: AppTextStyle.HeaderText.copyWith(
                        color: Theme.of(context).errorColor)),
              AnimatedOpacity(
                  child: Column(
                    children: [
                      Text('เลือกประเภทห้องประชุม',
                          style: AppTextStyle.HeaderText),
                      SizedBox(height: 8),
                      AnimatedCrossFade(
                          duration: const Duration(milliseconds: 200),
                          crossFadeState: _response == null
                              ? CrossFadeState.showFirst
                              : CrossFadeState.showSecond,
                          firstChild: SizedBox(
                            height: 48,
                            child: Center(
                              child: CircularProgressIndicator(
                                  valueColor: new AlwaysStoppedAnimation<Color>(
                                      Theme.of(context).primaryColor)),
                            ),
                          ),
                          secondChild: _response != null &&
                                  _response.length == 0
                              ? Center(
                                  child:
                                      Text('ไม่มีห้องว่างในเวลาที่ท่านเลือก'))
                              : Column(children: [
                                  for (var roomType in _response ?? [])
                                    CardDetailButton(
                                        roomType['name'],
                                        roomType['detail'],
                                        '${roomType['price']} ฿ / ชม.',
                                        onPressed: () {
                                      _goToPayment(roomType);
                                    })
                                ])),
                    ],
                  ),
                  opacity: (date == null ||
                          timeStart == null ||
                          timeEnd == null ||
                          validationText != null)
                      ? 0
                      : 1,
                  duration: const Duration(milliseconds: 200))
            ],
          )
        ]));
  }
}
