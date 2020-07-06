import os
import unittest

from gpapi.googleplay import GooglePlayAPI

class TestGooglePlay(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.EMAIL = os.environ['EMAIL']
        cls.PASSWORD = os.environ['PASSWORD']
        cls.GSFID = int(os.environ['GSFID'], 16)
        # Next, get AUTHSUBTOKEN. These expire, so it must be regenerated each
        # time the tests are run.
        api = GooglePlayAPI(locale='en_US', timezone='EST')
        c_password = api.encrypt_password(
            cls.EMAIL, cls.PASSWORD).decode('utf-8')
        api.getAuthSubToken(cls.EMAIL, c_password)
        cls.AUTHSUBTOKEN = api.authSubToken

    def setUp(self):
        # Create a fresh instance of GooglePlayAPI for each test
        self.API = GooglePlayAPI(locale='en_US', timezone='EST')
        self.API.login(gsfId=self.GSFID, authSubToken=self.AUTHSUBTOKEN)

    def test_search(self):
        # Search for 'firefox', requesting just 1 result
        results = self.API.search('firefox', 1)
        self.assertTrue(len(results), 1)
        # The search can return strange results, so we simply check that it
        # contains some data
        self.assertIn('child', results[0])

    def test_details(self):
        # Get the app details for 'airbnb'
        details = self.API.details('com.airbnb.android')
        # Check if the information in the app details is not none
        self.assertEqual(
            details['details']['appDetails']['developerName'],
            'Airbnb')

    def test_download(self):
        # The method we use to download the APK depends on whether the
        # app has already been "purchased". We've already "purchased" (aka,
        # downloaded) this app, so we simply call the download() method.
        # Otherwise, we would use the delivery() method.
        dl_data = self.API.download('com.airbnb.android')
        self.assertIsNotNone(next(dl_data['file']['data']))
