# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exception_hierarchy.py
# case: HierarchyTest_test_socket_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(socket.error, OSError)
    self.assertIs(socket.gaierror.__base__, OSError)
    self.assertIs(socket.herror.__base__, OSError)
    self.assertIs(socket.timeout, TimeoutError)
