# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ttk_textonly.py
# case: InternalFunctionsTest_test_format_layoutlist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def sample(indent=0, indent_size=2):
        return ttk._format_layoutlist([('a', {'other': [1, 2, 3], 'children': [('b', {'children': [('c', {'children': [('d', {'nice': 'opt'})], 'something': (1, 2)})]})]})], indent=indent, indent_size=indent_size)[0]

    def sample_expected(indent=0, indent_size=2):
        spaces = lambda amount=0: ' ' * (amount + indent)
        return '%sa -other {1 2 3} -children {\n%sb -children {\n%sc -something {1 2} -children {\n%sd -nice opt\n%s}\n%s}\n%s}' % (spaces(), spaces(indent_size), spaces(2 * indent_size), spaces(3 * indent_size), spaces(2 * indent_size), spaces(indent_size), spaces())
    self.assertEqual(ttk._format_layoutlist([])[0], '')
    self.assertRaises(AttributeError, ttk._format_layoutlist, [('a', 'b')])
    smallest = ttk._format_layoutlist([('a', None)], indent=0)
    self.assertEqual(smallest, ttk._format_layoutlist([('a', '')], indent=0))
    self.assertEqual(smallest[0], 'a')
    self.assertEqual(sample(), sample_expected())
    for i in range(4):
        self.assertEqual(sample(i), sample_expected(i))
        self.assertEqual(sample(i, i), sample_expected(i, i))
    self.assertRaises(ValueError, ttk._format_layoutlist, ['bad', 'format'])
    self.assertRaises(AttributeError, ttk._format_layoutlist, [('name', 'bad')])
    self.assertRaises(ValueError, ttk._format_layoutlist, [('name', {'children': {'a': None}})])
