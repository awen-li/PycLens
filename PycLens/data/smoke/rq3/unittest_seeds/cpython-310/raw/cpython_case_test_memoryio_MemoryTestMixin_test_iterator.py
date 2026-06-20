# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890\n')
    memio = self.ioclass(buf * 10)
    self.assertEqual(iter(memio), memio)
    self.assertTrue(hasattr(memio, '__iter__'))
    self.assertTrue(hasattr(memio, '__next__'))
    i = 0
    for line in memio:
        self.assertEqual(line, buf)
        i += 1
    self.assertEqual(i, 10)
    memio.seek(0)
    i = 0
    for line in memio:
        self.assertEqual(line, buf)
        i += 1
    self.assertEqual(i, 10)
    memio.seek(len(buf) * 10 + 1)
    self.assertEqual(list(memio), [])
    memio = self.ioclass(buf * 2)
    memio.close()
    self.assertRaises(ValueError, memio.__next__)
