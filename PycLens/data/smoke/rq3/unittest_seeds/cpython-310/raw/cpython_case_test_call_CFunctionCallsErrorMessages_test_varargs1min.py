# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs1min

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'get expected at least 1 argument, got 0'
    self.assertRaisesRegex(TypeError, msg, {}.get)
    msg = 'expected 1 argument, got 0'
    self.assertRaisesRegex(TypeError, msg, {}.__delattr__)
