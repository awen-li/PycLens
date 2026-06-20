# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_map

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(map(lambda x: x * x, range(1, 4))), [1, 4, 9])
    try:
        from math import sqrt
    except ImportError:

        def sqrt(x):
            return pow(x, 0.5)
    self.assertEqual(list(map(lambda x: list(map(sqrt, x)), [[16, 4], [81, 9]])), [[4.0, 2.0], [9.0, 3.0]])
    self.assertEqual(list(map(lambda x, y: x + y, [1, 3, 2], [9, 1, 4])), [10, 4, 6])

    def plus(*v):
        accu = 0
        for i in v:
            accu = accu + i
        return accu
    self.assertEqual(list(map(plus, [1, 3, 7])), [1, 3, 7])
    self.assertEqual(list(map(plus, [1, 3, 7], [4, 9, 2])), [1 + 4, 3 + 9, 7 + 2])
    self.assertEqual(list(map(plus, [1, 3, 7], [4, 9, 2], [1, 1, 0])), [1 + 4 + 1, 3 + 9 + 1, 7 + 2 + 0])
    self.assertEqual(list(map(int, Squares(10))), [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def Max(a, b):
        if a is None:
            return b
        if b is None:
            return a
        return max(a, b)
    self.assertEqual(list(map(Max, Squares(3), Squares(2))), [0, 1])
    self.assertRaises(TypeError, map)
    self.assertRaises(TypeError, map, lambda x: x, 42)

    class BadSeq:

        def __iter__(self):
            raise ValueError
            yield None
    self.assertRaises(ValueError, list, map(lambda x: x, BadSeq()))

    def badfunc(x):
        raise RuntimeError
    self.assertRaises(RuntimeError, list, map(badfunc, range(5)))
