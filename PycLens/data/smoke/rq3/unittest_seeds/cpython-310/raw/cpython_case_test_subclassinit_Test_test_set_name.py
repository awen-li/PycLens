# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subclassinit.py
# case: Test_test_set_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor:

        def __set_name__(self, owner, name):
            self.owner = owner
            self.name = name

    class A:
        d = Descriptor()
    self.assertEqual(A.d.name, 'd')
    self.assertIs(A.d.owner, A)
