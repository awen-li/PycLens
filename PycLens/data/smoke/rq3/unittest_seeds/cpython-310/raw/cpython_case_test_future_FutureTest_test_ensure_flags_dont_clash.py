# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future.py
# case: FutureTest_test_ensure_flags_dont_clash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flags = {f'CO_FUTURE_{future.upper()}': getattr(__future__, future).compiler_flag for future in __future__.all_feature_names}
    flags |= {flag: getattr(ast, flag) for flag in dir(ast) if flag.startswith('PyCF_')}
    self.assertCountEqual(set(flags.values()), flags.values())
