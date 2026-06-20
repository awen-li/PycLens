# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_abc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(issubclass(ConIO, io.RawIOBase))
    self.assertFalse(issubclass(ConIO, io.BufferedIOBase))
    self.assertFalse(issubclass(ConIO, io.TextIOBase))
