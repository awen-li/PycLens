# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: AttributesTestCase_test_comma_between_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    html = '<div class=bar,baz=asd><div class="bar",baz="asd"><div class=bar, baz=asd,><div class="bar", baz="asd",><div class="bar",><div class=,bar baz=,asd><div class=,"bar" baz=,"asd"><div ,class=bar ,baz=asd><div class,="bar" baz,="asd">'
    expected = [('starttag', 'div', [('class', 'bar,baz=asd')]), ('starttag', 'div', [('class', 'bar'), (',baz', 'asd')]), ('starttag', 'div', [('class', 'bar,'), ('baz', 'asd,')]), ('starttag', 'div', [('class', 'bar'), (',', None), ('baz', 'asd'), (',', None)]), ('starttag', 'div', [('class', 'bar'), (',', None)]), ('starttag', 'div', [('class', ',bar'), ('baz', ',asd')]), ('starttag', 'div', [('class', ',"bar"'), ('baz', ',"asd"')]), ('starttag', 'div', [(',class', 'bar'), (',baz', 'asd')]), ('starttag', 'div', [('class,', 'bar'), ('baz,', 'asd')])]
    self._run_check(html, expected)
