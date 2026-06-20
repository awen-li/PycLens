# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_tougher_find

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb+') as f:
        data = b'aabaac\x00deef\x00\x00aa\x00'
        n = len(data)
        f.write(data)
        f.flush()
        m = mmap.mmap(f.fileno(), n)
    for start in range(n + 1):
        for finish in range(start, n + 1):
            slice = data[start:finish]
            self.assertEqual(m.find(slice), data.find(slice))
            self.assertEqual(m.find(slice + b'x'), -1)
    m.close()
