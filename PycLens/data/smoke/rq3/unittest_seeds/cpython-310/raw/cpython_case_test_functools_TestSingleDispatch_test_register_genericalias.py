# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_register_genericalias

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def f(arg):
        return 'default'
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(list[int], lambda arg: 'types.GenericAlias')
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.List[int], lambda arg: 'typing.GenericAlias')
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(list[int] | str, lambda arg: 'types.UnionTypes(types.GenericAlias)')
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.List[float] | bytes, lambda arg: 'typing.Union[typing.GenericAlias]')
    with self.assertRaisesRegex(TypeError, 'Invalid first argument to '):
        f.register(typing.Any, lambda arg: 'typing.Any')
    self.assertEqual(f([1]), 'default')
    self.assertEqual(f([1.0]), 'default')
    self.assertEqual(f(''), 'default')
    self.assertEqual(f(b''), 'default')
