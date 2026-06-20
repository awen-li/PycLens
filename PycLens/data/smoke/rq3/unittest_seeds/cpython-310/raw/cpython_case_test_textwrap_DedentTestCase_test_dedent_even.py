# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_even

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '  Hello there.\n  How are ya?\n  Oh good.'
    expect = 'Hello there.\nHow are ya?\nOh good.'
    self.assertEqual(expect, dedent(text))
    text = '  Hello there.\n\n  How are ya?\n  Oh good.\n'
    expect = 'Hello there.\n\nHow are ya?\nOh good.\n'
    self.assertEqual(expect, dedent(text))
    text = '  Hello there.\n  \n  How are ya?\n  Oh good.\n'
    expect = 'Hello there.\n\nHow are ya?\nOh good.\n'
    self.assertEqual(expect, dedent(text))
