# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamic.py
# case: RebindBuiltinsTests_test_eval_gives_lambda_custom_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    globals_dict = {'len': lambda x: 7}
    foo = eval('lambda: len([])', globals_dict)
    self.configure_func(foo)
    self.assertEqual(foo(), 7)
