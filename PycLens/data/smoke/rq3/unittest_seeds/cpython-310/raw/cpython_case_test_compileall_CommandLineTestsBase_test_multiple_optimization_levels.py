# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compileall.py
# case: CommandLineTestsBase_test_multiple_optimization_levels

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = os.path.join(self.directory, 'optimizations')
    os.makedirs(path)
    script = script_helper.make_script(path, 'test_optimization', 'a = 0')
    bc = []
    for opt_level in ('', 1, 2, 3):
        bc.append(importlib.util.cache_from_source(script, optimization=opt_level))
    test_combinations = [['0', '1'], ['1', '2'], ['0', '2'], ['0', '1', '2']]
    for opt_combination in test_combinations:
        self.assertRunOK(path, *('-o' + str(n) for n in opt_combination))
        for opt_level in opt_combination:
            self.assertTrue(os.path.isfile(bc[int(opt_level)]))
            try:
                os.unlink(bc[opt_level])
            except Exception:
                pass
