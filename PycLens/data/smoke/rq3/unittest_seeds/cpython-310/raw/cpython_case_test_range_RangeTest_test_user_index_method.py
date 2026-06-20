# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_range.py
# case: RangeTest_test_user_index_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bignum = 2 * sys.maxsize
    smallnum = 42

    class I:

        def __init__(self, n):
            self.n = int(n)

        def __index__(self):
            return self.n
    self.assertEqual(list(range(I(bignum), I(bignum + 1))), [bignum])
    self.assertEqual(list(range(I(smallnum), I(smallnum + 1))), [smallnum])

    class IX:

        def __index__(self):
            raise RuntimeError
    self.assertRaises(RuntimeError, range, IX())

    class IN:

        def __index__(self):
            return 'not a number'
    self.assertRaises(TypeError, range, IN())
    self.assertEqual(range(10)[:I(5)], range(5))
    with self.assertRaises(RuntimeError):
        range(0, 10)[:IX()]
    with self.assertRaises(TypeError):
        range(0, 10)[:IN()]
