# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: LargeMmapTests_test_large_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._make_test_file(5637144575, b' ') as f:
        with mmap.mmap(f.fileno(), 0, offset=5368709120, access=mmap.ACCESS_READ) as m:
            self.assertEqual(m[268435455], 32)
