# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: StringModuleTest_test_formatter_parser

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def parse(format):
        return list(_string.formatter_parser(format))
    formatter = parse('prefix {2!s}xxx{0:^+10.3f}{obj.attr!s} {z[0]!s:10}')
    self.assertEqual(formatter, [('prefix ', '2', '', 's'), ('xxx', '0', '^+10.3f', None), ('', 'obj.attr', '', 's'), (' ', 'z[0]', '10', 's')])
    formatter = parse('prefix {} suffix')
    self.assertEqual(formatter, [('prefix ', '', '', None), (' suffix', None, None, None)])
    formatter = parse('str')
    self.assertEqual(formatter, [('str', None, None, None)])
    formatter = parse('')
    self.assertEqual(formatter, [])
    formatter = parse('{0}')
    self.assertEqual(formatter, [('', '0', '', None)])
    self.assertRaises(TypeError, _string.formatter_parser, 1)
