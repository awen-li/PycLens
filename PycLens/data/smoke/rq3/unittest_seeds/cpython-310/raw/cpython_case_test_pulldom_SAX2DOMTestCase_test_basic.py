# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pulldom.py
# case: SAX2DOMTestCase_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with io.StringIO(SMALL_SAMPLE) as fin:
        sd = SAX2DOMTestHelper(fin, xml.sax.make_parser(), len(SMALL_SAMPLE))
        for (evt, node) in sd:
            if evt == pulldom.START_ELEMENT and node.tagName == 'html':
                break
        self.assertGreater(len(node.childNodes), 0)
