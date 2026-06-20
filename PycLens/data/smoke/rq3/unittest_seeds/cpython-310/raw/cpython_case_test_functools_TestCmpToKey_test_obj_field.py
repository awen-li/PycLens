# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCmpToKey_test_obj_field

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def cmp1(x, y):
        return (x > y) - (x < y)
    key = self.cmp_to_key(mycmp=cmp1)
    self.assertEqual(key(50).obj, 50)
