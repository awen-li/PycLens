# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_starttag_end_boundary

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check("<a b='<'>", [('starttag', 'a', [('b', '<')])])
    self._run_check("<a b='>'>", [('starttag', 'a', [('b', '>')])])
