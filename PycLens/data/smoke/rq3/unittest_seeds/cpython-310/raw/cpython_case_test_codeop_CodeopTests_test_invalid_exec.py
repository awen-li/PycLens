# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codeop.py
# case: CodeopTests_test_invalid_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ai = self.assertInvalid
    ai('raise = 4', symbol='exec')
    ai('def a-b', symbol='exec')
    ai('await?', symbol='exec')
    ai('=!=', symbol='exec')
    ai('a await raise b', symbol='exec')
    ai('a await raise b?+1', symbol='exec')
