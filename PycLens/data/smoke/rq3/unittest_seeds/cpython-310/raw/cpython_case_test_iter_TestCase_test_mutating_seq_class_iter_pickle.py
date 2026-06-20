# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_mutating_seq_class_iter_pickle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    orig = SequenceClass(5)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorig = iter(orig)
        d = pickle.dumps((itorig, orig), proto)
        (it, seq) = pickle.loads(d)
        seq.n = 7
        self.assertIs(type(it), type(itorig))
        self.assertEqual(list(it), list(range(7)))
        next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, seq) = pickle.loads(d)
        seq.n = 7
        self.assertIs(type(it), type(itorig))
        self.assertEqual(list(it), list(range(1, 7)))
        for i in range(1, 5):
            next(itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, seq) = pickle.loads(d)
        seq.n = 7
        self.assertIs(type(it), type(itorig))
        self.assertEqual(list(it), list(range(5, 7)))
        self.assertRaises(StopIteration, next, itorig)
        d = pickle.dumps((itorig, orig), proto)
        (it, seq) = pickle.loads(d)
        seq.n = 7
        self.assertTrue(isinstance(it, collections.abc.Iterator))
        self.assertEqual(list(it), [])
