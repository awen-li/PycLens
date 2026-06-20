# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: C14NTest_test_c14n_exclusion

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml = textwrap.dedent('        <root xmlns:x="http://example.com/x">\n            <a x:attr="attrx">\n                <b>abtext</b>\n            </a>\n            <b>btext</b>\n            <c>\n                <x:d>dtext</x:d>\n            </c>\n        </root>\n        ')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True), '<root><a xmlns:x="http://example.com/x" x:attr="attrx"><b>abtext</b></a><b>btext</b><c><x:d xmlns:x="http://example.com/x">dtext</x:d></c></root>')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True, exclude_attrs=['{http://example.com/x}attr']), '<root><a><b>abtext</b></a><b>btext</b><c><x:d xmlns:x="http://example.com/x">dtext</x:d></c></root>')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True, exclude_tags=['{http://example.com/x}d']), '<root><a xmlns:x="http://example.com/x" x:attr="attrx"><b>abtext</b></a><b>btext</b><c></c></root>')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True, exclude_attrs=['{http://example.com/x}attr'], exclude_tags=['{http://example.com/x}d']), '<root><a><b>abtext</b></a><b>btext</b><c></c></root>')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True, exclude_tags=['a', 'b']), '<root><c><x:d xmlns:x="http://example.com/x">dtext</x:d></c></root>')
    self.assertEqual(c14n_roundtrip(xml, exclude_tags=['a', 'b']), '<root>\n    \n    \n    <c>\n        <x:d xmlns:x="http://example.com/x">dtext</x:d>\n    </c>\n</root>')
    self.assertEqual(c14n_roundtrip(xml, strip_text=True, exclude_tags=['{http://example.com/x}d', 'b']), '<root><a xmlns:x="http://example.com/x" x:attr="attrx"></a><c></c></root>')
    self.assertEqual(c14n_roundtrip(xml, exclude_tags=['{http://example.com/x}d', 'b']), '<root>\n    <a xmlns:x="http://example.com/x" x:attr="attrx">\n        \n    </a>\n    \n    <c>\n        \n    </c>\n</root>')
