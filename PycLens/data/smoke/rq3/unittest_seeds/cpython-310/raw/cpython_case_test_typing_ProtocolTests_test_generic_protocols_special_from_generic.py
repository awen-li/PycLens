# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ProtocolTests_test_generic_protocols_special_from_generic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')

    class P(Protocol[T]):
        pass
    self.assertEqual(P.__parameters__, (T,))
    self.assertEqual(P[int].__parameters__, ())
    self.assertEqual(P[int].__args__, (int,))
    self.assertIs(P[int].__origin__, P)
