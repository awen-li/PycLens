# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_isinstance.py
# case: TestIsInstanceIsSubclass_test_infinitely_many_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X:

        def __getattr__(self, attr):
            self.assertEqual(attr, '__bases__')

            class A:
                pass

            class B:
                pass
            A.__getattr__ = B.__getattr__ = X.__getattr__
            return (A(), B())
    with support.infinite_recursion():
        self.assertRaises(RecursionError, issubclass, X(), int)
