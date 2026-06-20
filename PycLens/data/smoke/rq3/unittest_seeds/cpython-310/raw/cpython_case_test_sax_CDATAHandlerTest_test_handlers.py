# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: CDATAHandlerTest_test_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestLexicalHandler(LexicalHandler):

        def __init__(self, test_harness, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.test_harness = test_harness

        def startCDATA(self):
            self.test_harness.in_cdata = True

        def endCDATA(self):
            self.test_harness.in_cdata = False

    class TestCharHandler(ContentHandler):

        def __init__(self, test_harness, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.test_harness = test_harness

        def characters(self, content):
            if content != '\n':
                h = self.test_harness
                t = h.specified_chars[h.char_index]
                h.assertEqual(t[0], content)
                h.assertEqual(t[1], h.in_cdata)
                h.char_index += 1
    self.parser = create_parser()
    self.parser.setContentHandler(TestCharHandler(self))
    self.parser.setProperty('http://xml.org/sax/properties/lexical-handler', TestLexicalHandler(self))
    source = InputSource()
    source.setCharacterStream(self.test_data)
    self.parser.parse(source)
    self.assertFalse(self.in_cdata)
    self.assertEqual(self.char_index, 2)
