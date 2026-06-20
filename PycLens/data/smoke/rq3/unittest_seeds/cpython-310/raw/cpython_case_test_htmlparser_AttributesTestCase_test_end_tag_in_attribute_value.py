# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_end_tag_in_attribute_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<a href=\'http://www.example.org/">;\'>spam</a>', [('starttag', 'a', [('href', 'http://www.example.org/">;')]), ('data', 'spam'), ('endtag', 'a')])
