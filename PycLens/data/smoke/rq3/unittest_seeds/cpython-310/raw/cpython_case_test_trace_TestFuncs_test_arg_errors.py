# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_trace.py
# case: TestFuncs_test_arg_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = self.tracer.runfunc(traced_capturer, 1, 2, self=3, func=4)
    self.assertEqual(res, ((1, 2), {'self': 3, 'func': 4}))
    with self.assertRaises(TypeError):
        self.tracer.runfunc(func=traced_capturer, arg=1)
    with self.assertRaises(TypeError):
        self.tracer.runfunc()
