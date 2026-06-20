# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BasicElementTest_test_get_keyword_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e1 = ET.Element('foo', x=1, y=2, z=3)
    self.assertEqual(e1.get('x', default=7), 1)
    self.assertEqual(e1.get('w', default=7), 7)
