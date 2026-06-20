# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_crlf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\nb\r\nc\rd', newline='\r\n')
    self.assertEqual(memio.read(), 'a\r\nb\r\r\nc\rd')
    memio.seek(0)
    self.assertEqual(list(memio), ['a\r\n', 'b\r\r\n', 'c\rd'])
    memio.seek(0)
    self.assertEqual(memio.readlines(), ['a\r\n', 'b\r\r\n', 'c\rd'])
    self.assertEqual(memio.getvalue(), 'a\r\nb\r\r\nc\rd')
    memio = self.ioclass(newline='\r\n')
    self.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    self.assertEqual(list(memio), ['a\r\n', 'b\r\r\n', 'c\rd'])
    self.assertEqual(memio.getvalue(), 'a\r\nb\r\r\nc\rd')
