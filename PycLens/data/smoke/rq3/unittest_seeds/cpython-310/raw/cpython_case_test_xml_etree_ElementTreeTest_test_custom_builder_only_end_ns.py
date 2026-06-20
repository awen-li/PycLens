# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_custom_builder_only_end_ns

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Builder(list):

        def end_ns(self, prefix):
            self.append(('end-ns', prefix))
    builder = Builder()
    parser = ET.XMLParser(target=builder)
    parser.feed(textwrap.dedent("            <?pi data?>\n            <!-- comment -->\n            <root xmlns='namespace' xmlns:p='pns' xmlns:a='ans'>\n               <a:element key='value'>text</a:element>\n               <p:element>text</p:element>tail\n               <empty-element/>\n            </root>\n            "))
    self.assertEqual(builder, [('end-ns', 'a'), ('end-ns', 'p'), ('end-ns', '')])
