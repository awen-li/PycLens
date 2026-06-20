# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlopen_DataTests_test_read_text_base64

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.text_url_base64_resp.read().decode(dict(self.text_url_base64_resp.info().get_params())['charset']), self.text)
