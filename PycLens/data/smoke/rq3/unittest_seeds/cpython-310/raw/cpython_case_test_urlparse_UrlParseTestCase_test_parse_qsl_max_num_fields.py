# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_parse_qsl_max_num_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):
        urllib.parse.parse_qs('&'.join(['a=a'] * 11), max_num_fields=10)
    urllib.parse.parse_qs('&'.join(['a=a'] * 10), max_num_fields=10)
