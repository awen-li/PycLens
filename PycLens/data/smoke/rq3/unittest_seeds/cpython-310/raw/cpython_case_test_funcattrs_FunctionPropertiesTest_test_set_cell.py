# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_set_cell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 12

    def f():
        return a
    c = f.__closure__
    c[0].cell_contents = 9
    self.assertEqual(c[0].cell_contents, 9)
    self.assertEqual(f(), 9)
    self.assertEqual(a, 9)
    del c[0].cell_contents
    try:
        c[0].cell_contents
    except ValueError:
        pass
    else:
        self.fail("shouldn't be able to read an empty cell")
    with self.assertRaises(NameError):
        f()
    with self.assertRaises(UnboundLocalError):
        print(a)
