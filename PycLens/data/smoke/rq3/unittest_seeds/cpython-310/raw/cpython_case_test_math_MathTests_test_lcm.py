# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_math.py
# case: MathTests_test_lcm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lcm = math.lcm
    self.assertEqual(lcm(0, 0), 0)
    self.assertEqual(lcm(1, 0), 0)
    self.assertEqual(lcm(-1, 0), 0)
    self.assertEqual(lcm(0, 1), 0)
    self.assertEqual(lcm(0, -1), 0)
    self.assertEqual(lcm(7, 1), 7)
    self.assertEqual(lcm(7, -1), 7)
    self.assertEqual(lcm(-23, 15), 345)
    self.assertEqual(lcm(120, 84), 840)
    self.assertEqual(lcm(84, -120), 840)
    self.assertEqual(lcm(1216342683557601535506311712, 436522681849110124616458784), 16592536571065866494401400422922201534178938447014944)
    x = 43461045657039990237
    y = 10645022458251153277
    for c in (652560, 57655923087165495981):
        a = x * c
        b = y * c
        d = x * y * c
        self.assertEqual(lcm(a, b), d)
        self.assertEqual(lcm(b, a), d)
        self.assertEqual(lcm(-a, b), d)
        self.assertEqual(lcm(b, -a), d)
        self.assertEqual(lcm(a, -b), d)
        self.assertEqual(lcm(-b, a), d)
        self.assertEqual(lcm(-a, -b), d)
        self.assertEqual(lcm(-b, -a), d)
    self.assertEqual(lcm(), 1)
    self.assertEqual(lcm(120), 120)
    self.assertEqual(lcm(-120), 120)
    self.assertEqual(lcm(120, 84, 102), 14280)
    self.assertEqual(lcm(120, 0, 84), 0)
    self.assertRaises(TypeError, lcm, 120.0)
    self.assertRaises(TypeError, lcm, 120.0, 84)
    self.assertRaises(TypeError, lcm, 120, 84.0)
    self.assertRaises(TypeError, lcm, 120, 0, 84.0)
    self.assertEqual(lcm(MyIndexable(120), MyIndexable(84)), 840)
