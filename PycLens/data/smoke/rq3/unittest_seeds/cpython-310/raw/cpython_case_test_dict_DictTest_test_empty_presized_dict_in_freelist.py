# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_empty_presized_dict_in_freelist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ZeroDivisionError):
        d = {'a': 1 // 0, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None, 'g': None, 'h': None}
    d = {}
