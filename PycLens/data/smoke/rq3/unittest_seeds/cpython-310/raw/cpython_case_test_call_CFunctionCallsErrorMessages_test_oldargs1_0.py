# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: CFunctionCallsErrorMessages_test_oldargs1_0

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'count\\(\\) takes exactly one argument \\(0 given\\)'
    self.assertRaisesRegex(TypeError, msg, [].count)
