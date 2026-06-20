# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_descriptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, descs) = self.server.descriptions(self.GROUP_PAT)
    self.assertTrue(resp.startswith('215 ') or resp.startswith('282 '), resp)
    self.assertIsInstance(descs, dict)
    desc = descs[self.GROUP_NAME]
    self.assertEqual(desc, self.server.description(self.GROUP_NAME))
