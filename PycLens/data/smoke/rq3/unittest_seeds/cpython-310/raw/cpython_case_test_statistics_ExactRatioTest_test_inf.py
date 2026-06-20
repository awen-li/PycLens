# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: ExactRatioTest_test_inf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    INF = float('INF')

    class MyFloat(float):
        pass

    class MyDecimal(Decimal):
        pass
    for inf in (INF, -INF):
        for type_ in (float, MyFloat, Decimal, MyDecimal):
            x = type_(inf)
            ratio = statistics._exact_ratio(x)
            self.assertEqual(ratio, (x, None))
            self.assertEqual(type(ratio[0]), type_)
            self.assertTrue(math.isinf(ratio[0]))
