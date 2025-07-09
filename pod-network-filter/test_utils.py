import unittest

from utils import make_http_request


class PodNetworkFilterTest(unittest.TestCase):
    def test_make_http_request(self):
        response, status = make_http_request("https://www.google.com")
        self.assertEqual(response, "success")
        self.assertEqual(status, 200)

        response, status = make_http_request("https://doesnot.exist")
        self.assertEqual(response, "no_such_host")
        self.assertEqual(status, 404)
