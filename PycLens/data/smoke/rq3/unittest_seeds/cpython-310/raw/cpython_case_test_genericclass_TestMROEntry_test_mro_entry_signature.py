# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tested = []

    class B:
        ...

    class C:

        def __mro_entries__(self, *args, **kwargs):
            tested.extend([args, kwargs])
            return (C,)
    c = C()
    self.assertEqual(tested, [])

    class D(B, c):
        ...
    self.assertEqual(tested[0], ((B, c),))
    self.assertEqual(tested[1], {})
