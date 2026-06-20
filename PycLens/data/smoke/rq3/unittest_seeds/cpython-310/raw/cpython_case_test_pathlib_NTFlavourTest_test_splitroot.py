# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: NTFlavourTest_test_splitroot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = self.flavour.splitroot
    self.assertEqual(f(''), ('', '', ''))
    self.assertEqual(f('a'), ('', '', 'a'))
    self.assertEqual(f('a\\b'), ('', '', 'a\\b'))
    self.assertEqual(f('\\a'), ('', '\\', 'a'))
    self.assertEqual(f('\\a\\b'), ('', '\\', 'a\\b'))
    self.assertEqual(f('c:a\\b'), ('c:', '', 'a\\b'))
    self.assertEqual(f('c:\\a\\b'), ('c:', '\\', 'a\\b'))
    self.assertEqual(f('\\\\a'), ('', '\\', 'a'))
    self.assertEqual(f('\\\\\\a/b'), ('', '\\', 'a/b'))
    self.assertEqual(f('c:\\\\a'), ('c:', '\\', 'a'))
    self.assertEqual(f('c:\\\\\\a/b'), ('c:', '\\', 'a/b'))
    self.assertEqual(f('\\\\a\\b'), ('\\\\a\\b', '\\', ''))
    self.assertEqual(f('\\\\a\\b\\'), ('\\\\a\\b', '\\', ''))
    self.assertEqual(f('\\\\a\\b\\c\\d'), ('\\\\a\\b', '\\', 'c\\d'))
    self.assertEqual(f('\\\\\\a\\b'), ('', '\\', 'a\\b'))
    self.assertEqual(f('\\\\a'), ('', '\\', 'a'))
