# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: LexicalHandlerTest_test_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestLexicalHandler(LexicalHandler):

        def __init__(self, test_harness, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.test_harness = test_harness

        def startDTD(self, doctype, publicID, systemID):
            self.test_harness.doctype = doctype
            self.test_harness.publicID = publicID
            self.test_harness.systemID = systemID

        def endDTD(self):
            self.test_harness.end_of_dtd = True

        def comment(self, text):
            self.test_harness.comments.append(text)
    self.parser = create_parser()
    self.parser.setContentHandler(ContentHandler())
    self.parser.setProperty('http://xml.org/sax/properties/lexical-handler', TestLexicalHandler(self))
    source = InputSource()
    source.setCharacterStream(self.test_data)
    self.parser.parse(source)
    self.assertEqual(self.doctype, self.specified_doctype)
    self.assertIsNone(self.publicID)
    self.assertIsNone(self.systemID)
    self.assertTrue(self.end_of_dtd)
    self.assertEqual(len(self.comments), len(self.specified_comment))
    self.assertEqual(f' {self.specified_comment[0]} ', self.comments[0])
