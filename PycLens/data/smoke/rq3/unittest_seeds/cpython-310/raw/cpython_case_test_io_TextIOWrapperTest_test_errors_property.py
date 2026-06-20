# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_errors_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8') as f:
        self.assertEqual(f.errors, 'strict')
    with self.open(os_helper.TESTFN, 'w', encoding='utf-8', errors='replace') as f:
        self.assertEqual(f.errors, 'replace')
