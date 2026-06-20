# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_resolve_bases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A:
        pass

    class B:
        pass

    class C:

        def __mro_entries__(self, bases):
            if A in bases:
                return ()
            return (A,)
    c = C()
    self.assertEqual(types.resolve_bases(()), ())
    self.assertEqual(types.resolve_bases((c,)), (A,))
    self.assertEqual(types.resolve_bases((C,)), (C,))
    self.assertEqual(types.resolve_bases((A, C)), (A, C))
    self.assertEqual(types.resolve_bases((c, A)), (A,))
    self.assertEqual(types.resolve_bases((A, c)), (A,))
    x = (A,)
    y = (C,)
    z = (A, C)
    t = (A, C, B)
    for bases in [x, y, z, t]:
        self.assertIs(types.resolve_bases(bases), bases)
