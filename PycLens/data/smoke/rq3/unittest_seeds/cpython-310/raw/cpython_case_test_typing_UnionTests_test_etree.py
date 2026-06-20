# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: UnionTests_test_etree

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from xml.etree.ElementTree import Element
    Union[Element, str]

    def Elem(*args):
        return Element(*args)
    Union[Elem, str]
