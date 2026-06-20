# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_slices

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('hello'[:4], 'hell')
    self.assertEqual('hello'[slice(4)], 'hell')
    self.assertEqual(str.__getitem__('hello', slice(4)), 'hell')

    class S(str):

        def __getitem__(self, x):
            return str.__getitem__(self, x)
    self.assertEqual(S('hello')[:4], 'hell')
    self.assertEqual(S('hello')[slice(4)], 'hell')
    self.assertEqual(S('hello').__getitem__(slice(4)), 'hell')
    self.assertEqual((1, 2, 3)[:2], (1, 2))
    self.assertEqual((1, 2, 3)[slice(2)], (1, 2))
    self.assertEqual(tuple.__getitem__((1, 2, 3), slice(2)), (1, 2))

    class T(tuple):

        def __getitem__(self, x):
            return tuple.__getitem__(self, x)
    self.assertEqual(T((1, 2, 3))[:2], (1, 2))
    self.assertEqual(T((1, 2, 3))[slice(2)], (1, 2))
    self.assertEqual(T((1, 2, 3)).__getitem__(slice(2)), (1, 2))
    self.assertEqual([1, 2, 3][:2], [1, 2])
    self.assertEqual([1, 2, 3][slice(2)], [1, 2])
    self.assertEqual(list.__getitem__([1, 2, 3], slice(2)), [1, 2])

    class L(list):

        def __getitem__(self, x):
            return list.__getitem__(self, x)
    self.assertEqual(L([1, 2, 3])[:2], [1, 2])
    self.assertEqual(L([1, 2, 3])[slice(2)], [1, 2])
    self.assertEqual(L([1, 2, 3]).__getitem__(slice(2)), [1, 2])
    a = L([1, 2, 3])
    a[slice(1, 3)] = [3, 2]
    self.assertEqual(a, [1, 3, 2])
    a[slice(0, 2, 1)] = [3, 1]
    self.assertEqual(a, [3, 1, 2])
    a.__setitem__(slice(1, 3), [2, 1])
    self.assertEqual(a, [3, 2, 1])
    a.__setitem__(slice(0, 2, 1), [2, 3])
    self.assertEqual(a, [2, 3, 1])
