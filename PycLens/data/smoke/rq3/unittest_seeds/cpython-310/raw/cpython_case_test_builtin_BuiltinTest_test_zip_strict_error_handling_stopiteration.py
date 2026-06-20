# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_zip_strict_error_handling_stopiteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Iter:

        def __init__(self, size):
            self.size = size

        def __iter__(self):
            return self

        def __next__(self):
            self.size -= 1
            if self.size < 0:
                raise StopIteration
            return self.size
    l1 = self.iter_error(zip('AB', Iter(1), strict=True), ValueError)
    self.assertEqual(l1, [('A', 0)])
    l2 = self.iter_error(zip('AB', Iter(2), 'A', strict=True), ValueError)
    self.assertEqual(l2, [('A', 1, 'A')])
    l3 = self.iter_error(zip('AB', Iter(2), 'ABC', strict=True), ValueError)
    self.assertEqual(l3, [('A', 1, 'A'), ('B', 0, 'B')])
    l4 = self.iter_error(zip('AB', Iter(3), strict=True), ValueError)
    self.assertEqual(l4, [('A', 2), ('B', 1)])
    l5 = self.iter_error(zip(Iter(1), 'AB', strict=True), ValueError)
    self.assertEqual(l5, [(0, 'A')])
    l6 = self.iter_error(zip(Iter(2), 'A', strict=True), ValueError)
    self.assertEqual(l6, [(1, 'A')])
    l7 = self.iter_error(zip(Iter(2), 'ABC', strict=True), ValueError)
    self.assertEqual(l7, [(1, 'A'), (0, 'B')])
    l8 = self.iter_error(zip(Iter(3), 'AB', strict=True), ValueError)
    self.assertEqual(l8, [(2, 'A'), (1, 'B')])
