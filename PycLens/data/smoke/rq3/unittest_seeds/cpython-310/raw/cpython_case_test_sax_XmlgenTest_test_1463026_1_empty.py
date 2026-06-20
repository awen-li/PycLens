# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_1463026_1_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result, short_empty_elements=True)
    gen.startDocument()
    gen.startElementNS((None, 'a'), 'a', {(None, 'b'): 'c'})
    gen.endElementNS((None, 'a'), 'a')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<a b="c"/>'))
