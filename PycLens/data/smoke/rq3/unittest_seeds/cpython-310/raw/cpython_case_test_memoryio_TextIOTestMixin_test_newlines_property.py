# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_memoryio.py
# case: TextIOTestMixin_test_newlines_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    memio = self.ioclass(newline=None)

    def force_decode():
        memio.seek(0)
        memio.read()
    self.assertEqual(memio.newlines, None)
    memio.write('a\n')
    force_decode()
    self.assertEqual(memio.newlines, '\n')
    memio.write('b\r\n')
    force_decode()
    self.assertEqual(memio.newlines, ('\n', '\r\n'))
    memio.write('c\rd')
    force_decode()
    self.assertEqual(memio.newlines, ('\r', '\n', '\r\n'))
