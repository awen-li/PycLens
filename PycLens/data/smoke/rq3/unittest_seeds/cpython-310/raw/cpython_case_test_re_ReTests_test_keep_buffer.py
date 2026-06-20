# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_keep_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = bytearray(b'x')
    it = re.finditer(b'a', b)
    with self.assertRaises(BufferError):
        b.extend(b'x' * 400)
    list(it)
    del it
    gc_collect()
    b.extend(b'x' * 400)
