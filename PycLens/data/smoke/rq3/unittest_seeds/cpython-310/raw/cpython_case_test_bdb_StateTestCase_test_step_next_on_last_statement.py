# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bdb.py
# case: StateTestCase_test_step_next_on_last_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for set_type in ('step', 'next'):
        with self.subTest(set_type=set_type):
            self.expect_set = [('line', 2, 'tfunc_main'), ('step',), ('line', 3, 'tfunc_main'), ('step',), ('call', 1, 'tfunc_first'), ('break', (__file__, 3)), ('None', 1, 'tfunc_first'), ('continue',), ('line', 3, 'tfunc_first', ({1: 1}, [])), (set_type,), ('line', 4, 'tfunc_first'), ('quit',)]
            with TracerRun(self) as tracer:
                tracer.runcall(tfunc_main)
