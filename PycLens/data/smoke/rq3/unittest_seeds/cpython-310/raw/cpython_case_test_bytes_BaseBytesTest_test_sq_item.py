# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_sq_item

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    _testcapi = import_helper.import_module('_testcapi')
    obj = self.type2test((42,))
    with self.assertRaises(IndexError):
        _testcapi.sequence_getitem(obj, -2)
    with self.assertRaises(IndexError):
        _testcapi.sequence_getitem(obj, 1)
    self.assertEqual(_testcapi.sequence_getitem(obj, 0), 42)
