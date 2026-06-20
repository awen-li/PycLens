# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_1463026_2_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result, short_empty_elements=True)
    gen.startDocument()
    gen.startPrefixMapping(None, 'qux')
    gen.startElementNS(('qux', 'a'), 'a', {})
    gen.endElementNS(('qux', 'a'), 'a')
    gen.endPrefixMapping(None)
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<a xmlns="qux"/>'))
