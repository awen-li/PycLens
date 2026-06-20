# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_5027_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startDocument()
    gen.startPrefixMapping('a', 'http://example.com/ns')
    gen.startElementNS(('http://example.com/ns', 'g1'), 'g1', {})
    lang_attr = {('http://www.w3.org/XML/1998/namespace', 'lang'): 'en'}
    gen.startElementNS(('http://example.com/ns', 'g2'), 'g2', lang_attr)
    gen.characters('Hello')
    gen.endElementNS(('http://example.com/ns', 'g2'), 'g2')
    gen.endElementNS(('http://example.com/ns', 'g1'), 'g1')
    gen.endPrefixMapping('a')
    gen.endDocument()
    self.assertEqual(result.getvalue(), self.xml('<a:g1 xmlns:a="http://example.com/ns"><a:g2 xml:lang="en">Hello</a:g2></a:g1>'))
