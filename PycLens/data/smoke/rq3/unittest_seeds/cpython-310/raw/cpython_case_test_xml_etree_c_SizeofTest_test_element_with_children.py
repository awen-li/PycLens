# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: SizeofTest_test_element_with_children

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = cET.Element('a')
    for i in range(5):
        cET.SubElement(e, 'span')
    self.check_sizeof(e, self.elementsize + self.extra + struct.calcsize('8P'))
