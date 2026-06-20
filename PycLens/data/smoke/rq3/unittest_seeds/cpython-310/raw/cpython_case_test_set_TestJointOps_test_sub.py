# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_sub

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = self.s.difference(self.otherword)
    self.assertEqual(self.s - set(self.otherword), i)
    self.assertEqual(self.s - frozenset(self.otherword), i)
    try:
        self.s - self.otherword
    except TypeError:
        pass
    else:
        self.fail('s-t did not screen-out general iterables')
