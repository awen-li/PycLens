# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_recursive_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = ET.Element('foo')
    with swap_attr(e, 'tag', e):
        with self.assertRaises(RuntimeError):
            repr(e)
