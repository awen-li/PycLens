# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_http_cookies.py
# case: MorselTests_test_set_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    morsel = cookies.Morsel()
    with self.assertRaises(AttributeError):
        morsel.key = ''
    with self.assertRaises(AttributeError):
        morsel.value = ''
    with self.assertRaises(AttributeError):
        morsel.coded_value = ''
