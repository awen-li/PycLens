# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestInterpreterAttrs_test_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp1 = interpreters.create()
    interp2 = interpreters.create()
    self.assertEqual(interp1, interp1)
    self.assertNotEqual(interp1, interp2)
