# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_captured_stdin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stdin() as stdin:
        stdin.write('hello\n')
        stdin.seek(0)
        captured = input()
    self.assertEqual(captured, 'hello')
