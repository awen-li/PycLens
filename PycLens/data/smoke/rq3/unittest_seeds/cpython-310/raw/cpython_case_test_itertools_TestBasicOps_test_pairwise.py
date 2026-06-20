# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_pairwise

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(list(pairwise('')), [])
    self.assertEqual(list(pairwise('a')), [])
    (self.assertEqual(list(pairwise('ab')), [('a', 'b')]),)
    self.assertEqual(list(pairwise('abcde')), [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')])
    self.assertEqual(list(pairwise(range(10000))), list(zip(range(10000), range(1, 10000))))
    with self.assertRaises(TypeError):
        pairwise()
    with self.assertRaises(TypeError):
        pairwise('abc', 10)
    with self.assertRaises(TypeError):
        pairwise(iterable='abc')
    with self.assertRaises(TypeError):
        pairwise(None)
