# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel = cookies.Morsel()
    self.assertIsNone(morsel.key)
    self.assertIsNone(morsel.value)
    self.assertIsNone(morsel.coded_value)
    self.assertEqual(morsel.keys(), cookies.Morsel._reserved.keys())
    for (key, val) in morsel.items():
        self.assertEqual(val, '', key)
