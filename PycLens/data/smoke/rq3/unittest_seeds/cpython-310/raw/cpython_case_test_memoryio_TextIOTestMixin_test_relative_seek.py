# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_relative_seek

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass()
    self.assertRaises(OSError, memio.seek, -1, 1)
    self.assertRaises(OSError, memio.seek, 3, 1)
    self.assertRaises(OSError, memio.seek, -3, 1)
    self.assertRaises(OSError, memio.seek, -1, 2)
    self.assertRaises(OSError, memio.seek, 1, 1)
    self.assertRaises(OSError, memio.seek, 1, 2)
