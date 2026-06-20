# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keywordonlyarg.py
# case: KeywordOnlyArgTestCase_test_kwonly_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Example:

        def f(self, *, k1=1, k2=2):
            return (k1, k2)
    self.assertEqual(Example().f(k1=1, k2=2), (1, 2))
    self.assertEqual(Example.f(Example(), k1=1, k2=2), (1, 2))
    self.assertRaises(TypeError, Example.f, k1=1, k2=2)
