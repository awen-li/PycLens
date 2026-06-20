# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keywordonlyarg.py
# case: KeywordOnlyArgTestCase_test_mangling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def f(self, *, __a=42):
            return __a
    self.assertEqual(X().f(), 42)
