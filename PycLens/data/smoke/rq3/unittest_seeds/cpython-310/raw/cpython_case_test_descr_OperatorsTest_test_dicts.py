# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.binop_test({1: 2, 3: 4}, 1, 1, 'b in a', '__contains__')
    self.binop_test({1: 2, 3: 4}, 2, 0, 'b in a', '__contains__')
    self.binop_test({1: 2, 3: 4}, 1, 2, 'a[b]', '__getitem__')
    d = {1: 2, 3: 4}
    l1 = []
    for i in list(d.keys()):
        l1.append(i)
    l = []
    for i in iter(d):
        l.append(i)
    self.assertEqual(l, l1)
    l = []
    for i in d.__iter__():
        l.append(i)
    self.assertEqual(l, l1)
    l = []
    for i in dict.__iter__(d):
        l.append(i)
    self.assertEqual(l, l1)
    d = {1: 2, 3: 4}
    self.unop_test(d, 2, 'len(a)', '__len__')
    self.assertEqual(eval(repr(d), {}), d)
    self.assertEqual(eval(d.__repr__(), {}), d)
    self.set2op_test({1: 2, 3: 4}, 2, 3, {1: 2, 2: 3, 3: 4}, 'a[b]=c', '__setitem__')
