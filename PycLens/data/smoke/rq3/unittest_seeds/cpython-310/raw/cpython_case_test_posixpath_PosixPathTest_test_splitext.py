# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posixpath.py
# case: PosixPathTest_test_splitext

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.splitextTest('foo.bar', 'foo', '.bar')
    self.splitextTest('foo.boo.bar', 'foo.boo', '.bar')
    self.splitextTest('foo.boo.biff.bar', 'foo.boo.biff', '.bar')
    self.splitextTest('.csh.rc', '.csh', '.rc')
    self.splitextTest('nodots', 'nodots', '')
    self.splitextTest('.cshrc', '.cshrc', '')
    self.splitextTest('...manydots', '...manydots', '')
    self.splitextTest('...manydots.ext', '...manydots', '.ext')
    self.splitextTest('.', '.', '')
    self.splitextTest('..', '..', '')
    self.splitextTest('........', '........', '')
    self.splitextTest('', '', '')
