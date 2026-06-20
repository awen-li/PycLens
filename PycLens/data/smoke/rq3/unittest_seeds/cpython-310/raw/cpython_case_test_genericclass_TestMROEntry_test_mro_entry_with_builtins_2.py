# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_with_builtins_2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tested = []

    class C:

        def __mro_entries__(self, bases):
            tested.append(bases)
            return (C,)
    c = C()
    self.assertEqual(tested, [])

    class D(c, dict):
        ...
    self.assertEqual(tested[-1], (c, dict))
    self.assertEqual(D.__bases__, (C, dict))
    self.assertEqual(D.__orig_bases__, (c, dict))
    self.assertEqual(D.__mro__, (D, C, dict, object))
