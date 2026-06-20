# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_cycle_copy_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    c = cycle('abc')
    self.assertEqual(next(c), 'a')
    self.assertEqual(take(10, copy.deepcopy(c)), list('bcabcabcab'))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.assertEqual(take(10, pickle.loads(pickle.dumps(c, proto))), list('bcabcabcab'))
        next(c)
        self.assertEqual(take(10, pickle.loads(pickle.dumps(c, proto))), list('cabcabcabc'))
        next(c)
        next(c)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, cycle('abc'))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        it = iter('abcde')
        c = cycle(it)
        _ = [next(c) for i in range(2)]
        p = pickle.dumps(c, proto)
        d = pickle.loads(p)
        self.assertEqual(take(20, d), list('cdeabcdeabcdeabcdeab'))
        it = iter('abcde')
        c = cycle(it)
        _ = [next(c) for i in range(7)]
        p = pickle.dumps(c, proto)
        d = pickle.loads(p)
        self.assertEqual(take(20, d), list('cdeabcdeabcdeabcdeab'))
