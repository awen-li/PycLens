# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_group

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, count, first, last, group) = self.server.group('fr.comp.lang.python')
    self.assertTrue(resp.startswith('211 '), resp)
    self.assertEqual(first, 761)
    self.assertEqual(last, 1265)
    self.assertEqual(count, 486)
    self.assertEqual(group, 'fr.comp.lang.python')
    with self.assertRaises(nntplib.NNTPTemporaryError) as cm:
        self.server.group('comp.lang.python.devel')
    exc = cm.exception
    self.assertTrue(exc.response.startswith('411 No such group'), exc.response)
