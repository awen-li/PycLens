# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_modules_forwardref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mgc_hints = {'default_a': Optional[mod_generics_cache.A], 'default_b': Optional[mod_generics_cache.B]}
    self.assertEqual(gth(mod_generics_cache), mgc_hints)
