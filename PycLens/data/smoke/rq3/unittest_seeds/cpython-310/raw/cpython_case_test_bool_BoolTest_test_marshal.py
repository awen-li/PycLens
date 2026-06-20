# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_marshal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import marshal
    self.assertIs(marshal.loads(marshal.dumps(True)), True)
    self.assertIs(marshal.loads(marshal.dumps(False)), False)
