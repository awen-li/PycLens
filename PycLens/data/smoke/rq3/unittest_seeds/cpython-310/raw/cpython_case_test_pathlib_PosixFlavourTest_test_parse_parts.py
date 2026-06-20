# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pathlib.py
# case: PosixFlavourTest_test_parse_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self._check_parse_parts
    check(['//a', 'b'], ('', '//', ['//', 'a', 'b']))
    check(['///a', 'b'], ('', '/', ['/', 'a', 'b']))
    check(['////a', 'b'], ('', '/', ['/', 'a', 'b']))
    check(['c:a'], ('', '', ['c:a']))
    check(['c:\\a'], ('', '', ['c:\\a']))
    check(['\\a'], ('', '', ['\\a']))
