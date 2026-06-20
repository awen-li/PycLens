# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_attr_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<a b=\'xxx\n\txxx\' c="yyy\t\nyyy" d=\'\txyz\n\'>', [('starttag', 'a', [('b', 'xxx\n\txxx'), ('c', 'yyy\t\nyyy'), ('d', '\txyz\n')])])
    self._run_check('<a b=\'\' c="">', [('starttag', 'a', [('b', ''), ('c', '')])])
    self._run_check('<e a=rgb(1,2,3)>', [('starttag', 'e', [('a', 'rgb(1,2,3)')])])
    self._run_check('<a href=mailto:xyz@example.com>', [('starttag', 'a', [('href', 'mailto:xyz@example.com')])])
