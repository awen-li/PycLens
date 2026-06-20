# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_nomargin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = "Hello there.\nHow are you?\nOh good, I'm glad."
    self.assertUnchanged(text)
    text = 'Hello there.\n\nBoo!'
    self.assertUnchanged(text)
    text = 'Hello there.\n  This is indented.'
    self.assertUnchanged(text)
    text = 'Hello there.\n\n  Boo!\n'
    self.assertUnchanged(text)
