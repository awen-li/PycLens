# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_ns_events_start_end

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser(events=('start-ns', 'start', 'end', 'end-ns'))
    self._feed(parser, "<tag xmlns='abc' xmlns:p='xyz'>\n")
    self.assert_event_tuples(parser, [('start-ns', ('', 'abc')), ('start-ns', ('p', 'xyz'))], max_events=2)
    self.assert_event_tags(parser, [('start', '{abc}tag')], max_events=1)
    self._feed(parser, '<child />\n')
    self.assert_event_tags(parser, [('start', '{abc}child'), ('end', '{abc}child')])
    self._feed(parser, '</tag>\n')
    parser.close()
    self.assert_event_tags(parser, [('end', '{abc}tag')], max_events=1)
    self.assert_event_tuples(parser, [('end-ns', None), ('end-ns', None)])
