# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree.py
# case: BadElementTest_test_extend_mutable_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        @property
        def __class__(self):
            L[:] = [ET.Element('baz')]
            return ET.Element
    L = [X()]
    e = ET.Element('foo')
    try:
        e.extend(L)
    except TypeError:
        pass

    class Y(X, ET.Element):
        pass
    L = [Y('x')]
    e = ET.Element('foo')
    e.extend(L)
