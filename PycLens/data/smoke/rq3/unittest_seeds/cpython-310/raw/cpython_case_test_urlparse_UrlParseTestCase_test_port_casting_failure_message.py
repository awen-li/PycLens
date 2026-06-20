# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_port_casting_failure_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    message = "Port could not be cast to integer value as 'oracle'"
    p1 = urllib.parse.urlparse('http://Server=sde; Service=sde:oracle')
    with self.assertRaisesRegex(ValueError, message):
        p1.port
    p2 = urllib.parse.urlsplit('http://Server=sde; Service=sde:oracle')
    with self.assertRaisesRegex(ValueError, message):
        p2.port
