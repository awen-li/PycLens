# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: MemoryTestMixin_test_readlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    buf = self.buftype('1234567890\n')
    memio = self.ioclass(buf * 10)
    self.assertEqual(memio.readlines(), [buf] * 10)
    memio.seek(5)
    self.assertEqual(memio.readlines(), [buf[5:]] + [buf] * 9)
    memio.seek(0)
    self.assertEqual(memio.readlines(15), [buf] * 2)
    memio.seek(0)
    self.assertEqual(memio.readlines(-1), [buf] * 10)
    memio.seek(0)
    self.assertEqual(memio.readlines(0), [buf] * 10)
    memio.seek(0)
    self.assertEqual(type(memio.readlines()[0]), type(buf))
    memio.seek(0)
    self.assertEqual(memio.readlines(None), [buf] * 10)
    self.assertRaises(TypeError, memio.readlines, '')
    memio.seek(len(buf) * 10 + 1)
    self.assertEqual(memio.readlines(), [])
    memio.close()
    self.assertRaises(ValueError, memio.readlines)
