# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCollectionABCs_test_issue26915

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class CustomSequence(Sequence):

        def __init__(self, seq):
            self._seq = seq

        def __getitem__(self, index):
            return self._seq[index]

        def __len__(self):
            return len(self._seq)
    nan = float('nan')
    obj = support.NEVER_EQ
    seq = CustomSequence([nan, obj, nan])
    containers = [seq, ItemsView({1: nan, 2: obj}), KeysView({1: nan, 2: obj}), ValuesView({1: nan, 2: obj})]
    for container in containers:
        for elem in container:
            self.assertIn(elem, container)
    self.assertEqual(seq.index(nan), 0)
    self.assertEqual(seq.index(obj), 1)
    self.assertEqual(seq.count(nan), 2)
    self.assertEqual(seq.count(obj), 1)
