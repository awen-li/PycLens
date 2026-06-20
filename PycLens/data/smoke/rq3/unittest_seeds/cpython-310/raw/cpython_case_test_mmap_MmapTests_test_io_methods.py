# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_io_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = b'0123456789'
    with open(TESTFN, 'wb') as fp:
        fp.write(b'x' * len(data))
    with open(TESTFN, 'r+b') as f:
        m = mmap.mmap(f.fileno(), len(data))
    for i in range(len(data)):
        self.assertEqual(m.tell(), i)
        m.write_byte(data[i])
        self.assertEqual(m.tell(), i + 1)
    self.assertRaises(ValueError, m.write_byte, b'x'[0])
    self.assertEqual(m[:], data)
    m.seek(0)
    for i in range(len(data)):
        self.assertEqual(m.tell(), i)
        self.assertEqual(m.read_byte(), data[i])
        self.assertEqual(m.tell(), i + 1)
    self.assertRaises(ValueError, m.read_byte)
    m.seek(3)
    self.assertEqual(m.read(3), b'345')
    self.assertEqual(m.tell(), 6)
    m.seek(3)
    m.write(b'bar')
    self.assertEqual(m.tell(), 6)
    self.assertEqual(m[:], b'012bar6789')
    m.write(bytearray(b'baz'))
    self.assertEqual(m.tell(), 9)
    self.assertEqual(m[:], b'012barbaz9')
    self.assertRaises(ValueError, m.write, b'ba')
