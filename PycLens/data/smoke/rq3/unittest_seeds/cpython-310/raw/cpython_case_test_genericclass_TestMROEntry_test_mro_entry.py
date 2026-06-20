# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tested = []

    class A:
        ...

    class B:
        ...

    class C:

        def __mro_entries__(self, bases):
            tested.append(bases)
            return (self.__class__,)
    c = C()
    self.assertEqual(tested, [])

    class D(A, c, B):
        ...
    self.assertEqual(tested[-1], (A, c, B))
    self.assertEqual(D.__bases__, (A, C, B))
    self.assertEqual(D.__orig_bases__, (A, c, B))
    self.assertEqual(D.__mro__, (D, A, C, B, object))
    d = D()

    class E(d):
        ...
    self.assertEqual(tested[-1], (d,))
    self.assertEqual(E.__bases__, (D,))
