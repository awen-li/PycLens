# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(filter(lambda c: 'a' <= c <= 'z', 'Hello World')), list('elloorld'))
    self.assertEqual(list(filter(None, [1, 'hello', [], [3], '', None, 9, 0])), [1, 'hello', [3], 9])
    self.assertEqual(list(filter(lambda x: x > 0, [1, -3, 9, 0, 2])), [1, 9, 2])
    self.assertEqual(list(filter(None, Squares(10))), [1, 4, 9, 16, 25, 36, 49, 64, 81])
    self.assertEqual(list(filter(lambda x: x % 2, Squares(10))), [1, 9, 25, 49, 81])

    def identity(item):
        return 1
    filter(identity, Squares(5))
    self.assertRaises(TypeError, filter)

    class BadSeq(object):

        def __getitem__(self, index):
            if index < 4:
                return 42
            raise ValueError
    self.assertRaises(ValueError, list, filter(lambda x: x, BadSeq()))

    def badfunc():
        pass
    self.assertRaises(TypeError, list, filter(badfunc, range(5)))
    self.assertEqual(list(filter(None, (1, 2))), [1, 2])
    self.assertEqual(list(filter(lambda x: x >= 3, (1, 2, 3, 4))), [3, 4])
    self.assertRaises(TypeError, list, filter(42, (1, 2)))
