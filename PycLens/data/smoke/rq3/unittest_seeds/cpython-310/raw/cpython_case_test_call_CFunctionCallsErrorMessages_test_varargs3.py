# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^from_bytes\\(\\) takes exactly 2 positional arguments \\(3 given\\)'
    self.assertRaisesRegex(TypeError, msg, int.from_bytes, b'a', 'little', False)
