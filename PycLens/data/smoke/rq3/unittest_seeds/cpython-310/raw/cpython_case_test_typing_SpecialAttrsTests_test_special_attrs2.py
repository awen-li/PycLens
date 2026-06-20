# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: SpecialAttrsTests_test_special_attrs2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fr = typing.ForwardRef('set[Any]')
    self.assertFalse(hasattr(fr, '__name__'))
    self.assertFalse(hasattr(fr, '__qualname__'))
    self.assertEqual(fr.__module__, 'typing')
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.assertRaises(TypeError):
            pickle.dumps(fr, proto)
    self.assertEqual(SpecialAttrsTests.TypeName.__name__, 'TypeName')
    self.assertEqual(SpecialAttrsTests.TypeName.__qualname__, 'SpecialAttrsTests.TypeName')
    self.assertEqual(SpecialAttrsTests.TypeName.__module__, __name__)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(SpecialAttrsTests.TypeName, proto)
        loaded = pickle.loads(s)
        self.assertIs(SpecialAttrsTests.TypeName, loaded)
    self.assertEqual(SpecialAttrsT.__name__, 'SpecialAttrsT')
    self.assertFalse(hasattr(SpecialAttrsT, '__qualname__'))
    self.assertEqual(SpecialAttrsT.__module__, __name__)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(SpecialAttrsT, proto)
        loaded = pickle.loads(s)
        self.assertIs(SpecialAttrsT, loaded)
    self.assertEqual(SpecialAttrsP.__name__, 'SpecialAttrsP')
    self.assertFalse(hasattr(SpecialAttrsP, '__qualname__'))
    self.assertEqual(SpecialAttrsP.__module__, __name__)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        s = pickle.dumps(SpecialAttrsP, proto)
        loaded = pickle.loads(s)
        self.assertIs(SpecialAttrsP, loaded)
