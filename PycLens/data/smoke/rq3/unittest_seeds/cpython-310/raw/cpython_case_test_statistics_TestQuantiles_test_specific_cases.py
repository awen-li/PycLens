# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestQuantiles_test_specific_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    quantiles = statistics.quantiles
    data = [120, 200, 250, 320, 350]
    random.shuffle(data)
    for (n, expected) in [(1, []), (2, [250.0]), (3, [200.0, 320.0]), (4, [160.0, 250.0, 335.0]), (5, [136.0, 220.0, 292.0, 344.0]), (6, [120.0, 200.0, 250.0, 320.0, 350.0]), (8, [100.0, 160.0, 212.5, 250.0, 302.5, 335.0, 357.5]), (10, [88.0, 136.0, 184.0, 220.0, 250.0, 292.0, 326.0, 344.0, 362.0]), (12, [80.0, 120.0, 160.0, 200.0, 225.0, 250.0, 285.0, 320.0, 335.0, 350.0, 365.0]), (15, [72.0, 104.0, 136.0, 168.0, 200.0, 220.0, 240.0, 264.0, 292.0, 320.0, 332.0, 344.0, 356.0, 368.0])]:
        self.assertEqual(expected, quantiles(data, n=n))
        self.assertEqual(len(quantiles(data, n=n)), n - 1)
        for datatype in (float, Decimal, Fraction):
            result = quantiles(map(datatype, data), n=n)
            self.assertTrue((all(type(x) == datatype) for x in result))
            self.assertEqual(result, list(map(datatype, expected)))
        if len(expected) >= 2:
            self.assertEqual(quantiles(expected, n=n), expected)
        sdata = sorted(data)
        lo = 2 * sdata[0] - sdata[1]
        hi = 2 * sdata[-1] - sdata[-2]
        padded_data = data + [lo, hi]
        self.assertEqual(quantiles(data, n=n), quantiles(padded_data, n=n, method='inclusive'), (n, data))

        def f(x):
            return 3.5 * x - 1234.675
        exp = list(map(f, expected))
        act = quantiles(map(f, data), n=n)
        self.assertTrue(all((math.isclose(e, a) for (e, a) in zip(exp, act))))
    for k in range(2, 60):
        data = random.choices(range(100), k=k)
        (q1, q2, q3) = quantiles(data)
        self.assertEqual(q2, statistics.median(data))
