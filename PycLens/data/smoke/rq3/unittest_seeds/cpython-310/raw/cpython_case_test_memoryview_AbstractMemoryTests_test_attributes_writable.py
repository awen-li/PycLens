# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryview.py
# case: AbstractMemoryTests_test_attributes_writable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not self.rw_type:
        self.skipTest('no writable type to test')
    m = self.check_attributes_with_type(self.rw_type)
    self.assertEqual(m.readonly, False)
