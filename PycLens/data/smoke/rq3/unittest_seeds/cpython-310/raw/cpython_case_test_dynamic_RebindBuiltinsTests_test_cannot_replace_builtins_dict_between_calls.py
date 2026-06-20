# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamic.py
# case: RebindBuiltinsTests_test_cannot_replace_builtins_dict_between_calls

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo():
        return len([1, 2, 3])
    self.configure_func(foo)
    self.assertEqual(foo(), 3)
    with swap_item(globals(), '__builtins__', {'len': lambda x: 7}):
        self.assertEqual(foo(), 3)
