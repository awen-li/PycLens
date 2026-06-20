# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_format.py
# case: FormatTest_test_optimisations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'abcde'
    self.assertIs('%s' % text, text)
    self.assertIs('%.5s' % text, text)
    self.assertIs('%.10s' % text, text)
    self.assertIs('%1s' % text, text)
    self.assertIs('%5s' % text, text)
    self.assertIs('{0}'.format(text), text)
    self.assertIs('{0:s}'.format(text), text)
    self.assertIs('{0:.5s}'.format(text), text)
    self.assertIs('{0:.10s}'.format(text), text)
    self.assertIs('{0:1s}'.format(text), text)
    self.assertIs('{0:5s}'.format(text), text)
    self.assertIs(text % (), text)
    self.assertIs(text.format(), text)
