# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_basic_plain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = ParamSpec('P')
    self.assertEqual(P, P)
    self.assertIsInstance(P, ParamSpec)
