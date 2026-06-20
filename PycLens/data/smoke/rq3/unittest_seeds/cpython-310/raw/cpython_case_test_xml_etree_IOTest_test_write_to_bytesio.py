# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: IOTest_test_write_to_bytesio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tree = ET.ElementTree(ET.XML('<site>ø</site>'))
    raw = io.BytesIO()
    tree.write(raw)
    self.assertEqual(raw.getvalue(), b'<site>&#248;</site>')
