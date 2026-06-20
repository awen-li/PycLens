# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestQuantiles_test_specific_cases_inclusive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quantiles = statistics.quantiles
    data = [100, 200, 400, 800]
    random.shuffle(data)
    for (n, expected) in [(1, []), (2, [300.0]), (3, [200.0, 400.0]), (4, [175.0, 300.0, 500.0]), (5, [160.0, 240.0, 360.0, 560.0]), (6, [150.0, 200.0, 300.0, 400.0, 600.0]), (8, [137.5, 175, 225.0, 300.0, 375.0, 500.0, 650.0]), (10, [130.0, 160.0, 190.0, 240.0, 300.0, 360.0, 440.0, 560.0, 680.0]), (12, [125.0, 150.0, 175.0, 200.0, 250.0, 300.0, 350.0, 400.0, 500.0, 600.0, 700.0]), (15, [120.0, 140.0, 160.0, 180.0, 200.0, 240.0, 280.0, 320.0, 360.0, 400.0, 480.0, 560.0, 640.0, 720.0])]:
        self.assertEqual(expected, quantiles(data, n=n, method='inclusive'))
        self.assertEqual(len(quantiles(data, n=n, method='inclusive')), n - 1)
        for datatype in (float, Decimal, Fraction):
            result = quantiles(map(datatype, data), n=n, method='inclusive')
            self.assertTrue((all(type(x) == datatype) for x in result))
            self.assertEqual(result, list(map(datatype, expected)))

        def f(x):
            return 3.5 * x - 1234.675
        exp = list(map(f, expected))
        act = quantiles(map(f, data), n=n, method='inclusive')
        self.assertTrue(all((math.isclose(e, a) for (e, a) in zip(exp, act))))
    self.assertEqual(quantiles([0, 100], n=10, method='inclusive'), [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0])
    self.assertEqual(quantiles(range(0, 101), n=10, method='inclusive'), [10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 90.0])
    data = [random.randrange(10000) for i in range(501)]
    actual = quantiles(data, n=32, method='inclusive')
    data.remove(min(data))
    data.remove(max(data))
    expected = quantiles(data, n=32)
    self.assertEqual(expected, actual)
    for k in range(2, 60):
        data = random.choices(range(100), k=k)
        (q1, q2, q3) = quantiles(data, method='inclusive')
        self.assertEqual(q2, statistics.median(data))
