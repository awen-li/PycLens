# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_escape_windows

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = self.check_escape
    check('?:?', '?:[?]')
    check('*:*', '*:[*]')
    check('\\\\?\\c:\\?', '\\\\?\\c:\\[?]')
    check('\\\\*\\*\\*', '\\\\*\\*\\[*]')
    check('//?/c:/?', '//?/c:/[?]')
    check('//*/*/*', '//*/*/[*]')
