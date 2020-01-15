import json

from settings.json_encoder import JSONEncoderWithoutModificator


class Report(object):
    def __init__(self):
        self._title = ''
        self._str = ''
        self._actual_result = ''
        self._expected_result = ''
        self._os_info = ''
        self._device_info = ''
        self._username = ''
        self._region = ''
        self._app_name = ''
        self._version_app = ''
        self._crash_log_file = None

    def add_title(self, text):
        self._title = text
        return self

    def add_str(self, text):
        self._str = text
        return self

    def add_os(self, os):
        self._os_info = os
        return self

    def add_device(self, device_info):
        self._device_info = device_info
        return self

    def add_username(self, username):
        self._username = username
        return self

    def add_region(self, region):
        self._region = region
        return self

    def add_ar(self, result):
        self._actual_result = result
        return self

    def add_er(self, result):
        self._expected_result = result
        return self

    def attach_file(self, file):
        self._crash_log_file = file
        return self

    def add_app_name(self, name):
        self._app_name = name
        return self

    def add_app_version(self, version):
        self._version_app = version
        return self

    @property
    def report(self):
        return json.dumps(self, cls=JSONEncoderWithoutModificator)


class MySiteReport(object):
    def __init__(self, priority=None, report=None):
        if priority:
            self._priority = priority
        if report:
            self._report = report

    @property
    def report(self):
        return json.dumps(self, cls=JSONEncoderWithoutModificator)


default_bug = Report()\
            .add_title('Application crashes if change application to another after message was sent to the friend in chat')\
            .add_app_name('WOT Assistance')\
            .add_app_version('3.2.1(13991)')\
            .add_username('chicago_bulls')\
            .add_device('Samsung s10+')\
            .add_os('android 9.1')\
            .add_region('usa')\
            .add_str('1. autorize user\n'
                     '2. select chat category in menu\n'
                     '3. select one of your friends\n'
                     '4. send message to him\n'
                     '5. via resent app change focus to another device application\n'
                     '6. return to the WOT Assistance app via resent apps')\
            .add_ar('Application crashes')\
            .add_er('Opened screen with sent message to your friend')\
            .attach_file('crash.file')
