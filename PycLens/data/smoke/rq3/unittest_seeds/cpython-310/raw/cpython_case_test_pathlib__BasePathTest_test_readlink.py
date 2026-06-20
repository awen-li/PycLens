# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePathTest_test_readlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls(BASE)
    self.assertEqual((P / 'linkA').readlink(), self.cls('fileA'))
    self.assertEqual((P / 'brokenLink').readlink(), self.cls('non-existing'))
    self.assertEqual((P / 'linkB').readlink(), self.cls('dirB'))
    with self.assertRaises(OSError):
        (P / 'fileA').readlink()
