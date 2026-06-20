# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_open_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = self.cls(BASE)
    with (p / 'fileA').open('r') as f:
        self.assertIsInstance(f, io.TextIOBase)
        self.assertEqual(f.read(), 'this is file A\n')
    with (p / 'fileA').open('rb') as f:
        self.assertIsInstance(f, io.BufferedIOBase)
        self.assertEqual(f.read().strip(), b'this is file A')
    with (p / 'fileA').open('rb', buffering=0) as f:
        self.assertIsInstance(f, io.RawIOBase)
        self.assertEqual(f.read().strip(), b'this is file A')
