# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_main_relative_import

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for depth in range(2, 5):
        if verbose > 1:
            print('Testing main relative imports at depth:', depth)
        self._check_relative_imports(depth, '__main__')
