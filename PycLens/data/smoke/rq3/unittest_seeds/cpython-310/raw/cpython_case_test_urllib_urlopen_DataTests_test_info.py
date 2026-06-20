# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_DataTests_test_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(self.text_url_resp.info(), email.message.Message)
    self.assertEqual(self.text_url_base64_resp.info().get_params(), [('text/plain', ''), ('charset', 'ISO-8859-1')])
    self.assertEqual(self.image_url_resp.info()['content-length'], str(len(self.image)))
    self.assertEqual(urllib.request.urlopen('data:,').info().get_params(), [('text/plain', ''), ('charset', 'US-ASCII')])
