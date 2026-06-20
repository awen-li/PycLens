# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_subscr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __index__(self):
            del e[:]
            return 1
    e = ET.Element('elem')
    e.append(ET.Element('child'))
    e[:X()]
    e.append(ET.Element('child'))
    e[0:10:X()]
