# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_iter_not_calling_getitem_on_maps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class DictWithGetItem(UserDict):

        def __init__(self, *args, **kwds):
            self.called = False
            UserDict.__init__(self, *args, **kwds)

        def __getitem__(self, item):
            self.called = True
            UserDict.__getitem__(self, item)
    d = DictWithGetItem(a=1)
    c = ChainMap(d)
    d.called = False
    set(c)
    self.assertFalse(d.called, '__getitem__ was called')
