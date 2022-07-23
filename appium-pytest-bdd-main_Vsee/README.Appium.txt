AppiumSession=============================================================================
1. open cmd in folder which contain apk file
2. get name of device: adb devices
name: R58R332YAYL
3. install apk: adb install VSee-vsee-beta.apk
4. Setup json in appium solfware
4.1 real device
{
  "platformName": "Android",
  "platformVersion": "11",
  "deviceName": "R58R332YAYL", //replace your devicename here R58R332YAYL
  "fullReset": "false",
  "appPackage": "com.vsee.vsee.beta",
  "appWaitActivity": "com.vsee.activity.LoginActivity",
  "app": "C:\\Users\\vuvan\\OneDrive\\Documents\\Vsee\\appium-pytest-bdd-main_Vsee\\source\\VSee-vsee-beta.apk"
}
4.2 simulator
{
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "appPackage": "com.vsee.vsee.beta",
  "appWaitActivity": "com.vsee.activity.LoginActivity",
  "app": "C:\\Users\\vuvan\\OneDrive\\Documents\\Vsee\\appium-pytest-bdd-main_Vsee\\source\\VSee-vsee-beta.apk"
}
5. run test
cd to tests folder
pip3 install -r requirements.txt
python3 -m pytest --html=report/report.html --css=report/highcontrast.css --css=report/accessible.css --self-contained-html

6. result:
https://app-automate.browserstack.com/builds/cba2e2a0e447aa89f62b21429fdc7368a8f43173/sessions/216977debdf2fb3076d0be1c8c3ca9104f30865c?auth_token=a58ee9e99203f0f2dc504b3cbbb0bb8299ce21cf0cfc8cdb000b51d6997af2a7