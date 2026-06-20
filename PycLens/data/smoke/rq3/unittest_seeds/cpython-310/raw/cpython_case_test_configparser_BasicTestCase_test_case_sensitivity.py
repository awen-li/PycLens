# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_case_sensitivity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    cf.add_section('A')
    cf.add_section('a')
    cf.add_section('B')
    L = cf.sections()
    L.sort()
    eq = self.assertEqual
    eq(L, ['A', 'B', 'a'])
    cf.set('a', 'B', 'value')
    eq(cf.options('a'), ['b'])
    eq(cf.get('a', 'b'), 'value', 'could not locate option, expecting case-insensitive option names')
    with self.assertRaises(configparser.NoSectionError):
        cf.set('b', 'A', 'value')
    self.assertTrue(cf.has_option('a', 'b'))
    self.assertFalse(cf.has_option('b', 'b'))
    cf.set('A', 'A-B', 'A-B value')
    for opt in ('a-b', 'A-b', 'a-B', 'A-B'):
        self.assertTrue(cf.has_option('A', opt), 'has_option() returned false for option which should exist')
    eq(cf.options('A'), ['a-b'])
    eq(cf.options('a'), ['b'])
    cf.remove_option('a', 'B')
    eq(cf.options('a'), [])
    cf = self.fromstring('[MySection]\nOption{} first line   \n\tsecond line   \n'.format(self.delimiters[0]))
    eq(cf.options('MySection'), ['option'])
    eq(cf.get('MySection', 'Option'), 'first line\nsecond line')
    cf = self.fromstring('[section]\nnekey{}nevalue\n'.format(self.delimiters[0]), defaults={'key': 'value'})
    self.assertTrue(cf.has_option('section', 'Key'))
