# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: UnionTests_test_or_type_operator_with_bad_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadMeta(type):
        __qualname__ = 'TypeVar'

        @property
        def __module__(self):
            1 / 0
    TypeVar = BadMeta('TypeVar', (), {})
    _SpecialForm = BadMeta('_SpecialForm', (), {})
    with self.assertRaises((TypeError, ZeroDivisionError)):
        str | TypeVar()
    with self.assertRaises((TypeError, ZeroDivisionError)):
        str | _SpecialForm()
