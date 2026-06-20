# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_sample_on_seqsets

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class SeqSet(abc.Sequence, abc.Set):

        def __init__(self, items):
            self._items = items

        def __len__(self):
            return len(self._items)

        def __getitem__(self, index):
            return self._items[index]
    population = SeqSet([2, 4, 1, 3])
    with warnings.catch_warnings():
        warnings.simplefilter('error', DeprecationWarning)
        self.gen.sample(population, k=2)
