# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_forward_recursion_actually

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def namespace1():
        a = typing.ForwardRef('A')
        A = a

        def fun(x: a):
            pass
        ret = get_type_hints(fun, globals(), locals())
        return a

    def namespace2():
        a = typing.ForwardRef('A')
        A = a

        def fun(x: a):
            pass
        ret = get_type_hints(fun, globals(), locals())
        return a

    def cmp(o1, o2):
        return o1 == o2
    r1 = namespace1()
    r2 = namespace2()
    self.assertIsNot(r1, r2)
    self.assertRaises(RecursionError, cmp, r1, r2)
