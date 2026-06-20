# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_utf8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.server.handler.enable_UTF8 = True
    expected = b'+OK I know RFC6856'
    result = self.client.utf8()
    self.assertEqual(result, expected)
