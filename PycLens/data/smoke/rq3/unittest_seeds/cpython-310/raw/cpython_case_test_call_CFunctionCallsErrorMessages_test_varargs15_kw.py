# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs15_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^ImportError\\(\\) takes at most 2 keyword arguments \\(3 given\\)$'
    self.assertRaisesRegex(TypeError, msg, ImportError, 0, name=1, path=2, foo=3)
