# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_fileclosed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        with open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
            self.assertIs(f.closed, False)
        self.assertIs(f.closed, True)
    finally:
        os.remove(os_helper.TESTFN)
