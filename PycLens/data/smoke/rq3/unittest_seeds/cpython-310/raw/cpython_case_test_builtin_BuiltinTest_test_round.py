# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_round

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(round(0.0), 0.0)
    self.assertEqual(type(round(0.0)), int)
    self.assertEqual(round(1.0), 1.0)
    self.assertEqual(round(10.0), 10.0)
    self.assertEqual(round(1000000000.0), 1000000000.0)
    self.assertEqual(round(1e+20), 1e+20)
    self.assertEqual(round(-1.0), -1.0)
    self.assertEqual(round(-10.0), -10.0)
    self.assertEqual(round(-1000000000.0), -1000000000.0)
    self.assertEqual(round(-1e+20), -1e+20)
    self.assertEqual(round(0.1), 0.0)
    self.assertEqual(round(1.1), 1.0)
    self.assertEqual(round(10.1), 10.0)
    self.assertEqual(round(1000000000.1), 1000000000.0)
    self.assertEqual(round(-1.1), -1.0)
    self.assertEqual(round(-10.1), -10.0)
    self.assertEqual(round(-1000000000.1), -1000000000.0)
    self.assertEqual(round(0.9), 1.0)
    self.assertEqual(round(9.9), 10.0)
    self.assertEqual(round(999999999.9), 1000000000.0)
    self.assertEqual(round(-0.9), -1.0)
    self.assertEqual(round(-9.9), -10.0)
    self.assertEqual(round(-999999999.9), -1000000000.0)
    self.assertEqual(round(-8.0, -1), -10.0)
    self.assertEqual(type(round(-8.0, -1)), float)
    self.assertEqual(type(round(-8.0, 0)), float)
    self.assertEqual(type(round(-8.0, 1)), float)
    self.assertEqual(round(5.5), 6)
    self.assertEqual(round(6.5), 6)
    self.assertEqual(round(-5.5), -6)
    self.assertEqual(round(-6.5), -6)
    self.assertEqual(round(0), 0)
    self.assertEqual(round(8), 8)
    self.assertEqual(round(-8), -8)
    self.assertEqual(type(round(0)), int)
    self.assertEqual(type(round(-8, -1)), int)
    self.assertEqual(type(round(-8, 0)), int)
    self.assertEqual(type(round(-8, 1)), int)
    self.assertEqual(round(number=-8.0, ndigits=-1), -10.0)
    self.assertRaises(TypeError, round)

    class TestRound:

        def __round__(self):
            return 23

    class TestNoRound:
        pass
    self.assertEqual(round(TestRound()), 23)
    self.assertRaises(TypeError, round, 1, 2, 3)
    self.assertRaises(TypeError, round, TestNoRound())
    t = TestNoRound()
    t.__round__ = lambda *args: args
    self.assertRaises(TypeError, round, t)
    self.assertRaises(TypeError, round, t, 0)
