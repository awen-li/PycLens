# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_sample_counts_equivalence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = self.gen.sample
    seed = self.gen.seed
    colors = ['red', 'green', 'blue', 'orange', 'black', 'amber']
    counts = [500, 200, 20, 10, 5, 1]
    k = 700
    seed(8675309)
    s1 = sample(colors, counts=counts, k=k)
    seed(8675309)
    expanded = [color for (color, count) in zip(colors, counts) for i in range(count)]
    self.assertEqual(len(expanded), sum(counts))
    s2 = sample(expanded, k=k)
    self.assertEqual(s1, s2)
    pop = 'abcdefghi'
    counts = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    seed(8675309)
    s1 = ''.join(sample(pop, counts=counts, k=30))
    expanded = ''.join([letter for (letter, count) in zip(pop, counts) for i in range(count)])
    seed(8675309)
    s2 = ''.join(sample(expanded, k=30))
    self.assertEqual(s1, s2)
