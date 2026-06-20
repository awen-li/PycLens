# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_sample

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 100
    population = range(N)
    for k in range(N + 1):
        s = self.gen.sample(population, k)
        self.assertEqual(len(s), k)
        uniq = set(s)
        self.assertEqual(len(uniq), k)
        self.assertTrue(uniq <= set(population))
    self.assertEqual(self.gen.sample([], 0), [])
    self.assertRaises(ValueError, self.gen.sample, population, N + 1)
    self.assertRaises(ValueError, self.gen.sample, [], -1)
