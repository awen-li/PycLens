# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestCachedProperty_test_reuse_different_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(RuntimeError) as ctx:

        class ReusedCachedProperty:

            @py_functools.cached_property
            def a(self):
                pass
            b = a
    self.assertEqual(str(ctx.exception.__context__), str(TypeError("Cannot assign the same cached_property to two different names ('a' and 'b').")))
