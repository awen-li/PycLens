# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_events_sequence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eventset = {'end', 'start'}
    parser = ET.XMLPullParser(events=eventset)
    self._feed(parser, '<foo>bar</foo>')
    self.assert_event_tags(parser, [('start', 'foo'), ('end', 'foo')])

    class DummyIter:

        def __init__(self):
            self.events = iter(['start', 'end', 'start-ns'])

        def __iter__(self):
            return self

        def __next__(self):
            return next(self.events)
    parser = ET.XMLPullParser(events=DummyIter())
    self._feed(parser, '<foo>bar</foo>')
    self.assert_event_tags(parser, [('start', 'foo'), ('end', 'foo')])
