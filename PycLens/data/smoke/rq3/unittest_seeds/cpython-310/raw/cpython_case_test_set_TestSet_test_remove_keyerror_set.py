# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestSet_test_remove_keyerror_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    key = self.thetype([3, 4])
    try:
        self.s.remove(key)
    except KeyError as e:
        self.assertTrue(e.args[0] is key, 'KeyError should be {0}, not {1}'.format(key, e.args[0]))
    else:
        self.fail()
