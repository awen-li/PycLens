# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_correct_detection_of_start_tags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<div style=""    ><b>The <a href="some_url">rain</a> <br /> in <span>Spain</span></b></div>'
    expected = [('starttag', 'div', [('style', '')]), ('starttag', 'b', []), ('data', 'The '), ('starttag', 'a', [('href', 'some_url')]), ('data', 'rain'), ('endtag', 'a'), ('data', ' '), ('startendtag', 'br', []), ('data', ' in '), ('starttag', 'span', []), ('data', 'Spain'), ('endtag', 'span'), ('endtag', 'b'), ('endtag', 'div')]
    self._run_check(html, expected)
    html = '<div style="", foo = "bar" ><b>The <a href="some_url">rain</a>'
    expected = [('starttag', 'div', [('style', ''), (',', None), ('foo', 'bar')]), ('starttag', 'b', []), ('data', 'The '), ('starttag', 'a', [('href', 'some_url')]), ('data', 'rain'), ('endtag', 'a')]
    self._run_check(html, expected)
