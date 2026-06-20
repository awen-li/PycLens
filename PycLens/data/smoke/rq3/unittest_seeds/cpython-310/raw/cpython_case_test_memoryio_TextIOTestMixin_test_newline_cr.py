# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_cr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\nb\r\nc\rd', newline='\r')
    self.assertEqual(memio.read(), 'a\rb\r\rc\rd')
    memio.seek(0)
    self.assertEqual(list(memio), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    self.assertEqual(memio.getvalue(), 'a\rb\r\rc\rd')
    memio = self.ioclass(newline='\r')
    self.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    self.assertEqual(list(memio), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    memio.seek(0)
    self.assertEqual(memio.readlines(), ['a\r', 'b\r', '\r', 'c\r', 'd'])
    self.assertEqual(memio.getvalue(), 'a\rb\r\rc\rd')
