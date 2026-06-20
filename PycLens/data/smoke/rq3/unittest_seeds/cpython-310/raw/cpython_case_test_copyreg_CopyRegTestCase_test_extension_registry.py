# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_copyreg.py
# case: CopyRegTestCase_test_extension_registry

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (mod, func, code) = ('junk1 ', ' junk2', 43981)
    e = ExtensionSaver(code)
    try:
        self.assertRaises(ValueError, copyreg.remove_extension, mod, func, code)
        copyreg.add_extension(mod, func, code)
        self.assertTrue(copyreg._extension_registry[mod, func] == code)
        self.assertTrue(copyreg._inverted_registry[code] == (mod, func))
        self.assertNotIn(code, copyreg._extension_cache)
        copyreg.add_extension(mod, func, code)
        self.assertRaises(ValueError, copyreg.add_extension, mod, func, code + 1)
        self.assertRaises(ValueError, copyreg.remove_extension, mod, func, code + 1)
        self.assertRaises(ValueError, copyreg.add_extension, mod[1:], func, code)
        self.assertRaises(ValueError, copyreg.remove_extension, mod[1:], func, code)
        self.assertRaises(ValueError, copyreg.add_extension, mod, func[1:], code)
        self.assertRaises(ValueError, copyreg.remove_extension, mod, func[1:], code)
        if code + 1 not in copyreg._inverted_registry:
            self.assertRaises(ValueError, copyreg.remove_extension, mod[1:], func[1:], code + 1)
    finally:
        e.restore()
    self.assertNotIn((mod, func), copyreg._extension_registry)
    for code in (1, 2147483647):
        e = ExtensionSaver(code)
        try:
            copyreg.add_extension(mod, func, code)
            copyreg.remove_extension(mod, func, code)
        finally:
            e.restore()
    for code in (-1, 0, 2147483648):
        self.assertRaises(ValueError, copyreg.add_extension, mod, func, code)
