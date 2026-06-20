# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestSingleDispatch_test_register_genericalias_annotation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @functools.singledispatch
    def f(arg):
        return 'default'
    with self.assertRaisesRegex(TypeError, "Invalid annotation for 'arg'"):

        @f.register
        def _(arg: list[int]):
            return 'types.GenericAlias'
    with self.assertRaisesRegex(TypeError, "Invalid annotation for 'arg'"):

        @f.register
        def _(arg: typing.List[float]):
            return 'typing.GenericAlias'
    with self.assertRaisesRegex(TypeError, "Invalid annotation for 'arg'"):

        @f.register
        def _(arg: list[int] | str):
            return 'types.UnionType(types.GenericAlias)'
    with self.assertRaisesRegex(TypeError, "Invalid annotation for 'arg'"):

        @f.register
        def _(arg: typing.List[float] | bytes):
            return 'typing.Union[typing.GenericAlias]'
    with self.assertRaisesRegex(TypeError, "Invalid annotation for 'arg'"):

        @f.register
        def _(arg: typing.Any):
            return 'typing.Any'
    self.assertEqual(f([1]), 'default')
    self.assertEqual(f([1.0]), 'default')
    self.assertEqual(f(''), 'default')
    self.assertEqual(f(b''), 'default')
