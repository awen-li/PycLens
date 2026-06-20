# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ConcatenateTests_test_var_substitution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T = TypeVar('T')
    P = ParamSpec('P')
    P2 = ParamSpec('P2')
    C = Concatenate[T, P]
    self.assertEqual(C[int, P2], Concatenate[int, P2])
    self.assertEqual(C[int, [str, float]], (int, str, float))
    self.assertEqual(C[int, []], (int,))
    self.assertEqual(C[int, Concatenate[str, P2]], Concatenate[int, str, P2])
    with self.assertRaises(TypeError):
        C[int, ...]
    C = Concatenate[int, P]
    self.assertEqual(C[P2], Concatenate[int, P2])
    self.assertEqual(C[[str, float]], (int, str, float))
    self.assertEqual(C[str, float], (int, str, float))
    self.assertEqual(C[[]], (int,))
    self.assertEqual(C[Concatenate[str, P2]], Concatenate[int, str, P2])
    with self.assertRaises(TypeError):
        C[...]
