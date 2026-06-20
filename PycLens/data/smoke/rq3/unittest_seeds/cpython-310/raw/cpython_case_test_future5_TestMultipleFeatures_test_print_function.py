# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_future5.py
# case: TestMultipleFeatures_test_print_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with support.captured_output('stderr') as s:
        print('foo', file=sys.stderr)
    self.assertEqual(s.getvalue(), 'foo\n')
