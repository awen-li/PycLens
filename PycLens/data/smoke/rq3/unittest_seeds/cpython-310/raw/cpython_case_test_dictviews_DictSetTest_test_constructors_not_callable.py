# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dictviews.py
# case: DictSetTest_test_constructors_not_callable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    kt = type({}.keys())
    self.assertRaises(TypeError, kt, {})
    self.assertRaises(TypeError, kt)
    it = type({}.items())
    self.assertRaises(TypeError, it, {})
    self.assertRaises(TypeError, it)
    vt = type({}.values())
    self.assertRaises(TypeError, vt, {})
    self.assertRaises(TypeError, vt)
