# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_user_text_writer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    stream = io.StringIO()
    writer = self.dummy()
    writer.write = stream.write
    tree.write(writer, encoding='unicode')
    self.assertEqual(stream.getvalue(), '<site>ø</site>')
