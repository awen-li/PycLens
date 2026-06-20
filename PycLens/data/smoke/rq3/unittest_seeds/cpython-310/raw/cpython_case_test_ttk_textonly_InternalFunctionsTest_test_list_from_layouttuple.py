# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_list_from_layouttuple

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tk = MockTkApp()
    self.assertFalse(ttk._list_from_layouttuple(tk, ()))
    self.assertEqual(ttk._list_from_layouttuple(tk, ('name',)), [('name', {})])
    sample_ltuple = ('name', '-option', 'value')
    self.assertEqual(ttk._list_from_layouttuple(tk, sample_ltuple), [('name', {'option': 'value'})])
    self.assertEqual(ttk._list_from_layouttuple(tk, ('something', '-children', ())), [('something', {'children': []})])
    ltuple = ('name', '-option', 'niceone', '-children', ('otherone', '-children', ('child',), '-otheropt', 'othervalue'))
    self.assertEqual(ttk._list_from_layouttuple(tk, ltuple), [('name', {'option': 'niceone', 'children': [('otherone', {'otheropt': 'othervalue', 'children': [('child', {})]})]})])
    self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, ('name', 'no_minus'))
    self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, ('name', 'no_minus', 'value'))
    self.assertRaises(ValueError, ttk._list_from_layouttuple, tk, ('something', '-children'))
