# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_malformed_adjacent_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('<x><y z=""o"" /></x>', [('starttag', 'x', []), ('startendtag', 'y', [('z', ''), ('o""', None)]), ('endtag', 'x')])
    self._run_check('<x><y z="""" /></x>', [('starttag', 'x', []), ('startendtag', 'y', [('z', ''), ('""', None)]), ('endtag', 'x')])
