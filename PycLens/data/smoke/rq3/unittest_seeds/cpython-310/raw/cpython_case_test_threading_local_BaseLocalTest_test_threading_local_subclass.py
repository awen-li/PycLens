# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading_local.py
# case: BaseLocalTest_test_threading_local_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class LocalSubclass(self._local):
        """To test that subclasses behave properly."""
    self._test_one_class(LocalSubclass)
