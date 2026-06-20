# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name_metaclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Meta(type):

        def __new__(cls, name, bases, ns):
            ret = super().__new__(cls, name, bases, ns)
            self.assertEqual(ret.d.name, 'd')
            self.assertIs(ret.d.owner, ret)
            return 0

    class Descriptor:

        def __set_name__(self, owner, name):
            self.owner = owner
            self.name = name

    class A(metaclass=Meta):
        d = Descriptor()
    self.assertEqual(A, 0)
