# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_nonbuffered_textio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_no_resource_warning(self):
        with self.assertRaises(ValueError):
            self.open(os_helper.TESTFN, 'w', encoding='utf-8', buffering=0)
