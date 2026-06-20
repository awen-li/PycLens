# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: NTFlavourTest_test_parse_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self._check_parse_parts
    check(['c:'], ('c:', '', ['c:']))
    check(['c:/'], ('c:', '\\', ['c:\\']))
    check(['/'], ('', '\\', ['\\']))
    check(['c:a'], ('c:', '', ['c:', 'a']))
    check(['c:/a'], ('c:', '\\', ['c:\\', 'a']))
    check(['/a'], ('', '\\', ['\\', 'a']))
    check(['//a/b'], ('\\\\a\\b', '\\', ['\\\\a\\b\\']))
    check(['//a/b/'], ('\\\\a\\b', '\\', ['\\\\a\\b\\']))
    check(['//a/b/c'], ('\\\\a\\b', '\\', ['\\\\a\\b\\', 'c']))
    check(['a', 'Z:b', 'c'], ('Z:', '', ['Z:', 'b', 'c']))
    check(['a', 'Z:/b', 'c'], ('Z:', '\\', ['Z:\\', 'b', 'c']))
    check(['a', '//b/c', 'd'], ('\\\\b\\c', '\\', ['\\\\b\\c\\', 'd']))
    check(['a', 'Z://b//c/', 'd/'], ('Z:', '\\', ['Z:\\', 'b', 'c', 'd']))
    check(['a', '//b/c//', 'd'], ('\\\\b\\c', '\\', ['\\\\b\\c\\', 'd']))
    check(['//?/c:/'], ('\\\\?\\c:', '\\', ['\\\\?\\c:\\']))
    check(['//?/c:/a'], ('\\\\?\\c:', '\\', ['\\\\?\\c:\\', 'a']))
    check(['//?/c:/a', '/b'], ('\\\\?\\c:', '\\', ['\\\\?\\c:\\', 'b']))
    check(['//?/UNC/b/c'], ('\\\\?\\UNC\\b\\c', '\\', ['\\\\?\\UNC\\b\\c\\']))
    check(['//?/UNC/b/c/d'], ('\\\\?\\UNC\\b\\c', '\\', ['\\\\?\\UNC\\b\\c\\', 'd']))
    check(['a', '/b', 'c'], ('', '\\', ['\\', 'b', 'c']))
    check(['Z:/a', '/b', 'c'], ('Z:', '\\', ['Z:\\', 'b', 'c']))
    check(['//?/Z:/a', '/b', 'c'], ('\\\\?\\Z:', '\\', ['\\\\?\\Z:\\', 'b', 'c']))
