# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_dict_disappearing_during_get_item

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __hash__(self):
            e.attrib = {}
            [{i: i} for i in range(1000)]
            return 13
    e = cET.Element('elem', {1: 2})
    r = e.get(X())
    self.assertIsNone(r)
