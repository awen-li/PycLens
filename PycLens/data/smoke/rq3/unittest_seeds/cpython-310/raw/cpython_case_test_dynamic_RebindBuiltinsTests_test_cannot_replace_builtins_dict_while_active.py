# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamic.py
# case: RebindBuiltinsTests_test_cannot_replace_builtins_dict_while_active

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo():
        x = range(3)
        yield len(x)
        yield len(x)
    self.configure_func(foo)
    g = foo()
    self.assertEqual(next(g), 3)
    with swap_item(globals(), '__builtins__', {'len': lambda x: 7}):
        self.assertEqual(next(g), 3)
