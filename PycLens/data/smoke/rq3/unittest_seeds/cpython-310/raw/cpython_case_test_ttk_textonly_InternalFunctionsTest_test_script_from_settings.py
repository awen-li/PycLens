# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_script_from_settings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(ttk._script_from_settings({'name': {'configure': None, 'map': None, 'element create': None}}))
    self.assertEqual(ttk._script_from_settings({'name': {'layout': None}}), 'ttk::style layout name {\nnull\n}')
    configdict = {'αβγ': True, 'á': False}
    self.assertTrue(ttk._script_from_settings({'name': {'configure': configdict}}))
    mapdict = {'üñíćódè': [('á', 'vãl')]}
    self.assertTrue(ttk._script_from_settings({'name': {'map': mapdict}}))
    self.assertRaises(IndexError, ttk._script_from_settings, {'name': {'element create': ['image']}})
    self.assertTrue(ttk._script_from_settings({'name': {'element create': ['image', 'name']}}))
    image = {'thing': {'element create': ['image', 'name', ('state1', 'state2', 'val')]}}
    self.assertEqual(ttk._script_from_settings(image), 'ttk::style element create thing image {name {state1 state2} val} ')
    image['thing']['element create'].append({'opt': 30})
    self.assertEqual(ttk._script_from_settings(image), 'ttk::style element create thing image {name {state1 state2} val} -opt 30')
    image['thing']['element create'][-1]['opt'] = [MockTclObj(3), MockTclObj('2m')]
    self.assertEqual(ttk._script_from_settings(image), 'ttk::style element create thing image {name {state1 state2} val} -opt {3 2m}')
