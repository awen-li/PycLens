# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_ctrl_z

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open('CONIN$', 'rb', buffering=0) as stdin:
        source = 'Ä\x1a\r\n'.encode('utf-16-le')
        expected = 'Ä'.encode('utf-8')
        write_input(stdin, source)
        (a, b) = (stdin.read(1), stdin.readall())
        self.assertEqual(expected[0:1], a)
        self.assertEqual(expected[1:], b)
