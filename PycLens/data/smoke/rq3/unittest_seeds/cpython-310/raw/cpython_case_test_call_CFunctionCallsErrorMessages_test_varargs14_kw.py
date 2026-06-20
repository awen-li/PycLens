# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_varargs14_kw

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^product\\(\\) takes at most 1 keyword argument \\(2 given\\)$'
    self.assertRaisesRegex(TypeError, msg, itertools.product, 0, repeat=1, foo=2)
