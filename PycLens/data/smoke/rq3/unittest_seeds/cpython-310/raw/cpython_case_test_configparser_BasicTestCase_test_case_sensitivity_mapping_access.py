# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_configparser.py
# case: BasicTestCase_test_case_sensitivity_mapping_access

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cf = self.newconfig()
    cf['A'] = {}
    cf['a'] = {'B': 'value'}
    cf['B'] = {}
    L = [section for section in cf]
    L.sort()
    eq = self.assertEqual
    elem_eq = self.assertCountEqual
    eq(L, sorted(['A', 'B', self.default_section, 'a']))
    eq(cf['a'].keys(), {'b'})
    eq(cf['a']['b'], 'value', 'could not locate option, expecting case-insensitive option names')
    with self.assertRaises(KeyError):
        cf['b']['A'] = 'value'
    self.assertTrue('b' in cf['a'])
    cf['A']['A-B'] = 'A-B value'
    for opt in ('a-b', 'A-b', 'a-B', 'A-B'):
        self.assertTrue(opt in cf['A'], 'has_option() returned false for option which should exist')
    eq(cf['A'].keys(), {'a-b'})
    eq(cf['a'].keys(), {'b'})
    del cf['a']['B']
    elem_eq(cf['a'].keys(), {})
    cf = self.fromstring('[MySection]\nOption{} first line   \n\tsecond line   \n'.format(self.delimiters[0]))
    eq(cf['MySection'].keys(), {'option'})
    eq(cf['MySection']['Option'], 'first line\nsecond line')
    cf = self.fromstring('[section]\nnekey{}nevalue\n'.format(self.delimiters[0]), defaults={'key': 'value'})
    self.assertTrue('Key' in cf['section'])
