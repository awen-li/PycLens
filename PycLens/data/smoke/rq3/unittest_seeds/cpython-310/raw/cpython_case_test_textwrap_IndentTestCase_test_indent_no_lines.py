# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCase_test_indent_no_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    predicate = lambda line: False
    for text in self.CASES:
        self.assertEqual(indent(text, '    ', predicate), text)
