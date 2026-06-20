# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_subinterps_distinct_state

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for run in self.run_repeated_init_and_subinterpreters():
        (main, *subs, _) = run
        if '0x0' in main:
            raise unittest.SkipTest('platform prints pointers as 0x0')
        for sub in subs:
            self.assertNotEqual(sub.interp, main.interp)
            self.assertNotEqual(sub.tstate, main.tstate)
            self.assertNotEqual(sub.modules, main.modules)
