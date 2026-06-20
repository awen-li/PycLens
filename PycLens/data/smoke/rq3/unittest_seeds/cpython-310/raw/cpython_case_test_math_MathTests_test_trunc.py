# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_trunc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(math.trunc(1), 1)
    self.assertEqual(math.trunc(-1), -1)
    self.assertEqual(type(math.trunc(1)), int)
    self.assertEqual(type(math.trunc(1.5)), int)
    self.assertEqual(math.trunc(1.5), 1)
    self.assertEqual(math.trunc(-1.5), -1)
    self.assertEqual(math.trunc(1.999999), 1)
    self.assertEqual(math.trunc(-1.999999), -1)
    self.assertEqual(math.trunc(-0.999999), -0)
    self.assertEqual(math.trunc(-100.999), -100)

    class TestTrunc:

        def __trunc__(self):
            return 23

    class FloatTrunc(float):

        def __trunc__(self):
            return 23

    class TestNoTrunc:
        pass
    self.assertEqual(math.trunc(TestTrunc()), 23)
    self.assertEqual(math.trunc(FloatTrunc()), 23)
    self.assertRaises(TypeError, math.trunc)
    self.assertRaises(TypeError, math.trunc, 1, 2)
    self.assertRaises(TypeError, math.trunc, FloatLike(23.5))
    self.assertRaises(TypeError, math.trunc, TestNoTrunc())
