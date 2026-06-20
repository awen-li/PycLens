# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_parts_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sep = self.sep
    P = self.cls
    p = P('a/b')
    parts = p.parts
    self.assertEqual(parts, ('a', 'b'))
    self.assertIs(parts, p.parts)
    p = P('/a/b')
    parts = p.parts
    self.assertEqual(parts, (sep, 'a', 'b'))
