# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs12_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^staticmethod\\(\\) takes no keyword arguments$'
    self.assertRaisesRegex(TypeError, msg, staticmethod, func=id)
