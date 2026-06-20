# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: IndentTestCase_test_roundtrip_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for text in self.ROUNDTRIP_CASES:
        self.assertEqual(dedent(indent(text, '\t\t')), text)
