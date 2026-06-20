# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_reverseitemiterator_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        data = {1: 'a', 2: 'b', 3: 'c'}
        itorg = reversed(data.items())
        d = pickle.dumps(itorg, proto)
        it = pickle.loads(d)
        self.assertIsInstance(it, collections.abc.Iterator)
        self.assertEqual(dict(it), data)
        it = pickle.loads(d)
        drop = next(it)
        d = pickle.dumps(it, proto)
        it = pickle.loads(d)
        del data[drop[0]]
        self.assertEqual(dict(it), data)
