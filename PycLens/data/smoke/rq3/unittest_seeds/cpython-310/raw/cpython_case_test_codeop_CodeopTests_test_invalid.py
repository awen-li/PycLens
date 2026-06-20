# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeop.py
# case: CodeopTests_test_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ai = self.assertInvalid
    ai('a b')
    ai('a @')
    ai('a b @')
    ai('a ** @')
    ai('a = ')
    ai('a = 9 +')
    ai('def x():\n\npass\n')
    ai('\n\n if 1: pass\n\npass')
    ai('a = 9+ \\\n')
    ai("a = 'a\\ ")
    ai("a = 'a\\\n")
    ai('a = 1', 'eval')
    ai(']', 'eval')
    ai('())', 'eval')
    ai('[}', 'eval')
    ai('9+', 'eval')
    ai('lambda z:', 'eval')
    ai('a b', 'eval')
    ai('return 2.3')
    ai('if (a == 1 and b = 2): pass')
    ai('del 1')
    ai('del (1,)')
    ai('del [1]')
    ai("del '1'")
    ai('[i for i in range(10)] = (1, 2, 3)')
