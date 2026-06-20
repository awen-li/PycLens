# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_preserve_margin_tabs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '  hello there\n\thow are you?'
    self.assertUnchanged(text)
    text = '        hello there\n\thow are you?'
    self.assertUnchanged(text)
    text = '\thello there\n\thow are you?'
    expect = 'hello there\nhow are you?'
    self.assertEqual(expect, dedent(text))
    text = '  \thello there\n  \thow are you?'
    self.assertEqual(expect, dedent(text))
    text = '  \t  hello there\n  \t  how are you?'
    self.assertEqual(expect, dedent(text))
    text = '  \thello there\n  \t  how are you?'
    expect = 'hello there\n  how are you?'
    self.assertEqual(expect, dedent(text))
    text = "  \thello there\n   \thow are you?\n \tI'm fine, thanks"
    expect = " \thello there\n  \thow are you?\n\tI'm fine, thanks"
    self.assertEqual(expect, dedent(text))
