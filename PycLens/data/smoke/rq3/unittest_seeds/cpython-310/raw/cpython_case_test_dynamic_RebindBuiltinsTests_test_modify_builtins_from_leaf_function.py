# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamic.py
# case: RebindBuiltinsTests_test_modify_builtins_from_leaf_function

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with swap_attr(builtins, 'len', len):

        def bar():
            builtins.len = lambda x: 4

        def foo(modifier):
            l = []
            l.append(len(range(7)))
            modifier()
            l.append(len(range(7)))
            return l
        self.configure_func(foo, lambda : None)
        self.assertEqual(foo(bar), [7, 4])
