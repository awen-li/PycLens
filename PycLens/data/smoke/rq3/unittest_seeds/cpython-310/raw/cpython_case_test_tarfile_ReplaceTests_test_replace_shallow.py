# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tarfile.py
# case: ReplaceTests_test_replace_shallow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    member = self.tar.getmember('pax/regtype1')
    replaced = member.replace(deep=False)
    replaced.pax_headers['gname'] = 'not-bar'
    self.assertEqual(member.pax_headers['gname'], 'not-bar')
    self.assertEqual(self.tar.getmember('pax/regtype1').pax_headers['gname'], 'not-bar')
