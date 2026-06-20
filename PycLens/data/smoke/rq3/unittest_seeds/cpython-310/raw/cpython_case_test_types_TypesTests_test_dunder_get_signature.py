# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_dunder_get_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sig = inspect.signature(object.__init__.__get__)
    self.assertEqual(list(sig.parameters), ['instance', 'owner'])
    self.assertIs(sig.parameters['owner'].default, None)
