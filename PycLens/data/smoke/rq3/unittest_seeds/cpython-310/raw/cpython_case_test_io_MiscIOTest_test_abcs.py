# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_abcs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(self.IOBase, abc.ABCMeta)
    self.assertIsInstance(self.RawIOBase, abc.ABCMeta)
    self.assertIsInstance(self.BufferedIOBase, abc.ABCMeta)
    self.assertIsInstance(self.TextIOBase, abc.ABCMeta)
