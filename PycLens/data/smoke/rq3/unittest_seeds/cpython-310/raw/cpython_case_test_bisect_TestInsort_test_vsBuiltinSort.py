# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bisect.py
# case: TestInsort_test_vsBuiltinSort

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from random import choice
    for insorted in (list(), UserList()):
        for i in range(n):
            digit = choice('0123456789')
            if digit in '02468':
                f = self.module.insort_left
            else:
                f = self.module.insort_right
            f(insorted, digit)
        self.assertEqual(sorted(insorted), insorted)
