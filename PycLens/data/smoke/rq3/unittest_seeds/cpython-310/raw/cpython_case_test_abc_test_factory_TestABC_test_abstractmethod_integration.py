# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_abc.py
# case: test_factory_TestABC_test_abstractmethod_integration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for abstractthing in [abc.abstractmethod, abc.abstractproperty, abc.abstractclassmethod, abc.abstractstaticmethod]:

        class C(metaclass=abc_ABCMeta):

            @abstractthing
            def foo(self):
                pass

            def bar(self):
                pass
        self.assertEqual(C.__abstractmethods__, {'foo'})
        self.assertRaises(TypeError, C)
        self.assertTrue(isabstract(C))

        class D(C):

            def bar(self):
                pass
        self.assertEqual(D.__abstractmethods__, {'foo'})
        self.assertRaises(TypeError, D)
        self.assertTrue(isabstract(D))

        class E(D):

            def foo(self):
                pass
        self.assertEqual(E.__abstractmethods__, set())
        E()
        self.assertFalse(isabstract(E))

        class F(E):

            @abstractthing
            def bar(self):
                pass
        self.assertEqual(F.__abstractmethods__, {'bar'})
        self.assertRaises(TypeError, F)
        self.assertTrue(isabstract(F))
