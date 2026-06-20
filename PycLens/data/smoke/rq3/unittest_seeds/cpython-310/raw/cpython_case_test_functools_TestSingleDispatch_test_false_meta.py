# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_false_meta

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MetaA(type):

        def __len__(self):
            return 0

    class A(metaclass=MetaA):
        pass

    class AA(A):
        pass

    @functools.singledispatch
    def fun(a):
        return 'base A'

    @fun.register(A)
    def _(a):
        return 'fun A'
    aa = AA()
    self.assertEqual(fun(aa), 'fun A')
