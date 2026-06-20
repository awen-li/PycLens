# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericclass.py
# case: TestMROEntry_test_mro_entry_type_call

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __mro_entries__(self, bases):
            return ()
    c = C()
    with self.assertRaisesRegex(TypeError, 'MRO entry resolution; use types.new_class()'):
        type('Bad', (c,), {})
