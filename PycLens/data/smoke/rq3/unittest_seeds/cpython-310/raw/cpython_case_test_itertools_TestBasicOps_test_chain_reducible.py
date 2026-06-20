# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_chain_reducible

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for oper in [copy.deepcopy] + picklecopiers:
        it = chain('abc', 'def')
        self.assertEqual(list(oper(it)), list('abcdef'))
        self.assertEqual(next(it), 'a')
        self.assertEqual(list(oper(it)), list('bcdef'))
        self.assertEqual(list(oper(chain(''))), [])
        self.assertEqual(take(4, oper(chain('abc', 'def'))), list('abcd'))
        self.assertRaises(TypeError, list, oper(chain(2, 3)))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, chain('abc', 'def'), compare=list('abcdef'))
