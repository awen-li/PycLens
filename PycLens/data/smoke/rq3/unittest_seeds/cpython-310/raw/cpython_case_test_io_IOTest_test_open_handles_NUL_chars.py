# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: IOTest_test_open_handles_NUL_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fn_with_NUL = 'foo\x00bar'
    self.assertRaises(ValueError, self.open, fn_with_NUL, 'w', encoding='utf-8')
    bytes_fn = bytes(fn_with_NUL, 'ascii')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', DeprecationWarning)
        self.assertRaises(ValueError, self.open, bytes_fn, 'w', encoding='utf-8')
