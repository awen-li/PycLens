# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_for_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(gth(int), {})
    self.assertEqual(gth(type), {})
    self.assertEqual(gth(dir), {})
    self.assertEqual(gth(len), {})
    self.assertEqual(gth(object.__str__), {})
    self.assertEqual(gth(object().__str__), {})
    self.assertEqual(gth(str.join), {})
