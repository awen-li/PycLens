# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_get_starttag_text

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '<foo:bar   \n   one="1"\ttwo=2   >'
    self._run_check_extra(s, [('starttag', 'foo:bar', [('one', '1'), ('two', '2')]), ('starttag_text', s)])
