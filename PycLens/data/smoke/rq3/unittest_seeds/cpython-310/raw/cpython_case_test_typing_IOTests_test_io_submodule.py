# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: IOTests_test_io_submodule

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from typing.io import IO, TextIO, BinaryIO, __all__, __name__
    self.assertIs(IO, typing.IO)
    self.assertIs(TextIO, typing.TextIO)
    self.assertIs(BinaryIO, typing.BinaryIO)
    self.assertEqual(set(__all__), set(['IO', 'TextIO', 'BinaryIO']))
    self.assertEqual(__name__, 'typing.io')
