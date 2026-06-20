# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_htmlparser.py
# case: HTMLParserTestCase_test_cdata_with_closing_tags

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Collector(EventCollector):

        def get_events(self):
            return self.events
    content = '<!-- not a comment --> &not-an-entity-ref;\n                  <a href="" /> </p><p> <span></span></style>\n                  \'</script\' + \'>\''
    for element in [' script', 'script ', ' script ', '\nscript', 'script\n', '\nscript\n']:
        element_lower = element.lower().strip()
        s = '<script>{content}</{element}>'.format(element=element, content=content)
        self._run_check(s, [('starttag', element_lower, []), ('data', content), ('endtag', element_lower)], collector=Collector(convert_charrefs=False))
