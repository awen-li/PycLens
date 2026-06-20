# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_remove_keyerror_unpacking

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for v1 in ['Q', (1,)]:
        try:
            self.s.remove(v1)
        except KeyError as e:
            v2 = e.args[0]
            self.assertEqual(v1, v2)
        else:
            self.fail()
