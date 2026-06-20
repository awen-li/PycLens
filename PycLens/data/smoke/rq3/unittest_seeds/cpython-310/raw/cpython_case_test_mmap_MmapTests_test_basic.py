# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'bw+')
    try:
        f.write(b'\x00' * PAGESIZE)
        f.write(b'foo')
        f.write(b'\x00' * (PAGESIZE - 3))
        f.flush()
        m = mmap.mmap(f.fileno(), 2 * PAGESIZE)
    finally:
        f.close()
    tp = str(type(m))
    self.assertEqual(m.find(b'foo'), PAGESIZE)
    self.assertEqual(len(m), 2 * PAGESIZE)
    self.assertEqual(m[0], 0)
    self.assertEqual(m[0:3], b'\x00\x00\x00')
    self.assertRaises(IndexError, m.__getitem__, len(m))
    self.assertRaises(IndexError, m.__setitem__, len(m), b'\x00')
    m[0] = b'3'[0]
    m[PAGESIZE + 3:PAGESIZE + 3 + 3] = b'bar'
    self.assertEqual(m[0], b'3'[0])
    self.assertEqual(m[0:3], b'3\x00\x00')
    self.assertEqual(m[PAGESIZE - 1:PAGESIZE + 7], b'\x00foobar\x00')
    m.flush()
    match = re.search(b'[A-Za-z]+', m)
    if match is None:
        self.fail('regex match on mmap failed!')
    else:
        (start, end) = match.span(0)
        length = end - start
        self.assertEqual(start, PAGESIZE)
        self.assertEqual(end, PAGESIZE + 6)
    m.seek(0, 0)
    self.assertEqual(m.tell(), 0)
    m.seek(42, 1)
    self.assertEqual(m.tell(), 42)
    m.seek(0, 2)
    self.assertEqual(m.tell(), len(m))
    self.assertRaises(ValueError, m.seek, -1)
    self.assertRaises(ValueError, m.seek, 1, 2)
    self.assertRaises(ValueError, m.seek, -len(m) - 1, 2)
    try:
        m.resize(512)
    except SystemError:
        pass
    else:
        self.assertEqual(len(m), 512)
        self.assertRaises(ValueError, m.seek, 513, 0)
        f = open(TESTFN, 'rb')
        try:
            f.seek(0, 2)
            self.assertEqual(f.tell(), 512)
        finally:
            f.close()
        self.assertEqual(m.size(), 512)
    m.close()
