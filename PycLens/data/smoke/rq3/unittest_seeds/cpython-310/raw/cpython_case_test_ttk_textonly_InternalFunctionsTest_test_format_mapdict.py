# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_format_mapdict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    opts = {'a': [('b', 'c', 'val'), ('d', 'otherval'), ('', 'single')]}
    result = ttk._format_mapdict(opts)
    self.assertEqual(len(result), len(list(opts.keys())) * 2)
    self.assertEqual(result, ('-a', '{b c} val d otherval {} single'))
    self.assertEqual(ttk._format_mapdict(opts, script=True), ('-a', '{{b c} val d otherval {} single}'))
    self.assertEqual(ttk._format_mapdict({2: []}), ('-2', ''))
    opts = {'üñíćódè': [('á', 'vãl')]}
    result = ttk._format_mapdict(opts)
    self.assertEqual(result, ('-üñíćódè', 'á vãl'))
    self.assertEqual(ttk._format_mapdict({'opt': [('value',)]}), ('-opt', '{} value'))
    valid = {'opt': [('', '', 'hi')]}
    self.assertEqual(ttk._format_mapdict(valid), ('-opt', '{ } hi'))
    invalid = {'opt': [(1, 2, 'valid val')]}
    self.assertRaises(TypeError, ttk._format_mapdict, invalid)
    invalid = {'opt': [([1], '2', 'valid val')]}
    self.assertRaises(TypeError, ttk._format_mapdict, invalid)
    valid = {'opt': [[1, 'value']]}
    self.assertEqual(ttk._format_mapdict(valid), ('-opt', '1 value'))
    for stateval in (None, 0, False, '', set()):
        valid = {'opt': [(stateval, 'value')]}
        self.assertEqual(ttk._format_mapdict(valid), ('-opt', '{} value'))
    opts = {'a': None}
    self.assertRaises(TypeError, ttk._format_mapdict, opts)
