# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: StateTestCase_test_until_with_too_large_count

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.expect_set = [('line', 2, 'tfunc_main'), break_in_func('tfunc_first'), ('None', 2, 'tfunc_main'), ('continue',), ('line', 2, 'tfunc_first', ({1: 1}, [])), ('until', (9999,)), ('return', 4, 'tfunc_first'), ('quit',)]
    with TracerRun(self) as tracer:
        tracer.runcall(tfunc_main)
