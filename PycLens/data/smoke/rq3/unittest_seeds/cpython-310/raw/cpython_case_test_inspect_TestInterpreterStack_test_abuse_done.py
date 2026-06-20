# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestInterpreterStack_test_abuse_done

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.istest(inspect.istraceback, 'git.ex[2]')
    self.istest(inspect.isframe, 'mod.fr')
