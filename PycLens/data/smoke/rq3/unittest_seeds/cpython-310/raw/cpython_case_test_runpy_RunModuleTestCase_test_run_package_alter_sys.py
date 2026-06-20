# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_run_package_alter_sys

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for depth in range(1, 4):
        if verbose > 1:
            print('Testing package depth:', depth)
        self._check_package(depth, alter_sys=True)
