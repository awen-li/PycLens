# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_total

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    D = TypedDict('D', {'x': int}, total=False)
    self.assertEqual(D(), {})
    self.assertEqual(D(x=1), {'x': 1})
    self.assertEqual(D.__total__, False)
    self.assertEqual(D.__required_keys__, frozenset())
    self.assertEqual(D.__optional_keys__, {'x'})
    self.assertEqual(Options(), {})
    self.assertEqual(Options(log_level=2), {'log_level': 2})
    self.assertEqual(Options.__total__, False)
    self.assertEqual(Options.__required_keys__, frozenset())
    self.assertEqual(Options.__optional_keys__, {'log_level', 'log_path'})
