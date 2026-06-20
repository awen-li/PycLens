# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_struct.py
# case: StructTest_test_nN_code

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def assertStructError(func, *args, **kwargs):
        with self.assertRaises(struct.error) as cm:
            func(*args, **kwargs)
        self.assertIn('bad char in struct format', str(cm.exception))
    for code in 'nN':
        for byteorder in ('=', '<', '>', '!'):
            format = byteorder + code
            assertStructError(struct.calcsize, format)
            assertStructError(struct.pack, format, 0)
            assertStructError(struct.unpack, format, b'')
