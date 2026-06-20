# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    m = Match[Union[str, bytes]]
    with self.assertRaises(TypeError):
        m[str]
    with self.assertRaises(TypeError):
        isinstance(42, Pattern[str])
    with self.assertRaises(TypeError):
        issubclass(Pattern[bytes], Pattern[str])
