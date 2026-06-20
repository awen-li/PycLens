# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_newnews

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dt = datetime.datetime(2010, 9, 13, 8, 20, 4)
    (resp, ids) = self.server.newnews('comp.lang.python', dt)
    expected = '230 list of newsarticles (NNTP v{0}) created after Mon Sep 13 08:20:04 2010 follows'.format(self.nntp_version)
    self.assertEqual(resp, expected)
    self.assertEqual(ids, ['<a4929a40-6328-491a-aaaf-cb79ed7309a2@q2g2000vbk.googlegroups.com>', '<f30c0419-f549-4218-848f-d7d0131da931@y3g2000vbm.googlegroups.com>'])
    dt = datetime.datetime(2010, 9, 13, 8, 20, 4)
    (resp, ids) = self.server.newnews('fr.comp.lang.python', dt)
    self.assertEqual(resp, '230 An empty list of newsarticles follows')
    self.assertEqual(ids, [])
