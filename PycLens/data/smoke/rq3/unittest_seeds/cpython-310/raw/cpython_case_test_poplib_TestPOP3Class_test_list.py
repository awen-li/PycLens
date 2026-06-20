# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_poplib.py
# case: TestPOP3Class_test_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.client.list()[1:], ([b'1 1', b'2 2', b'3 3', b'4 4', b'5 5'], 25))
    self.assertTrue(self.client.list('1').endswith(b'OK 1 1'))
