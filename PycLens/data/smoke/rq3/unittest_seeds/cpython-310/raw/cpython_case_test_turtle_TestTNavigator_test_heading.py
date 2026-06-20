# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_turtle.py
# case: TestTNavigator_test_heading

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.nav.left(90)
    self.assertAlmostEqual(self.nav.heading(), 90)
    self.nav.left(45)
    self.assertAlmostEqual(self.nav.heading(), 135)
    self.nav.right(1.6)
    self.assertAlmostEqual(self.nav.heading(), 133.4)
    self.assertRaises(TypeError, self.nav.right, 'sdkfjdsf')
    self.nav.reset()
    rotations = [10, 20, 170, 300]
    result = sum(rotations) % 360
    for num in rotations:
        self.nav.left(num)
    self.assertEqual(self.nav.heading(), result)
    self.nav.reset()
    result = (360 - sum(rotations)) % 360
    for num in rotations:
        self.nav.right(num)
    self.assertEqual(self.nav.heading(), result)
    self.nav.reset()
    rotations = [10, 20, -170, 300, -210, 34.3, -50.2, -10, -29.98, 500]
    sum_so_far = 0
    for num in rotations:
        if num < 0:
            self.nav.right(abs(num))
        else:
            self.nav.left(num)
        sum_so_far += num
        self.assertAlmostEqual(self.nav.heading(), sum_so_far % 360)
