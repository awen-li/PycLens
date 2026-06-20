# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_support.py
# case: TestSupport_test_captured_stderr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_stderr() as stderr:
        print('hello', file=sys.stderr)
    self.assertEqual(stderr.getvalue(), 'hello\n')
