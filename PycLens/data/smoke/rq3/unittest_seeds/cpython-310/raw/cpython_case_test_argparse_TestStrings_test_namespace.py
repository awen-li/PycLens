# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_argparse.py
# case: TestStrings_test_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = argparse.Namespace(foo=42, bar='spam')
    string = "Namespace(foo=42, bar='spam')"
    self.assertStringEqual(ns, string)
