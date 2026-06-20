# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: RawConfigParserTestCase_test_set_nonstring_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    cf.add_section('non-string')
    cf.set('non-string', 'int', 1)
    cf.set('non-string', 'list', [0, 1, 1, 2, 3, 5, 8, 13])
    cf.set('non-string', 'dict', {'pi': 3.14159})
    self.assertEqual(cf.get('non-string', 'int'), 1)
    self.assertEqual(cf.get('non-string', 'list'), [0, 1, 1, 2, 3, 5, 8, 13])
    self.assertEqual(cf.get('non-string', 'dict'), {'pi': 3.14159})
    cf.add_section(123)
    cf.set(123, 'this is sick', True)
    self.assertEqual(cf.get(123, 'this is sick'), True)
    if cf._dict is configparser._default_dict:
        cf.optionxform = lambda x: x
        cf.set('non-string', 1, 1)
        self.assertEqual(cf.get('non-string', 1), 1)
