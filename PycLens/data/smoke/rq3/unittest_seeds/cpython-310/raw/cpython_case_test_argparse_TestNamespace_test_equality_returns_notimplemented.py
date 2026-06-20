# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestNamespace_test_equality_returns_notimplemented

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = argparse.Namespace(a=1, b=2)
    self.assertIs(ns.__eq__(None), NotImplemented)
    self.assertIs(ns.__ne__(None), NotImplemented)
