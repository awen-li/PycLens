# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_namedtuple_special_keyword_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    NT = NamedTuple('NT', cls=type, self=object, typename=str, fields=list)
    self.assertEqual(NT.__name__, 'NT')
    self.assertEqual(NT._fields, ('cls', 'self', 'typename', 'fields'))
    a = NT(cls=str, self=42, typename='foo', fields=[('bar', tuple)])
    self.assertEqual(a.cls, str)
    self.assertEqual(a.self, 42)
    self.assertEqual(a.typename, 'foo')
    self.assertEqual(a.fields, [('bar', tuple)])
