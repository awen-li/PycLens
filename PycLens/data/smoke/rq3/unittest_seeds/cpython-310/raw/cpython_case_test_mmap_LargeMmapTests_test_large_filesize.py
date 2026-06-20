# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: LargeMmapTests_test_large_filesize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self._make_test_file(6442450943, b' ') as f:
        if sys.maxsize < 6442450944:
            with self.assertRaises(OverflowError):
                mmap.mmap(f.fileno(), 6442450944, access=mmap.ACCESS_READ)
            with self.assertRaises(ValueError):
                mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        with mmap.mmap(f.fileno(), 65536, access=mmap.ACCESS_READ) as m:
            self.assertEqual(m.size(), 6442450944)
