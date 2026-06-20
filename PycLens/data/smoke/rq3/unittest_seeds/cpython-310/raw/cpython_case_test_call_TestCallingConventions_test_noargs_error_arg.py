# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestCallingConventions_test_noargs_error_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'meth_noargs\\(\\) takes no arguments \\(1 given\\)'
    self.assertRaisesRegex(TypeError, msg, lambda : self.obj.meth_noargs(1))
