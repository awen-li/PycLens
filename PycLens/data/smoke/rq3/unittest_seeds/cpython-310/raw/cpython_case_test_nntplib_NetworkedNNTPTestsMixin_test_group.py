# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    result = self.server.group(self.GROUP_NAME)
    self.assertEqual(5, len(result))
    (resp, count, first, last, group) = result
    self.assertEqual(group, self.GROUP_NAME)
    self.assertIsInstance(count, int)
    self.assertIsInstance(first, int)
    self.assertIsInstance(last, int)
    self.assertLessEqual(first, last)
    self.assertTrue(resp.startswith('211 '), resp)
