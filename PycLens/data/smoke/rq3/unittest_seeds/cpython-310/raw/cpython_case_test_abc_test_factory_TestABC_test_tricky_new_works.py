# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_tricky_new_works

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def with_metaclass(meta, *bases):

        class metaclass(type):

            def __new__(cls, name, this_bases, d):
                return meta(name, bases, d)
        return type.__new__(metaclass, 'temporary_class', (), {})

    class A:
        ...

    class B:
        ...

    class C(with_metaclass(abc_ABCMeta, A, B)):
        pass
    self.assertEqual(C.__class__, abc_ABCMeta)
