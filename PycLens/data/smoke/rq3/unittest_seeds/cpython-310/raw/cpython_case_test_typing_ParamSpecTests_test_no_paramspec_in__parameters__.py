# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_no_paramspec_in__parameters__

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')
    self.assertNotIn(P, List[P].__parameters__)
    self.assertIn(T, Tuple[T, P].__parameters__)
    self.assertNotIn(P, list[P].__parameters__)
    self.assertIn(T, tuple[T, P].__parameters__)
    self.assertNotIn(P, (list[P] | int).__parameters__)
    self.assertIn(T, (tuple[T, P] | int).__parameters__)
