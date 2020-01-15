import pytest

from settings.report import MySiteReport, default_bug
from settings.services import my_site
from settings.user import User


class TestSendReport:

    @pytest.fixture(scope="module", autouse=True)
    def authorize_user(self):
        user = User(username='Alan', password='Rickman')
        token = my_site.authorize(user=user.credential).get('token')
        global headers
        headers = user.get_headers(token)
        yield

    @pytest.mark.parametrize(
        'priority',
        [1, 5]
    )
    def test_send_report(self, priority):
        my_site_report = MySiteReport(priority=str(priority), report=default_bug.report)
        response = my_site.submit_report(headers=headers, report=my_site_report.report)

        assert response.get('status') == 200, 'Incorrect status code when send report'

    @pytest.mark.parametrize(
        'priority',
        [0, 6]
    )
    def test_send_report_with_incorrect_priority(self, priority):
        my_site_report = MySiteReport(priority=str(priority), report=default_bug.report)
        response = my_site.submit_report(headers=headers, report=my_site_report.report)

        assert response.get('status') == 404, 'Incorrect status code when send incorrect report priority'
        assert response.get('message') == 'Priority for report is incorrect',\
            'Incorrect massage when send incorrect report priority'

    def test_send_report_without_priority(self):
        my_site_report = MySiteReport(report=default_bug.report)
        response = my_site.submit_report(headers=headers, report=my_site_report.report)

        assert response.get('status') == 404, 'Incorrect status code when send incorrect report priority'
        assert response.get('message') == 'Priority for report is incorrect',\
            'Incorrect massage when send incorrect report priority'

    def test_send_report_with_empty_message(self):
        my_site_report = MySiteReport(priority=3, report='')
        response = my_site.submit_report(headers=headers, report=my_site_report.report)

        assert response.get('status') == 404, 'Incorrect status code when send empty report'
        assert response.get('message') == 'Report is empty', \
            'Incorrect massage when send send empty report'
