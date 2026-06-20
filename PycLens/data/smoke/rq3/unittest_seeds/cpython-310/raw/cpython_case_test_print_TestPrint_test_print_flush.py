# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_print.py
# case: TestPrint_test_print_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class filelike:

        def __init__(self):
            self.written = ''
            self.flushed = 0

        def write(self, str):
            self.written += str

        def flush(self):
            self.flushed += 1
    f = filelike()
    print(1, file=f, end='', flush=True)
    print(2, file=f, end='', flush=True)
    print(3, file=f, flush=False)
    self.assertEqual(f.written, '123\n')
    self.assertEqual(f.flushed, 2)

    class noflush:

        def write(self, str):
            pass

        def flush(self):
            raise RuntimeError
    self.assertRaises(RuntimeError, print, 1, file=noflush(), flush=True)
