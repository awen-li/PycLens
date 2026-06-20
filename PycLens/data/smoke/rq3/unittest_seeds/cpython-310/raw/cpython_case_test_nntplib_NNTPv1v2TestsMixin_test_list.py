# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, groups) = self.server.list()
    self.assertEqual(len(groups), 6)
    g = groups[1]
    self.assertEqual(g, GroupInfo('comp.lang.python.announce', '0000001153', '0000000993', 'm'))
    (resp, groups) = self.server.list('*distutils*')
    self.assertEqual(len(groups), 2)
    g = groups[0]
    self.assertEqual(g, GroupInfo('gmane.comp.python.distutils.devel', '0000014104', '0000000001', 'm'))
