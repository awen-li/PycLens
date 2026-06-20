# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_sub_and_super

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (p, q, r) = map(self.thetype, ['ab', 'abcde', 'def'])
    self.assertTrue(p < q)
    self.assertTrue(p <= q)
    self.assertTrue(q <= q)
    self.assertTrue(q > p)
    self.assertTrue(q >= p)
    self.assertFalse(q < r)
    self.assertFalse(q <= r)
    self.assertFalse(q > r)
    self.assertFalse(q >= r)
    self.assertTrue(set('a').issubset('abc'))
    self.assertTrue(set('abc').issuperset('a'))
    self.assertFalse(set('a').issubset('cbs'))
    self.assertFalse(set('cbs').issuperset('a'))
