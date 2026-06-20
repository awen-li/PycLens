# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: ByteArrayTest_test_mutating_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Boom:

        def __index__(self):
            b.clear()
            return 0
    with self.subTest('tp_as_mapping'):
        b = bytearray(b'Now you see me...')
        with self.assertRaises(IndexError):
            b[0] = Boom()
    with self.subTest('tp_as_sequence'):
        _testcapi = import_helper.import_module('_testcapi')
        b = bytearray(b'Now you see me...')
        with self.assertRaises(IndexError):
            _testcapi.sequence_setitem(b, 0, Boom())
