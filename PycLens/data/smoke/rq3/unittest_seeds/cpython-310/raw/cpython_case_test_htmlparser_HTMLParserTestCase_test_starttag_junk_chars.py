# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_starttag_junk_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._run_check('</>', [])
    self._run_check('</$>', [('comment', '$')])
    self._run_check('</', [('data', '</')])
    self._run_check('</a', [('data', '</a')])
    self._run_check('<a<a>', [('starttag', 'a<a', [])])
    self._run_check('</a<a>', [('endtag', 'a<a')])
    self._run_check('<!', [('data', '<!')])
    self._run_check('<a', [('data', '<a')])
    self._run_check("<a foo='bar'", [('data', "<a foo='bar'")])
    self._run_check("<a foo='bar", [('data', "<a foo='bar")])
    self._run_check("<a foo='>'", [('data', "<a foo='>'")])
    self._run_check("<a foo='>", [('data', "<a foo='>")])
    self._run_check('<a$>', [('starttag', 'a$', [])])
    self._run_check('<a$b>', [('starttag', 'a$b', [])])
    self._run_check('<a$b/>', [('startendtag', 'a$b', [])])
    self._run_check('<a$b  >', [('starttag', 'a$b', [])])
    self._run_check('<a$b  />', [('startendtag', 'a$b', [])])
