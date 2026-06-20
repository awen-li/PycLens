# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_wrapped_decoratored_func

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    expects = {'self': ForRefExample}
    self.assertEqual(gth(ForRefExample.func), expects)
    self.assertEqual(gth(ForRefExample.nested), expects)
