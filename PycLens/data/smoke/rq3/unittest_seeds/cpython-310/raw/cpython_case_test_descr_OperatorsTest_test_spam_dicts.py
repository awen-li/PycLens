# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_spam_dicts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import copy, xxsubtype as spam

    def spamdict(d, memo=None):
        import xxsubtype as spam
        sd = spam.spamdict()
        for (k, v) in list(d.items()):
            sd[k] = v
        return sd
    copy._deepcopy_dispatch[spam.spamdict] = spamdict
    self.binop_test(spamdict({1: 2, 3: 4}), 1, 1, 'b in a', '__contains__')
    self.binop_test(spamdict({1: 2, 3: 4}), 2, 0, 'b in a', '__contains__')
    self.binop_test(spamdict({1: 2, 3: 4}), 1, 2, 'a[b]', '__getitem__')
    d = spamdict({1: 2, 3: 4})
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
    for i in type(spamdict({})).__iter__(d):
        l.append(i)
    self.assertEqual(l, l1)
    straightd = {1: 2, 3: 4}
    spamd = spamdict(straightd)
    self.unop_test(spamd, 2, 'len(a)', '__len__')
    self.unop_test(spamd, repr(straightd), 'repr(a)', '__repr__')
    self.set2op_test(spamdict({1: 2, 3: 4}), 2, 3, spamdict({1: 2, 2: 3, 3: 4}), 'a[b]=c', '__setitem__')

    class C(spam.spamdict):

        def foo(self):
            return 1
    a = C()
    self.assertEqual(list(a.items()), [])
    self.assertEqual(a.foo(), 1)
    a['foo'] = 'bar'
    self.assertEqual(list(a.items()), [('foo', 'bar')])
    self.assertEqual(a.getstate(), 0)
    a.setstate(100)
    self.assertEqual(a.getstate(), 100)
