# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_query_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    self.assertEqual(cf.sections(), [], 'new ConfigParser should have no defined sections')
    self.assertFalse(cf.has_section('Foo'), 'new ConfigParser should have no acknowledged sections')
    with self.assertRaises(configparser.NoSectionError):
        cf.options('Foo')
    with self.assertRaises(configparser.NoSectionError):
        cf.set('foo', 'bar', 'value')
    e = self.get_error(cf, configparser.NoSectionError, 'foo', 'bar')
    self.assertEqual(e.args, ('foo',))
    cf.add_section('foo')
    e = self.get_error(cf, configparser.NoOptionError, 'foo', 'bar')
    self.assertEqual(e.args, ('bar', 'foo'))
