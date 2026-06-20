# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ParamSpecTests_test_user_generics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')
    P_2 = ParamSpec('P_2')

    class X(Generic[T, P]):
        f: Callable[P, int]
        x: T
    G1 = X[int, P_2]
    self.assertEqual(G1.__args__, (int, P_2))
    self.assertEqual(G1.__parameters__, (P_2,))
    with self.assertRaisesRegex(TypeError, 'few arguments for'):
        X[int]
    with self.assertRaisesRegex(TypeError, 'many arguments for'):
        X[int, P_2, str]
    G2 = X[int, Concatenate[int, P_2]]
    self.assertEqual(G2.__args__, (int, Concatenate[int, P_2]))
    self.assertEqual(G2.__parameters__, (P_2,))
    G3 = X[int, [int, bool]]
    self.assertEqual(G3.__args__, (int, (int, bool)))
    self.assertEqual(G3.__parameters__, ())
    G4 = X[int, ...]
    self.assertEqual(G4.__args__, (int, Ellipsis))
    self.assertEqual(G4.__parameters__, ())

    class Z(Generic[P]):
        f: Callable[P, int]
    G5 = Z[[int, str, bool]]
    self.assertEqual(G5.__args__, ((int, str, bool),))
    self.assertEqual(G5.__parameters__, ())
    G6 = Z[int, str, bool]
    self.assertEqual(G6.__args__, ((int, str, bool),))
    self.assertEqual(G6.__parameters__, ())
    self.assertEqual(G5.__args__, G6.__args__)
    self.assertEqual(G5.__origin__, G6.__origin__)
    self.assertEqual(G5.__parameters__, G6.__parameters__)
    self.assertEqual(G5, G6)
    G7 = Z[int]
    self.assertEqual(G7.__args__, ((int,),))
    self.assertEqual(G7.__parameters__, ())
    with self.assertRaisesRegex(TypeError, 'many arguments for'):
        Z[[int, str], bool]
    with self.assertRaisesRegex(TypeError, 'many arguments for'):
        Z[P_2, bool]
