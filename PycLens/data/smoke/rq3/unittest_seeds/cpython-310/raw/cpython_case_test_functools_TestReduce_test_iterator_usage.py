# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestReduce_test_iterator_usage

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SequenceClass:

        def __init__(self, n):
            self.n = n

        def __getitem__(self, i):
            if 0 <= i < self.n:
                return i
            else:
                raise IndexError
    from operator import add
    self.assertEqual(self.reduce(add, SequenceClass(5)), 10)
    self.assertEqual(self.reduce(add, SequenceClass(5), 42), 52)
    self.assertRaises(TypeError, self.reduce, add, SequenceClass(0))
    self.assertEqual(self.reduce(add, SequenceClass(0), 42), 42)
    self.assertEqual(self.reduce(add, SequenceClass(1)), 0)
    self.assertEqual(self.reduce(add, SequenceClass(1), 42), 42)
    d = {'one': 1, 'two': 2, 'three': 3}
    self.assertEqual(self.reduce(add, d), ''.join(d.keys()))
