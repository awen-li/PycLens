# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_no_unicode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_no_unicode('md5')
    self.check_no_unicode('sha1')
    self.check_no_unicode('sha224')
    self.check_no_unicode('sha256')
    self.check_no_unicode('sha384')
    self.check_no_unicode('sha512')
