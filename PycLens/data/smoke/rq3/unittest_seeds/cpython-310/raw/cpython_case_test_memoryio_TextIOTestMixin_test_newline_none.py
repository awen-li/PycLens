# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\nb\r\nc\rd', newline=None)
    self.assertEqual(list(memio), ['a\n', 'b\n', 'c\n', 'd'])
    memio.seek(0)
    self.assertEqual(memio.read(1), 'a')
    self.assertEqual(memio.read(2), '\nb')
    self.assertEqual(memio.read(2), '\nc')
    self.assertEqual(memio.read(1), '\n')
    self.assertEqual(memio.getvalue(), 'a\nb\nc\nd')
    memio = self.ioclass(newline=None)
    self.assertEqual(2, memio.write('a\n'))
    self.assertEqual(3, memio.write('b\r\n'))
    self.assertEqual(3, memio.write('c\rd'))
    memio.seek(0)
    self.assertEqual(memio.read(), 'a\nb\nc\nd')
    self.assertEqual(memio.getvalue(), 'a\nb\nc\nd')
    memio = self.ioclass('a\r\nb', newline=None)
    self.assertEqual(memio.read(3), 'a\nb')
