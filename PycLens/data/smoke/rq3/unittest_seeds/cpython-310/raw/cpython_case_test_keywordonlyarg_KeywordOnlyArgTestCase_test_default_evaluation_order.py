# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keywordonlyarg.py
# case: KeywordOnlyArgTestCase_test_default_evaluation_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 42
    with self.assertRaises(NameError) as err:

        def f(v=a, x=b, *, y=c, z=d):
            pass
    self.assertEqual(str(err.exception), "name 'b' is not defined")
    with self.assertRaises(NameError) as err:
        f = lambda v=a, x=b, *, y=c, z=d: None
    self.assertEqual(str(err.exception), "name 'b' is not defined")
