# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestCallingConventions_test_o_error_no_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'meth_o\\(\\) takes exactly one argument \\(0 given\\)'
    self.assertRaisesRegex(TypeError, msg, self.obj.meth_o)
