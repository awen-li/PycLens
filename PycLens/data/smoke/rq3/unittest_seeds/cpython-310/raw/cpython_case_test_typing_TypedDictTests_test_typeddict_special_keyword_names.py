# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_typeddict_special_keyword_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    TD = TypedDict('TD', cls=type, self=object, typename=str, _typename=int, fields=list, _fields=dict)
    self.assertEqual(TD.__name__, 'TD')
    self.assertEqual(TD.__annotations__, {'cls': type, 'self': object, 'typename': str, '_typename': int, 'fields': list, '_fields': dict})
    a = TD(cls=str, self=42, typename='foo', _typename=53, fields=[('bar', tuple)], _fields={'baz', set})
    self.assertEqual(a['cls'], str)
    self.assertEqual(a['self'], 42)
    self.assertEqual(a['typename'], 'foo')
    self.assertEqual(a['_typename'], 53)
    self.assertEqual(a['fields'], [('bar', tuple)])
    self.assertEqual(a['_fields'], {'baz', set})
