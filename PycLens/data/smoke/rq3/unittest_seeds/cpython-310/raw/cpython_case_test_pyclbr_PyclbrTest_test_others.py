# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyclbr.py
# case: PyclbrTest_test_others

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cm = self.checkModule
    cm('random', ignore=('Random',))
    cm('cgi', ignore=('log',))
    cm('pickle', ignore=('partial', 'PickleBuffer'))
    cm('aifc', ignore=('_aifc_params',))
    cm('sre_parse', ignore=('dump', 'groups', 'pos'))
    cm('pdb')
    cm('pydoc', ignore=('input', 'output'))
    cm('email.parser')
    cm('test.test_pyclbr')
