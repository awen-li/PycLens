# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ReplaceTests_test_replace_all

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    member = self.tar.getmember('ustar/regtype')
    for attr_name in ('name', 'mtime', 'mode', 'linkname', 'uid', 'gid', 'uname', 'gname'):
        with self.subTest(attr_name=attr_name):
            replaced = member.replace(**{attr_name: None})
            self.assertEqual(getattr(replaced, attr_name), None)
            self.assertNotEqual(getattr(member, attr_name), None)
