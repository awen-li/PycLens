# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: XMLPullParserTest_test_events_pi

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = ET.XMLPullParser(events=('start', 'pi', 'end'))
    self._feed(parser, '<?pitarget?>\n')
    self.assert_events(parser, [('pi', (ET.PI, 'pitarget'))])
    parser = ET.XMLPullParser(events=('pi',))
    self._feed(parser, '<?pitarget some text ?>\n')
    self.assert_events(parser, [('pi', (ET.PI, 'pitarget some text '))])
