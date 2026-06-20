# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_preserve_internal_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '  hello\tthere\n  how are\tyou?'
    expect = 'hello\tthere\nhow are\tyou?'
    self.assertEqual(expect, dedent(text))
    self.assertEqual(expect, dedent(expect))
