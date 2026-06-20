# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_textwrap.py
# case: DedentTestCase_test_dedent_uneven

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    text = '        def foo():\n            while 1:\n                return foo\n        '
    expect = 'def foo():\n    while 1:\n        return foo\n'
    self.assertEqual(expect, dedent(text))
    text = '  Foo\n    Bar\n\n   Baz\n'
    expect = 'Foo\n  Bar\n\n Baz\n'
    self.assertEqual(expect, dedent(text))
    text = '  Foo\n    Bar\n \n   Baz\n'
    expect = 'Foo\n  Bar\n\n Baz\n'
    self.assertEqual(expect, dedent(text))
