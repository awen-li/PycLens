# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XMLFilterBaseTest_test_filter_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = BytesIO()
    gen = XMLGenerator(result)
    filter = XMLFilterBase()
    filter.setContentHandler(gen)
    filter.startDocument()
    filter.startElement('doc', {})
    filter.characters('content')
    filter.ignorableWhitespace(' ')
    filter.endElement('doc')
    filter.endDocument()
    self.assertEqual(result.getvalue(), start + b'<doc>content </doc>')
