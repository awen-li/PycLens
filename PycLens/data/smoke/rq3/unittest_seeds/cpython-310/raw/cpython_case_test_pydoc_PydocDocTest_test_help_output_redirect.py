# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pydoc.py
# case: PydocDocTest_test_help_output_redirect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_pattern = expected_text_pattern
    getpager_old = pydoc.getpager
    getpager_new = lambda : lambda x: x
    self.maxDiff = None
    buf = StringIO()
    helper = pydoc.Helper(output=buf)
    (unused, doc_loc) = get_pydoc_text(pydoc_mod)
    module = 'test.pydoc_mod'
    help_header = '\n        Help on module test.pydoc_mod in test:\n\n        '.lstrip()
    help_header = textwrap.dedent(help_header)
    expected_help_pattern = help_header + expected_text_pattern
    pydoc.getpager = getpager_new
    try:
        with captured_output('stdout') as output, captured_output('stderr') as err:
            helper.help(module)
            result = buf.getvalue().strip()
            expected_text = expected_help_pattern % ((doc_loc,) + expected_text_data_docstrings + (inspect.getabsfile(pydoc_mod),))
            self.assertEqual('', output.getvalue())
            self.assertEqual('', err.getvalue())
            self.assertEqual(expected_text, result)
    finally:
        pydoc.getpager = getpager_old
