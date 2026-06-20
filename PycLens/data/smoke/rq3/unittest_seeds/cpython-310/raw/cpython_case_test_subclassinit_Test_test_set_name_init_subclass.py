# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name_init_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor:

        def __set_name__(self, owner, name):
            self.owner = owner
            self.name = name

    class Meta(type):

        def __new__(cls, name, bases, ns):
            self = super().__new__(cls, name, bases, ns)
            self.meta_owner = self.owner
            self.meta_name = self.name
            return self

    class A:

        def __init_subclass__(cls):
            cls.owner = cls.d.owner
            cls.name = cls.d.name

    class B(A, metaclass=Meta):
        d = Descriptor()
    self.assertIs(B.owner, B)
    self.assertEqual(B.name, 'd')
    self.assertIs(B.meta_owner, B)
    self.assertEqual(B.name, 'd')
