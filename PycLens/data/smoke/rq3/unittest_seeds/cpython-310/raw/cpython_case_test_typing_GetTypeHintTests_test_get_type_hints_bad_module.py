# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GetTypeHintTests_test_get_type_hints_bad_module

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadModule:
        pass
    BadModule.__module__ = 'bad'
    self.assertNotIn('bad', sys.modules)
    self.assertEqual(get_type_hints(BadModule), {})
