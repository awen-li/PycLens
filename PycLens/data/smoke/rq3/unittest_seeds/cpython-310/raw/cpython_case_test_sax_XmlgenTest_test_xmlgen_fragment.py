# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sax.py
# case: XmlgenTest_test_xmlgen_fragment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.ioclass()
    gen = XMLGenerator(result)
    gen.startElement('foo', {'a': '1.0'})
    gen.characters('Hello')
    gen.endElement('foo')
    gen.startElement('bar', {'b': '2.0'})
    gen.endElement('bar')
    self.assertEqual(result.getvalue(), self.xml('<foo a="1.0">Hello</foo><bar b="2.0"></bar>')[len(self.xml('')):])
