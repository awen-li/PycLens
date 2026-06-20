# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestReduce_test_reduce

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Squares:

        def __init__(self, max):
            self.max = max
            self.sofar = []

        def __len__(self):
            return len(self.sofar)

        def __getitem__(self, i):
            if not 0 <= i < self.max:
                raise IndexError
            n = len(self.sofar)
            while n <= i:
                self.sofar.append(n * n)
                n += 1
            return self.sofar[i]

    def add(x, y):
        return x + y
    self.assertEqual(self.reduce(add, ['a', 'b', 'c'], ''), 'abc')
    self.assertEqual(self.reduce(add, [['a', 'c'], [], ['d', 'w']], []), ['a', 'c', 'd', 'w'])
    self.assertEqual(self.reduce(lambda x, y: x * y, range(2, 8), 1), 5040)
    self.assertEqual(self.reduce(lambda x, y: x * y, range(2, 21), 1), 2432902008176640000)
    self.assertEqual(self.reduce(add, Squares(10)), 285)
    self.assertEqual(self.reduce(add, Squares(10), 0), 285)
    self.assertEqual(self.reduce(add, Squares(0), 0), 0)
    self.assertRaises(TypeError, self.reduce)
    self.assertRaises(TypeError, self.reduce, 42, 42)
    self.assertRaises(TypeError, self.reduce, 42, 42, 42)
    self.assertEqual(self.reduce(42, '1'), '1')
    self.assertEqual(self.reduce(42, '', '1'), '1')
    self.assertRaises(TypeError, self.reduce, 42, (42, 42))
    self.assertRaises(TypeError, self.reduce, add, [])
    self.assertRaises(TypeError, self.reduce, add, '')
    self.assertRaises(TypeError, self.reduce, add, ())
    self.assertRaises(TypeError, self.reduce, add, object())

    class TestFailingIter:

        def __iter__(self):
            raise RuntimeError
    self.assertRaises(RuntimeError, self.reduce, add, TestFailingIter())
    self.assertEqual(self.reduce(add, [], None), None)
    self.assertEqual(self.reduce(add, [], 42), 42)

    class BadSeq:

        def __getitem__(self, index):
            raise ValueError
    self.assertRaises(ValueError, self.reduce, 42, BadSeq())
