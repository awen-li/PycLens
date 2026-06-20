# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestStdLib_test_inspect_getmembers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    values = dict((('__class__', EnumMeta), ('__doc__', 'An enumeration.'), ('__members__', self.Color.__members__), ('__module__', __name__), ('blue', self.Color.blue), ('green', self.Color.green), ('name', Enum.__dict__['name']), ('red', self.Color.red), ('value', Enum.__dict__['value'])))
    result = dict(inspect.getmembers(self.Color))
    self.assertEqual(values.keys(), result.keys())
    failed = False
    for k in values.keys():
        if result[k] != values[k]:
            print()
            print('\n%s\n     key: %s\n  result: %s\nexpected: %s\n%s\n' % ('=' * 75, k, result[k], values[k], '=' * 75), sep='')
            failed = True
    if failed:
        self.fail('result does not equal expected, see print above')
