# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestExamples_test_accumulate_reducible_none

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    it = accumulate([None, None, None], operator.is_)
    self.assertEqual(next(it), None)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        it_copy = pickle.loads(pickle.dumps(it, proto))
        self.assertEqual(list(it_copy), [True, False])
    self.assertEqual(list(copy.deepcopy(it)), [True, False])
    self.assertEqual(list(copy.copy(it)), [True, False])
