# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BytesTest_test_getitem_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'python'
    msg = 'byte indices must be integers or slices'
    with self.assertRaisesRegex(TypeError, msg):
        b['a']
