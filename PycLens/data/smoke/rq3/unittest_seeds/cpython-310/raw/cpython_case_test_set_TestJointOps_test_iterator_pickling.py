# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_set.py
# case: TestJointOps_test_iterator_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        itorg = iter(self.s)
        data = self.thetype(self.s)
        d = pickle.dumps(itorg, proto)
        it = pickle.loads(d)
        self.assertIsInstance(it, collections.abc.Iterator)
        self.assertEqual(self.thetype(it), data)
        it = pickle.loads(d)
        try:
            drop = next(it)
        except StopIteration:
            continue
        d = pickle.dumps(it, proto)
        it = pickle.loads(d)
        self.assertEqual(self.thetype(it), data - self.thetype((drop,)))
