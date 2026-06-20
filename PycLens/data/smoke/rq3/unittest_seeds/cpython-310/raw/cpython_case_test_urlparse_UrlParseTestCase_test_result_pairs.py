# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: UrlParseTestCase_test_result_pairs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result_types = [urllib.parse.DefragResult, urllib.parse.SplitResult, urllib.parse.ParseResult]
    for result_type in result_types:
        self._check_result_type(result_type)
