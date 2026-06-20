# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_unlink

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'w', encoding='utf-8') as f:
        pass
    os_helper.unlink(TESTFN)
    self.assertFalse(os.path.exists(TESTFN))
    os_helper.unlink(TESTFN)
