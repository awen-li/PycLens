# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xml_etree_c.py
# case: MiscTests_test_bpo_31728

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    elem = cET.Element('elem')

    class X:

        def __del__(self):
            elem.text
            elem.tail
            elem.clear()
    elem.text = X()
    elem.clear()
    elem.tail = X()
    elem.clear()
    elem.text = X()
    elem.text = X()
    elem.clear()
    elem.tail = X()
    elem.tail = X()
    elem.clear()
    elem.text = X()
    elem.__setstate__({'tag': 42})
    elem.clear()
    elem.tail = X()
    elem.__setstate__({'tag': 42})
