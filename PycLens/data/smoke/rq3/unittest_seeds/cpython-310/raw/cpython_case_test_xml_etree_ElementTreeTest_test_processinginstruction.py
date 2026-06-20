# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: ElementTreeTest_test_processinginstruction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ET.tostring(ET.ProcessingInstruction('test', 'instruction')), b'<?test instruction?>')
    self.assertEqual(ET.tostring(ET.PI('test', 'instruction')), b'<?test instruction?>')
    self.assertEqual(ET.tostring(ET.PI('test', '<testing&>')), b'<?test <testing&>?>')
    self.assertEqual(ET.tostring(ET.PI('test', '<testing&>ã'), 'latin-1'), b"<?xml version='1.0' encoding='latin-1'?>\n<?test <testing&>\xe3?>")
