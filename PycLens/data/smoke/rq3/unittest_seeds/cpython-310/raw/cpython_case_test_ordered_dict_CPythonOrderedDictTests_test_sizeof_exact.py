# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: CPythonOrderedDictTests_test_sizeof_exact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    calcsize = struct.calcsize
    size = support.calcobjsize
    check = self.check_sizeof
    basicsize = size('nQ2P' + '3PnPn2P')
    keysize = calcsize('2nP2n')
    entrysize = calcsize('n2P')
    p = calcsize('P')
    nodesize = calcsize('Pn2P')
    od = OrderedDict()
    check(od, basicsize)
    od.x = 1
    check(od, basicsize)
    od.update([(i, i) for i in range(3)])
    check(od, basicsize + keysize + 8 * p + 8 + 5 * entrysize + 3 * nodesize)
    od.update([(i, i) for i in range(3, 10)])
    check(od, basicsize + keysize + 16 * p + 16 + 10 * entrysize + 10 * nodesize)
    check(od.keys(), size('P'))
    check(od.items(), size('P'))
    check(od.values(), size('P'))
    itersize = size('iP2n2P')
    check(iter(od), itersize)
    check(iter(od.keys()), itersize)
    check(iter(od.items()), itersize)
    check(iter(od.values()), itersize)
