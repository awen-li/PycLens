# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ReplaceTests_test_replace_internal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    member = self.tar.getmember('ustar/regtype')
    with self.assertRaises(TypeError):
        member.replace(offset=123456789)
