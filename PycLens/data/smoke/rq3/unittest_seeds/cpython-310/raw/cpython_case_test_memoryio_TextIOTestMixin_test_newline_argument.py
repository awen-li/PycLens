# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_argument

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.ioclass, newline=b'\n')
    self.assertRaises(ValueError, self.ioclass, newline='error')
    for newline in (None, '', '\n', '\r', '\r\n'):
        self.ioclass(newline=newline)
