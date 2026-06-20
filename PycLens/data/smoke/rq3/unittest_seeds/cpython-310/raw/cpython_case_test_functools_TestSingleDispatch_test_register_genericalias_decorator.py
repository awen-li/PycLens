# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_register_genericalias_decorator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def f(arg):
        return 'default'
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(list[int])
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.List[int])
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(list[int] | str)
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.List[int] | str)
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.Any)
