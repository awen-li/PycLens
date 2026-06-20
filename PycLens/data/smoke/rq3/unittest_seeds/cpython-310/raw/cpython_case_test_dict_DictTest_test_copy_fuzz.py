# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_copy_fuzz

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for dict_size in [10, 100, 1000, 10000, 100000]:
        dict_size = random.randrange(dict_size // 2, dict_size + dict_size // 2)
        with self.subTest(dict_size=dict_size):
            d = {}
            for i in range(dict_size):
                d[i] = i
            d2 = d.copy()
            self.assertIsNot(d2, d)
            self.assertEqual(d, d2)
            d2['key'] = 'value'
            self.assertNotEqual(d, d2)
            self.assertEqual(len(d2), len(d) + 1)
