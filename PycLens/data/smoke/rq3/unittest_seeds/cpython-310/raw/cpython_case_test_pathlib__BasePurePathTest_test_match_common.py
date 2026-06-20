# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BasePurePathTest_test_match_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = self.cls
    self.assertRaises(ValueError, P('a').match, '')
    self.assertRaises(ValueError, P('a').match, '.')
    self.assertTrue(P('b.py').match('b.py'))
    self.assertTrue(P('a/b.py').match('b.py'))
    self.assertTrue(P('/a/b.py').match('b.py'))
    self.assertFalse(P('a.py').match('b.py'))
    self.assertFalse(P('b/py').match('b.py'))
    self.assertFalse(P('/a.py').match('b.py'))
    self.assertFalse(P('b.py/c').match('b.py'))
    self.assertTrue(P('b.py').match('*.py'))
    self.assertTrue(P('a/b.py').match('*.py'))
    self.assertTrue(P('/a/b.py').match('*.py'))
    self.assertFalse(P('b.pyc').match('*.py'))
    self.assertFalse(P('b./py').match('*.py'))
    self.assertFalse(P('b.py/c').match('*.py'))
    self.assertTrue(P('ab/c.py').match('a*/*.py'))
    self.assertTrue(P('/d/ab/c.py').match('a*/*.py'))
    self.assertFalse(P('a.py').match('a*/*.py'))
    self.assertFalse(P('/dab/c.py').match('a*/*.py'))
    self.assertFalse(P('ab/c.py/d').match('a*/*.py'))
    self.assertTrue(P('/b.py').match('/*.py'))
    self.assertFalse(P('b.py').match('/*.py'))
    self.assertFalse(P('a/b.py').match('/*.py'))
    self.assertFalse(P('/a/b.py').match('/*.py'))
    self.assertTrue(P('/a/b.py').match('/a/*.py'))
    self.assertFalse(P('/ab.py').match('/a/*.py'))
    self.assertFalse(P('/a/b/c.py').match('/a/*.py'))
    self.assertFalse(P('/a/b/c.py').match('/**/*.py'))
    self.assertTrue(P('/a/b/c.py').match('/a/**/*.py'))
