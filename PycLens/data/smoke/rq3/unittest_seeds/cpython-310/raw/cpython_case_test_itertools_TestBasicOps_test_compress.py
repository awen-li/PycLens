# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_compress

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(compress(data='ABCDEF', selectors=[1, 0, 1, 0, 1, 1])), list('ACEF'))
    self.assertEqual(list(compress('ABCDEF', [1, 0, 1, 0, 1, 1])), list('ACEF'))
    self.assertEqual(list(compress('ABCDEF', [0, 0, 0, 0, 0, 0])), list(''))
    self.assertEqual(list(compress('ABCDEF', [1, 1, 1, 1, 1, 1])), list('ABCDEF'))
    self.assertEqual(list(compress('ABCDEF', [1, 0, 1])), list('AC'))
    self.assertEqual(list(compress('ABC', [0, 1, 1, 1, 1, 1])), list('BC'))
    n = 10000
    data = chain.from_iterable(repeat(range(6), n))
    selectors = chain.from_iterable(repeat((0, 1)))
    self.assertEqual(list(compress(data, selectors)), [1, 3, 5] * n)
    self.assertRaises(TypeError, compress, None, range(6))
    self.assertRaises(TypeError, compress, range(6), None)
    self.assertRaises(TypeError, compress, range(6))
    self.assertRaises(TypeError, compress, range(6), None)
    for op in [lambda a: copy.copy(a), lambda a: copy.deepcopy(a)] + picklecopiers:
        for (data, selectors, result1, result2) in [('ABCDEF', [1, 0, 1, 0, 1, 1], 'ACEF', 'CEF'), ('ABCDEF', [0, 0, 0, 0, 0, 0], '', ''), ('ABCDEF', [1, 1, 1, 1, 1, 1], 'ABCDEF', 'BCDEF'), ('ABCDEF', [1, 0, 1], 'AC', 'C'), ('ABC', [0, 1, 1, 1, 1, 1], 'BC', 'C')]:
            self.assertEqual(list(op(compress(data=data, selectors=selectors))), list(result1))
            self.assertEqual(list(op(compress(data, selectors))), list(result1))
            testIntermediate = compress(data, selectors)
            if result1:
                next(testIntermediate)
                self.assertEqual(list(op(testIntermediate)), list(result2))
