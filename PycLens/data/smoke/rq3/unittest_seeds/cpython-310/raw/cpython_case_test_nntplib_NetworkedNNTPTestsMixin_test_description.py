# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_description

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check_desc(desc):
        self.assertIsInstance(desc, str)
        self.assertNotIn(self.GROUP_NAME, desc)
    desc = self.server.description(self.GROUP_NAME)
    _check_desc(desc)
    self.assertIn(self.DESC, desc)
    desc = self.server.description(self.GROUP_PAT)
    _check_desc(desc)
    desc = self.server.description('zk.brrtt.baz')
    self.assertEqual(desc, '')
