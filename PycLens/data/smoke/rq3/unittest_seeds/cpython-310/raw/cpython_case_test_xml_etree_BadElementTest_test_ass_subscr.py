# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_ass_subscr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __index__(self):
            e[:] = []
            return 1
    e = ET.Element('elem')
    for _ in range(10):
        e.insert(0, ET.Element('child'))
    e[0:10:X()] = []
