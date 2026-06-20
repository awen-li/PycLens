# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_weird_chars_in_unquoted_attribute_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<form action=bogus|&#()value>', [('starttag', 'form', [('action', 'bogus|&#()value')])])
