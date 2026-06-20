# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\nb\r\nc\rd', newline='')
    self.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\r', 'd'])
    memio.seek(0)
    self.assertEqual(memio.read(4), 'a\nb\r')
    self.assertEqual(memio.read(2), '\nc')
    self.assertEqual(memio.read(1), '\r')
    self.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
    memio = self.ioclass(newline='')
    self.assertEqual(2, memio.write('a\n'))
    self.assertEqual(2, memio.write('b\r'))
    self.assertEqual(2, memio.write('\nc'))
    self.assertEqual(2, memio.write('\rd'))
    memio.seek(0)
    self.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\r', 'd'])
    self.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
