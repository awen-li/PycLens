# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: CPythonOrderedDictTests_test_iterators_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    pairs = [('c', 1), ('b', 2), ('a', 3), ('d', 4), ('e', 5), ('f', 6)]
    od = OrderedDict(pairs)
    for method_name in ('keys', 'values', 'items'):
        meth = getattr(od, method_name)
        expected = list(meth())[1:]
        for i in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(method_name=method_name, protocol=i):
                it = iter(meth())
                next(it)
                p = pickle.dumps(it, i)
                unpickled = pickle.loads(p)
                self.assertEqual(list(unpickled), expected)
                self.assertEqual(list(it), expected)
