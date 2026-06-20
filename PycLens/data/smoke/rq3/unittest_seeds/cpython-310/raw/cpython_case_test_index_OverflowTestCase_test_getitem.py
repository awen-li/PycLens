# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: OverflowTestCase_test_getitem

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class GetItem:

        def __len__(self):
            assert False, '__len__ should not be invoked'

        def __getitem__(self, key):
            return key
    x = GetItem()
    self.assertEqual(x[self.pos], self.pos)
    self.assertEqual(x[self.neg], self.neg)
    self.assertEqual(x[self.neg:self.pos].indices(maxsize), (0, maxsize, 1))
    self.assertEqual(x[self.neg:self.pos:1].indices(maxsize), (0, maxsize, 1))
