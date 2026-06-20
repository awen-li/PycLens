# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newline_lf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass('a\nb\r\nc\rd', newline='\n')
    self.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\rd'])
    self.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
    memio = self.ioclass(newline='\n')
    self.assertEqual(memio.write('a\nb\r\nc\rd'), 8)
    memio.seek(0)
    self.assertEqual(list(memio), ['a\n', 'b\r\n', 'c\rd'])
    self.assertEqual(memio.getvalue(), 'a\nb\r\nc\rd')
