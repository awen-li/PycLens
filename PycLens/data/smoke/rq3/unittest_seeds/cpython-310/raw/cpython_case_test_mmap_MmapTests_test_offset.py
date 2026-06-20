# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'w+b')
    try:
        halfsize = mmap.ALLOCATIONGRANULARITY
        m = self.make_mmap_file(f, halfsize)
        m.close()
        f.close()
        mapsize = halfsize * 2
        f = open(TESTFN, 'r+b')
        for offset in [-2, -1, None]:
            try:
                m = mmap.mmap(f.fileno(), mapsize, offset=offset)
                self.assertEqual(0, 1)
            except (ValueError, TypeError, OverflowError):
                pass
            else:
                self.assertEqual(0, 0)
        f.close()
        f = open(TESTFN, 'r+b')
        m = mmap.mmap(f.fileno(), mapsize - halfsize, offset=halfsize)
        self.assertEqual(m[0:3], b'foo')
        f.close()
        try:
            m.resize(512)
        except SystemError:
            pass
        else:
            self.assertEqual(len(m), 512)
            self.assertRaises(ValueError, m.seek, 513, 0)
            self.assertEqual(m[0:3], b'foo')
            f = open(TESTFN, 'rb')
            f.seek(0, 2)
            self.assertEqual(f.tell(), halfsize + 512)
            f.close()
            self.assertEqual(m.size(), halfsize + 512)
        m.close()
    finally:
        f.close()
        try:
            os.unlink(TESTFN)
        except OSError:
            pass
