# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: TestDescriptions_test_field_order_for_named_tuples

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Person = namedtuple('Person', ['nickname', 'firstname', 'agegroup'])
    s = pydoc.render_doc(Person)
    self.assertLess(s.index('nickname'), s.index('firstname'))
    self.assertLess(s.index('firstname'), s.index('agegroup'))

    class NonIterableFields:
        _fields = None

    class NonHashableFields:
        _fields = [[]]
    pydoc.render_doc(NonIterableFields)
    pydoc.render_doc(NonHashableFields)
