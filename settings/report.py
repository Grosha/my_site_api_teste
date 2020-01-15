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
        # self.pre_condition = ''
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
            .add_title('title')\
            .add_username('username')\
            .add_device('device')\
            .add_os('android')\
            .add_region('usa')\
            .add_str('step 1')\
            .add_ar('win')\
            .add_er('lose')
