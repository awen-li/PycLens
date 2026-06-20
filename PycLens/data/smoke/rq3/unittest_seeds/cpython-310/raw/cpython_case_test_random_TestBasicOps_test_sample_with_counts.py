# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestBasicOps_test_sample_with_counts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = self.gen.sample
    colors = ['red', 'green', 'blue', 'orange', 'black', 'brown', 'amber']
    counts = [500, 200, 20, 10, 5, 0, 1]
    k = 700
    summary = Counter(sample(colors, counts=counts, k=k))
    self.assertEqual(sum(summary.values()), k)
    for (color, weight) in zip(colors, counts):
        self.assertLessEqual(summary[color], weight)
    self.assertNotIn('brown', summary)
    k = sum(counts)
    summary = Counter(sample(colors, counts=counts, k=k))
    self.assertEqual(sum(summary.values()), k)
    for (color, weight) in zip(colors, counts):
        self.assertLessEqual(summary[color], weight)
    self.assertNotIn('brown', summary)
    summary = Counter(sample(['x'], counts=[10], k=8))
    self.assertEqual(summary, Counter(x=8))
    nc = len(colors)
    summary = Counter(sample(colors, counts=[10] * nc, k=10 * nc))
    self.assertEqual(summary, Counter(10 * colors))
    with self.assertRaises(TypeError):
        sample(['red', 'green', 'blue'], counts=10, k=10)
    with self.assertRaises(ValueError):
        sample(['red', 'green', 'blue'], counts=[-3, -7, -8], k=2)
    with self.assertRaises(ValueError):
        sample(['red', 'green', 'blue'], counts=[0, 0, 0], k=2)
    with self.assertRaises(ValueError):
        sample(['red', 'green'], counts=[10, 10], k=21)
    with self.assertRaises(ValueError):
        sample(['red', 'green', 'blue'], counts=[1, 2], k=2)
    with self.assertRaises(ValueError):
        sample(['red', 'green', 'blue'], counts=[1, 2, 3, 4], k=2)
