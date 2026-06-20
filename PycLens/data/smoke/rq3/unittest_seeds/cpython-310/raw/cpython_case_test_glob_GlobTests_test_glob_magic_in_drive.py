# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_glob.py
# case: GlobTests_test_glob_magic_in_drive

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    eq = self.assertSequencesEqual_noorder
    eq(glob.glob('*:'), [])
    eq(glob.glob(b'*:'), [])
    eq(glob.glob('?:'), [])
    eq(glob.glob(b'?:'), [])
    eq(glob.glob('\\\\?\\c:\\'), ['\\\\?\\c:\\'])
    eq(glob.glob(b'\\\\?\\c:\\'), [b'\\\\?\\c:\\'])
    eq(glob.glob('\\\\*\\*\\'), [])
    eq(glob.glob(b'\\\\*\\*\\'), [])
