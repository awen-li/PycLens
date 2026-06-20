# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_funny_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):

        def __new__(cls, arg):
            if isinstance(arg, str):
                return [1, 2, 3]
            elif isinstance(arg, int):
                return object.__new__(D)
            else:
                return object.__new__(cls)

    class D(C):

        def __init__(self, arg):
            self.foo = arg
    self.assertEqual(C('1'), [1, 2, 3])
    self.assertEqual(D('1'), [1, 2, 3])
    d = D(None)
    self.assertEqual(d.foo, None)
    d = C(1)
    self.assertIsInstance(d, D)
    self.assertEqual(d.foo, 1)
    d = D(1)
    self.assertIsInstance(d, D)
    self.assertEqual(d.foo, 1)

    class C(object):

        @staticmethod
        def __new__(*args):
            return args
    self.assertEqual(C(1, 2), (C, 1, 2))

    class D(C):
        pass
    self.assertEqual(D(1, 2), (D, 1, 2))

    class C(object):

        @classmethod
        def __new__(*args):
            return args
    self.assertEqual(C(1, 2), (C, C, 1, 2))

    class D(C):
        pass
    self.assertEqual(D(1, 2), (D, D, 1, 2))
