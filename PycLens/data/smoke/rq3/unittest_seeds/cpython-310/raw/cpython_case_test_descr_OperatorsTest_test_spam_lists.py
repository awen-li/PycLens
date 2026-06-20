# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: OperatorsTest_test_spam_lists

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import copy, xxsubtype as spam

    def spamlist(l, memo=None):
        import xxsubtype as spam
        return spam.spamlist(l)
    copy._deepcopy_dispatch[spam.spamlist] = spamlist
    self.binop_test(spamlist([1]), spamlist([2]), spamlist([1, 2]), 'a+b', '__add__')
    self.binop_test(spamlist([1, 2, 3]), 2, 1, 'b in a', '__contains__')
    self.binop_test(spamlist([1, 2, 3]), 4, 0, 'b in a', '__contains__')
    self.binop_test(spamlist([1, 2, 3]), 1, 2, 'a[b]', '__getitem__')
    self.sliceop_test(spamlist([1, 2, 3]), 0, 2, spamlist([1, 2]), 'a[b:c]', '__getitem__')
    self.setop_test(spamlist([1]), spamlist([2]), spamlist([1, 2]), 'a+=b', '__iadd__')
    self.setop_test(spamlist([1, 2]), 3, spamlist([1, 2, 1, 2, 1, 2]), 'a*=b', '__imul__')
    self.unop_test(spamlist([1, 2, 3]), 3, 'len(a)', '__len__')
    self.binop_test(spamlist([1, 2]), 3, spamlist([1, 2, 1, 2, 1, 2]), 'a*b', '__mul__')
    self.binop_test(spamlist([1, 2]), 3, spamlist([1, 2, 1, 2, 1, 2]), 'b*a', '__rmul__')
    self.set2op_test(spamlist([1, 2]), 1, 3, spamlist([1, 3]), 'a[b]=c', '__setitem__')
    self.setsliceop_test(spamlist([1, 2, 3, 4]), 1, 3, spamlist([5, 6]), spamlist([1, 5, 6, 4]), 'a[b:c]=d', '__setitem__')

    class C(spam.spamlist):

        def foo(self):
            return 1
    a = C()
    self.assertEqual(a, [])
    self.assertEqual(a.foo(), 1)
    a.append(100)
    self.assertEqual(a, [100])
    self.assertEqual(a.getstate(), 0)
    a.setstate(42)
    self.assertEqual(a.getstate(), 42)
