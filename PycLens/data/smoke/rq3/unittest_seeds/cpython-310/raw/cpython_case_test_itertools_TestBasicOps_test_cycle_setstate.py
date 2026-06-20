# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_cycle_setstate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = cycle('defg')
    c.__setstate__((list('abc'), 0))
    self.assertEqual(take(20, c), list('defgabcdefgabcdefgab'))
    c = cycle('defg')
    c.__setstate__((list('abcdefg'), 1))
    self.assertEqual(take(20, c), list('defgabcdefgabcdefgab'))
    with self.assertRaises(TypeError):
        cycle('defg').__setstate__([list('abcdefg'), 0])
    with self.assertRaises(TypeError):
        c = cycle('defg')
        c.__setstate__((tuple('defg'), 0))
    take(20, c)
    with self.assertRaises(TypeError):
        cycle('defg').__setstate__((list('abcdefg'), 'x'))
    self.assertRaises(TypeError, cycle('').__setstate__, ())
    self.assertRaises(TypeError, cycle('').__setstate__, ([],))
