# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs17_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^print\\(\\) takes at most 4 keyword arguments \\(5 given\\)$'
    self.assertRaisesRegex(TypeError, msg, print, 0, sep=1, end=2, file=3, flush=4, foo=5)
