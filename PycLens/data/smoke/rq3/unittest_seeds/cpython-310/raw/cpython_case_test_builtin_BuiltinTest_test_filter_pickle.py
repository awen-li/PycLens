# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_filter_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        f1 = filter(filter_char, 'abcdeabcde')
        f2 = filter(filter_char, 'abcdeabcde')
        self.check_iter_pickle(f1, list(f2), proto)
