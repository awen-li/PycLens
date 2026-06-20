# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_setstate_middle_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start_state = self.gen.getstate()
    self.assertRaises(TypeError, self.gen.setstate, (2, None, None))
    self.assertRaises(ValueError, self.gen.setstate, (2, (1, 2, 3), None))
    self.assertRaises(TypeError, self.gen.setstate, (2, ('a',) * 625, None))
    self.assertRaises(TypeError, self.gen.setstate, (2, (0,) * 624 + ('a',), None))
    with self.assertRaises((ValueError, OverflowError)):
        self.gen.setstate((2, (1,) * 624 + (625,), None))
    with self.assertRaises((ValueError, OverflowError)):
        self.gen.setstate((2, (1,) * 624 + (-1,), None))
    bits100 = self.gen.getrandbits(100)
    self.gen.setstate(start_state)
    self.assertEqual(self.gen.getrandbits(100), bits100)
    state_values = self.gen.getstate()[1]
    state_values = list(state_values)
    state_values[-1] = float('nan')
    state = (int(x) for x in state_values)
    self.assertRaises(TypeError, self.gen.setstate, (2, state, None))
