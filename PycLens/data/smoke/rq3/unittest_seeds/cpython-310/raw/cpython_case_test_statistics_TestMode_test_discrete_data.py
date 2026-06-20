# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMode_test_discrete_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = list(range(10))
    for i in range(10):
        d = data + [i]
        random.shuffle(d)
        self.assertEqual(self.func(d), i)
