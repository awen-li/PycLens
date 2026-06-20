# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_events_comment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser(events=('start', 'comment', 'end'))
    self._feed(parser, '<!-- text here -->\n')
    self.assert_events(parser, [('comment', (ET.Comment, ' text here '))])
    self._feed(parser, '<!-- more text here -->\n')
    self.assert_events(parser, [('comment', (ET.Comment, ' more text here '))])
    self._feed(parser, '<root-tag>text')
    self.assert_event_tags(parser, [('start', 'root-tag')])
    self._feed(parser, '<!-- inner comment-->\n')
    self.assert_events(parser, [('comment', (ET.Comment, ' inner comment'))])
    self._feed(parser, '</root-tag>\n')
    self.assert_event_tags(parser, [('end', 'root-tag')])
    self._feed(parser, '<!-- outer comment -->\n')
    self.assert_events(parser, [('comment', (ET.Comment, ' outer comment '))])
    parser = ET.XMLPullParser(events=('comment',))
    self._feed(parser, '<!-- text here -->\n')
    self.assert_events(parser, [('comment', (ET.Comment, ' text here '))])
