# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestWeirdBugs_test_8420_set_merge

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global be_bad, set2, dict2
    be_bad = False
    set1 = {bad_eq()}
    set2 = {bad_eq() for i in range(75)}
    be_bad = True
    self.assertRaises(ZeroDivisionError, set1.update, set2)
    be_bad = False
    set1 = {bad_dict_clear()}
    dict2 = {bad_dict_clear(): None}
    be_bad = True
    set1.symmetric_difference_update(dict2)
