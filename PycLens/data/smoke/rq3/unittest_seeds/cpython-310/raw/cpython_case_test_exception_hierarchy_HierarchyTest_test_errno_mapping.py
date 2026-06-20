# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: HierarchyTest_test_errno_mapping

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    e = OSError(EEXIST, 'Bad file descriptor')
    self.assertIs(type(e), FileExistsError)
    for (errcode, exc) in self._map.items():
        e = OSError(errcode, 'Some message')
        self.assertIs(type(e), exc)
    othercodes = set(errno.errorcode) - set(self._map)
    for errcode in othercodes:
        e = OSError(errcode, 'Some message')
        self.assertIs(type(e), OSError)
