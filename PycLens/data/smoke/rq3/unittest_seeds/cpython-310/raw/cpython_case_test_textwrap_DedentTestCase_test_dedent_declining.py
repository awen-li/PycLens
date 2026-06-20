# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_declining

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '     Foo\n    Bar\n'
    expect = ' Foo\nBar\n'
    self.assertEqual(expect, dedent(text))
    text = '     Foo\n\n    Bar\n'
    expect = ' Foo\n\nBar\n'
    self.assertEqual(expect, dedent(text))
    text = '     Foo\n    \n    Bar\n'
    expect = ' Foo\n\nBar\n'
    self.assertEqual(expect, dedent(text))
