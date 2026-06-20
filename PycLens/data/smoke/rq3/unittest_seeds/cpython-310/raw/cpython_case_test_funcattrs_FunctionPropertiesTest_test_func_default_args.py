# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_funcattrs.py
# case: FunctionPropertiesTest_test_func_default_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def first_func(a, b):
        return a + b

    def second_func(a=1, b=2):
        return a + b
    self.assertEqual(first_func.__defaults__, None)
    self.assertEqual(second_func.__defaults__, (1, 2))
    first_func.__defaults__ = (1, 2)
    self.assertEqual(first_func.__defaults__, (1, 2))
    self.assertEqual(first_func(), 3)
    self.assertEqual(first_func(3), 5)
    self.assertEqual(first_func(3, 5), 8)
    del second_func.__defaults__
    self.assertEqual(second_func.__defaults__, None)
    try:
        second_func()
    except TypeError:
        pass
    else:
        self.fail('__defaults__ does not update; deleting it does not remove requirement')
