# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_DataTests_test_geturl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.text_url_resp.geturl(), self.text_url)
    self.assertEqual(self.text_url_base64_resp.geturl(), self.text_url_base64)
    self.assertEqual(self.image_url_resp.geturl(), self.image_url)
