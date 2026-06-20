# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_empty_line_after_linecont

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = '\\\npass\n        \\\n\npass\n'
    try:
        compile(s, '<string>', 'exec')
    except SyntaxError:
        self.fail('Empty line after a line continuation character is valid.')
    s1 = "\\\ndef fib(n):\n    \\\n'''Print a Fibonacci series up to n.'''\n    \\\na, b = 0, 1\n"
    s2 = "\\\ndef fib(n):\n    '''Print a Fibonacci series up to n.'''\n    a, b = 0, 1\n"
    try:
        self.assertEqual(compile(s1, '<string>', 'exec'), compile(s2, '<string>', 'exec'))
    except SyntaxError:
        self.fail('Indented statement over multiple lines is valid')
