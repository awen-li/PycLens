# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CastTests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(cast(int, 42), 42)
    self.assertEqual(cast(float, 42), 42)
    self.assertIs(type(cast(float, 42)), int)
    self.assertEqual(cast(Any, 42), 42)
    self.assertEqual(cast(list, 42), 42)
    self.assertEqual(cast(Union[str, float], 42), 42)
    self.assertEqual(cast(AnyStr, 42), 42)
    self.assertEqual(cast(None, 42), 42)
