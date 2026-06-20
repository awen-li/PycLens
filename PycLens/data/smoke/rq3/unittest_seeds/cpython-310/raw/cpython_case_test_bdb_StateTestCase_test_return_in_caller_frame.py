# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: StateTestCase_test_return_in_caller_frame

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expect_set = [('line', 2, 'tfunc_main'), ('step',), ('line', 3, 'tfunc_main'), ('step',), ('call', 1, 'tfunc_first'), ('up',), ('None', 3, 'tfunc_main'), ('return',), ('return', 7, 'tfunc_main'), ('quit',)]
    with TracerRun(self) as tracer:
        tracer.runcall(tfunc_main)
