# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_memoize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    counts = {}

    @memoize
    @countcalls(counts)
    def double(x):
        return x * 2
    self.assertEqual(double.__name__, 'double')
    self.assertEqual(counts, dict(double=0))
    self.assertEqual(double(2), 4)
    self.assertEqual(counts['double'], 1)
    self.assertEqual(double(2), 4)
    self.assertEqual(counts['double'], 1)
    self.assertEqual(double(3), 6)
    self.assertEqual(counts['double'], 2)
    self.assertEqual(double([10]), [10, 10])
    self.assertEqual(counts['double'], 3)
    self.assertEqual(double([10]), [10, 10])
    self.assertEqual(counts['double'], 4)
