# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_move

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(TESTFN, 'wb+') as f:
        f.write(b'ABCDEabcde')
        f.flush()
        mf = mmap.mmap(f.fileno(), 10)
        mf.move(5, 0, 5)
        self.assertEqual(mf[:], b'ABCDEABCDE', 'Map move should have duplicated front 5')
        mf.close()
    data = b'0123456789'
    for dest in range(len(data)):
        for src in range(len(data)):
            for count in range(len(data) - max(dest, src)):
                expected = data[:dest] + data[src:src + count] + data[dest + count:]
                m = mmap.mmap(-1, len(data))
                m[:] = data
                m.move(dest, src, count)
                self.assertEqual(m[:], expected)
                m.close()
    m = mmap.mmap(-1, 100)
    offsets = [-100, -1, 0, 1, 100]
    for (source, dest, size) in itertools.product(offsets, offsets, offsets):
        try:
            m.move(source, dest, size)
        except ValueError:
            pass
    offsets = [(-1, -1, -1), (-1, -1, 0), (-1, 0, -1), (0, -1, -1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
    for (source, dest, size) in offsets:
        self.assertRaises(ValueError, m.move, source, dest, size)
    m.close()
    m = mmap.mmap(-1, 1)
    self.assertRaises(ValueError, m.move, 0, 0, 2)
    self.assertRaises(ValueError, m.move, 1, 0, 1)
    self.assertRaises(ValueError, m.move, 0, 1, 1)
    m.move(0, 0, 1)
    m.move(0, 0, 0)
