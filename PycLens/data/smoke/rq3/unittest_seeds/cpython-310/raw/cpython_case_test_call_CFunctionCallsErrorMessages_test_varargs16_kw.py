# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs16_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^min\\(\\) takes at most 2 keyword arguments \\(3 given\\)$'
    self.assertRaisesRegex(TypeError, msg, min, 0, default=1, key=2, foo=3)
