const debugOnEmulator = true;
const serverUrl =
    debugOnEmulator ? 'http://10.0.2.2:8000' : 'http://127.0.0.1:8000';

class AppData {
  static String authToken;
}
