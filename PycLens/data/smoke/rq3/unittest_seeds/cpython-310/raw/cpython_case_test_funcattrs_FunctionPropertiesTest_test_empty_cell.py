# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_empty_cell

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        print(a)
    try:
        f.__closure__[0].cell_contents
    except ValueError:
        pass
    else:
        self.fail("shouldn't be able to read an empty cell")
    a = 12
