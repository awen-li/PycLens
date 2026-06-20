# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_forward_equality_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    def namespace1():
        a = typing.ForwardRef('A')

        def fun(x: a):
            pass
        get_type_hints(fun, globals(), locals())
        return a

    def namespace2():
        a = typing.ForwardRef('A')

        class A:
            pass

        def fun(x: a):
            pass
        get_type_hints(fun, globals(), locals())
        return a
    self.assertEqual(namespace1(), namespace1())
    self.assertNotEqual(namespace1(), namespace2())
