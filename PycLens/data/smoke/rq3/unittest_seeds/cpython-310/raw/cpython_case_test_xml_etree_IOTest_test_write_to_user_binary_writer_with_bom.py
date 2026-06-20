# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_user_binary_writer_with_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.ElementTree(ET.XML('<site />'))
    raw = io.BytesIO()
    writer = self.dummy()
    writer.write = raw.write
    writer.seekable = lambda : True
    writer.tell = raw.tell
    tree.write(writer, encoding='utf-16')
    self.assertEqual(raw.getvalue(), "<?xml version='1.0' encoding='utf-16'?>\n<site />".encode('utf-16'))
