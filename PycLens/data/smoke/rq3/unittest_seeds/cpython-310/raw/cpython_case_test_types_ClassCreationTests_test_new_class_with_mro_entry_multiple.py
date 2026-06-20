# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_new_class_with_mro_entry_multiple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A1:
        pass

    class A2:
        pass

    class B1:
        pass

    class B2:
        pass

    class A:

        def __mro_entries__(self, bases):
            return (A1, A2)

    class B:

        def __mro_entries__(self, bases):
            return (B1, B2)
    D = types.new_class('D', (A(), B()), {})
    self.assertEqual(D.__bases__, (A1, A2, B1, B2))
