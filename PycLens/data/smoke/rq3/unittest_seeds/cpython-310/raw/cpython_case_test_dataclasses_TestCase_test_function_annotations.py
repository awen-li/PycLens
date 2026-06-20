# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_function_annotations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class F:
        pass
    f = F()

    def validate_class(cls):
        self.assertEqual(cls.__annotations__['i'], int)
        self.assertEqual(cls.__annotations__['j'], str)
        self.assertEqual(cls.__annotations__['k'], F)
        self.assertEqual(cls.__annotations__['l'], float)
        self.assertEqual(cls.__annotations__['z'], complex)
        signature = inspect.signature(cls.__init__)
        self.assertIs(signature.return_annotation, None)
        params = iter(signature.parameters.values())
        param = next(params)
        self.assertEqual(param.name, 'self')
        param = next(params)
        self.assertEqual(param.name, 'i')
        self.assertIs(param.annotation, int)
        self.assertEqual(param.default, inspect.Parameter.empty)
        self.assertEqual(param.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        param = next(params)
        self.assertEqual(param.name, 'j')
        self.assertIs(param.annotation, str)
        self.assertEqual(param.default, inspect.Parameter.empty)
        self.assertEqual(param.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        param = next(params)
        self.assertEqual(param.name, 'k')
        self.assertIs(param.annotation, F)
        self.assertEqual(param.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        param = next(params)
        self.assertEqual(param.name, 'l')
        self.assertIs(param.annotation, float)
        self.assertEqual(param.kind, inspect.Parameter.POSITIONAL_OR_KEYWORD)
        self.assertRaises(StopIteration, next, params)

    @dataclass
    class C:
        i: int
        j: str
        k: F = f
        l: float = field(default=None)
        z: complex = field(default=3 + 4j, init=False)
    validate_class(C)

    @dataclass(frozen=True, unsafe_hash=True)
    class C:
        i: int
        j: str
        k: F = f
        l: float = field(default=None)
        z: complex = field(default=3 + 4j, init=False)
    validate_class(C)
