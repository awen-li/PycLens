# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypingCallableTests_test_consistency

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c1 = typing.Callable[[int, str], dict]
    c2 = collections.abc.Callable[[int, str], dict]
    self.assertEqual(c1.__args__, c2.__args__)
    self.assertEqual(hash(c1.__args__), hash(c2.__args__))
