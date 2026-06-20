# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestVariousIteratorArgs_test_iter_with_altered_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = deque('abcdefg')
    it = iter(d)
    d.pop()
    self.assertRaises(RuntimeError, next, it)
