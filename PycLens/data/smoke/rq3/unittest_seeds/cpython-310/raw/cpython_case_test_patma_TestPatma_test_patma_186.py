# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_patma.py
# case: TestPatma_test_patma_186

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Seq(collections.abc.Sequence):

        def __getitem__(self, i):
            return i

        def __len__(self):
            return 42
    match Seq():
        case [x, *_, y]:
            z = 0
    self.assertEqual(x, 0)
    self.assertEqual(y, 41)
    self.assertEqual(z, 0)
