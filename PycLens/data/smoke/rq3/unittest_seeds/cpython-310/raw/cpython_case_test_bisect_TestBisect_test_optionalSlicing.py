# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestBisect_test_optionalSlicing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (func, data, elem, expected) in self.precomputedCases:
        for lo in range(4):
            lo = min(len(data), lo)
            for hi in range(3, 8):
                hi = min(len(data), hi)
                ip = func(data, elem, lo, hi)
                self.assertTrue(lo <= ip <= hi)
                if func is self.module.bisect_left and ip < hi:
                    self.assertTrue(elem <= data[ip])
                if func is self.module.bisect_left and ip > lo:
                    self.assertTrue(data[ip - 1] < elem)
                if func is self.module.bisect_right and ip < hi:
                    self.assertTrue(elem < data[ip])
                if func is self.module.bisect_right and ip > lo:
                    self.assertTrue(data[ip - 1] <= elem)
                self.assertEqual(ip, max(lo, min(hi, expected)))
