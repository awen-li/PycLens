# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCase_test_indent_all_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    prefix = '  '
    expected = ('  Hi.\n  This is a test.\n  Testing.', '  Hi.\n  This is a test.\n  \n  Testing.', '  \n  Hi.\n  This is a test.\n  Testing.\n', '  Hi.\r\n  This is a test.\r\n  Testing.\r\n', '  \n  Hi.\r\n  This is a test.\n  \r\n  Testing.\r\n  \n')
    predicate = lambda line: True
    for (text, expect) in zip(self.CASES, expected):
        self.assertEqual(indent(text, prefix, predicate), expect)
