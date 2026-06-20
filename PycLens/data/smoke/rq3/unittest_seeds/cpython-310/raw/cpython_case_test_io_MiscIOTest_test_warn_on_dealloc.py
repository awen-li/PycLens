# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: MiscIOTest_test_warn_on_dealloc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._check_warn_on_dealloc(os_helper.TESTFN, 'wb', buffering=0)
    self._check_warn_on_dealloc(os_helper.TESTFN, 'wb')
    self._check_warn_on_dealloc(os_helper.TESTFN, 'w', encoding='utf-8')
