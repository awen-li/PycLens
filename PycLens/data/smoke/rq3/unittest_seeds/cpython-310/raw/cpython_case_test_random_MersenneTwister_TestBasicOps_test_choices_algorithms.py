# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_choices_algorithms

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    choices = self.gen.choices
    n = 104729
    self.gen.seed(8675309)
    a = self.gen.choices(range(n), k=10000)
    self.gen.seed(8675309)
    b = self.gen.choices(range(n), [1] * n, k=10000)
    self.assertEqual(a, b)
    self.gen.seed(8675309)
    c = self.gen.choices(range(n), cum_weights=range(1, n + 1), k=10000)
    self.assertEqual(a, c)
    population = ['Red', 'Black', 'Green']
    weights = [18, 18, 2]
    cum_weights = [18, 36, 38]
    expanded_population = ['Red'] * 18 + ['Black'] * 18 + ['Green'] * 2
    self.gen.seed(9035768)
    a = self.gen.choices(expanded_population, k=10000)
    self.gen.seed(9035768)
    b = self.gen.choices(population, weights, k=10000)
    self.assertEqual(a, b)
    self.gen.seed(9035768)
    c = self.gen.choices(population, cum_weights=cum_weights, k=10000)
    self.assertEqual(a, c)
