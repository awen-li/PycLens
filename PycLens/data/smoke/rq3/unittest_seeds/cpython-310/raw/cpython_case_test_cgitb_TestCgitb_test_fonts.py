# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgitb.py
# case: TestCgitb_test_fonts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = 'Hello Robbie!'
    self.assertEqual(cgitb.small(text), '<small>{}</small>'.format(text))
    self.assertEqual(cgitb.strong(text), '<strong>{}</strong>'.format(text))
    self.assertEqual(cgitb.grey(text), '<font color="#909090">{}</font>'.format(text))
