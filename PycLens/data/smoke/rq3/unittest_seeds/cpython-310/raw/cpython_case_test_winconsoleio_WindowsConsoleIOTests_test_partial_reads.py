# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winconsoleio.py
# case: WindowsConsoleIOTests_test_partial_reads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = 'ϼўТλФЙ\r\n'.encode('utf-16-le')
    expected = 'ϼўТλФЙ\r\n'.encode('utf-8')
    for read_count in range(1, 16):
        with open('CONIN$', 'rb', buffering=0) as stdin:
            write_input(stdin, source)
            actual = b''
            while not actual.endswith(b'\n'):
                b = stdin.read(read_count)
                actual += b
            self.assertEqual(actual, expected, 'stdin.read({})'.format(read_count))
