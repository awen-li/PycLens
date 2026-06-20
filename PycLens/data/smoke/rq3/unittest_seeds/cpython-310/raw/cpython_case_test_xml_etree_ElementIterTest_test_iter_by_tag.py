# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementIterTest_test_iter_by_tag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    doc = ET.XML('\n            <document>\n                <house>\n                    <room>bedroom1</room>\n                    <room>bedroom2</room>\n                </house>\n                <shed>nothing here\n                </shed>\n                <house>\n                    <room>bedroom8</room>\n                </house>\n            </document>')
    self.assertEqual(self._ilist(doc, 'room'), ['room'] * 3)
    self.assertEqual(self._ilist(doc, 'house'), ['house'] * 2)
    self.assertEqual(summarize_list(doc.iter(tag='room')), ['room'] * 3)
    all_tags = ['document', 'house', 'room', 'room', 'shed', 'house', 'room']
    self.assertEqual(summarize_list(doc.iter()), all_tags)
    self.assertEqual(self._ilist(doc), all_tags)
    self.assertEqual(self._ilist(doc, '*'), all_tags)
