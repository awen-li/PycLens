# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_1463026_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startPrefixMapping('my', 'qux')
    gen.startElementNS(('qux', 'a'), 'a', {(None, 'b'): 'c'})
    gen.endElementNS(('qux', 'a'), 'a')
    gen.endPrefixMapping('my')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<my:a xmlns:my="qux" b="c"></my:a>'))
