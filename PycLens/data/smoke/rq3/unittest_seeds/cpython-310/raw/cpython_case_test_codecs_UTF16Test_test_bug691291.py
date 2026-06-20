# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF16Test_test_bug691291

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = 'Hello\r\nworld\r\n'
    s = s1.encode(self.encoding)
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with open(os_helper.TESTFN, 'wb') as fp:
        fp.write(s)
    with warnings_helper.check_warnings(('', DeprecationWarning)):
        reader = codecs.open(os_helper.TESTFN, 'U', encoding=self.encoding)
    with reader:
        self.assertEqual(reader.read(), s1)
