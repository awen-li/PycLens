# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_slots

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_slots

    class BA(bytearray):
        __slots__ = ('a', 'b', 'c')
    check(BA(), bytearray(), '3P')

    class D(dict):
        __slots__ = ('a', 'b', 'c')
    check(D(x=[]), {'x': []}, '3P')

    class L(list):
        __slots__ = ('a', 'b', 'c')
    check(L(), [], '3P')

    class S(set):
        __slots__ = ('a', 'b', 'c')
    check(S(), set(), '3P')

    class FS(frozenset):
        __slots__ = ('a', 'b', 'c')
    check(FS(), frozenset(), '3P')
    from collections import OrderedDict

    class OD(OrderedDict):
        __slots__ = ('a', 'b', 'c')
    check(OD(x=[]), OrderedDict(x=[]), '3P')
