# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '__contains__\\(\\) takes exactly one argument \\(2 given\\)'
    self.assertRaisesRegex(TypeError, msg, {}.__contains__, 0, 1)
