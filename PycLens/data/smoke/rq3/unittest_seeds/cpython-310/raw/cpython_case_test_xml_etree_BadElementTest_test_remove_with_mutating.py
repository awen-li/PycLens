# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_remove_with_mutating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(ET.Element):

        def __eq__(self, o):
            del e[:]
            return False
    e = ET.Element('foo')
    e.extend([X('bar')])
    self.assertRaises(ValueError, e.remove, ET.Element('baz'))
    e = ET.Element('foo')
    e.extend([ET.Element('bar')])
    self.assertRaises(ValueError, e.remove, X('baz'))
