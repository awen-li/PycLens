# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_runpy.py
# case: RunModuleTestCase_test_run_module_in_namespace_package

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for depth in range(1, 4):
        if verbose > 1:
            print('Testing package depth:', depth)
        self._check_module(depth, namespace=True, parent_namespaces=True)
