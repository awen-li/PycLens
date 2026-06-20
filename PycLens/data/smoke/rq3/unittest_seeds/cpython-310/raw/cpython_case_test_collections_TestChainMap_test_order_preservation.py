# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestChainMap_test_order_preservation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = ChainMap(OrderedDict(j=0, h=88888), OrderedDict(), OrderedDict(i=9999, d=4444, c=3333), OrderedDict(f=666, b=222, g=777, c=333, h=888), OrderedDict(), OrderedDict(e=55, b=22), OrderedDict(a=1, b=2, c=3, d=4, e=5), OrderedDict())
    self.assertEqual(''.join(d), 'abcdefghij')
    self.assertEqual(list(d.items()), [('a', 1), ('b', 222), ('c', 3333), ('d', 4444), ('e', 55), ('f', 666), ('g', 777), ('h', 88888), ('i', 9999), ('j', 0)])
