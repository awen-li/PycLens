# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlretrieve_FileTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = urllib.request.urlretrieve('file:%s' % os_helper.TESTFN)
    self.assertEqual(result[0], os_helper.TESTFN)
    self.assertIsInstance(result[1], email.message.Message, 'did not get an email.message.Message instance as second returned value')
