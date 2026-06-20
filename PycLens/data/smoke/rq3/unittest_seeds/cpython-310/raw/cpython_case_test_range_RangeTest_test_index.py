# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_index

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    u = range(2)
    self.assertEqual(u.index(0), 0)
    self.assertEqual(u.index(1), 1)
    self.assertRaises(ValueError, u.index, 2)
    u = range(-2, 3)
    self.assertEqual(u.count(0), 1)
    self.assertEqual(u.index(0), 2)
    self.assertRaises(TypeError, u.index)

    class BadExc(Exception):
        pass

    class BadCmp:

        def __eq__(self, other):
            if other == 2:
                raise BadExc()
            return False
    a = range(4)
    self.assertRaises(BadExc, a.index, BadCmp())
    a = range(-2, 3)
    self.assertEqual(a.index(0), 2)
    self.assertEqual(range(1, 10, 3).index(4), 1)
    self.assertEqual(range(1, -10, -3).index(-5), 2)
    self.assertEqual(range(10 ** 20).index(1), 1)
    self.assertEqual(range(10 ** 20).index(10 ** 20 - 1), 10 ** 20 - 1)
    self.assertRaises(ValueError, range(1, 2 ** 100, 2).index, 2 ** 87)
    self.assertEqual(range(1, 2 ** 100, 2).index(2 ** 87 + 1), 2 ** 86)
    self.assertEqual(range(10).index(ALWAYS_EQ), 0)
