# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_issue35714

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for s in ('\x00', '2\x00i', b'\x00'):
        with self.assertRaisesRegex(struct.error, 'embedded null character'):
            struct.calcsize(s)
