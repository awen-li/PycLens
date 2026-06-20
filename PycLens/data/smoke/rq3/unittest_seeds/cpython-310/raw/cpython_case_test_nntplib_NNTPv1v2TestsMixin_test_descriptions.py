# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_descriptions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, groups) = self.server.descriptions('comp.lang.python')
    self.assertEqual(resp, '215 Descriptions in form "group description".')
    self.assertEqual(groups, {'comp.lang.python': 'The Python computer language.'})
    (resp, groups) = self.server.descriptions('comp.lang.python*')
    self.assertEqual(groups, {'comp.lang.python': 'The Python computer language.', 'comp.lang.python.announce': 'Announcements about the Python language. (Moderated)'})
    (resp, groups) = self.server.descriptions('comp.lang.pythonx')
    self.assertEqual(groups, {})
