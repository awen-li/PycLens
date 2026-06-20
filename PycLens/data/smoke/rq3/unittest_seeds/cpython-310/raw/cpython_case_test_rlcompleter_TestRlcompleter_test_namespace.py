# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_rlcompleter.py
# case: TestRlcompleter_test_namespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class A(dict):
        pass

    class B(list):
        pass
    self.assertTrue(self.stdcompleter.use_main_ns)
    self.assertFalse(self.completer.use_main_ns)
    self.assertFalse(rlcompleter.Completer(A()).use_main_ns)
    self.assertRaises(TypeError, rlcompleter.Completer, B((1,)))
