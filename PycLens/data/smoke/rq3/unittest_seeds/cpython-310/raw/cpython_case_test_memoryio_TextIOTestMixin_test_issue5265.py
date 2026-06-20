# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_issue5265

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\r\nb\r\n', newline=None)
    self.assertEqual(memio.read(5), 'a\nb\n')
    self.assertEqual(memio.getvalue(), 'a\nb\n')
