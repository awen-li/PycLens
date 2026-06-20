# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: _BaseFlavourTest_test_parse_parts_common

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self._check_parse_parts
    sep = self.flavour.sep
    check([], ('', '', []))
    check(['a'], ('', '', ['a']))
    check(['a/'], ('', '', ['a']))
    check(['a', 'b'], ('', '', ['a', 'b']))
    check(['a/b'], ('', '', ['a', 'b']))
    check(['a/b/'], ('', '', ['a', 'b']))
    check(['a', 'b/c', 'd'], ('', '', ['a', 'b', 'c', 'd']))
    check(['a', 'b//c', 'd'], ('', '', ['a', 'b', 'c', 'd']))
    check(['a', 'b/c/', 'd'], ('', '', ['a', 'b', 'c', 'd']))
    check(['.'], ('', '', []))
    check(['.', '.', 'b'], ('', '', ['b']))
    check(['a', '.', 'b'], ('', '', ['a', 'b']))
    check(['a', '.', '.'], ('', '', ['a']))
    check(['/a/b'], ('', sep, [sep, 'a', 'b']))
    check(['/a', 'b'], ('', sep, [sep, 'a', 'b']))
    check(['/a/', 'b'], ('', sep, [sep, 'a', 'b']))
    check(['a', '/b', 'c'], ('', sep, [sep, 'b', 'c']))
    check(['a', '/b', '/c'], ('', sep, [sep, 'c']))
