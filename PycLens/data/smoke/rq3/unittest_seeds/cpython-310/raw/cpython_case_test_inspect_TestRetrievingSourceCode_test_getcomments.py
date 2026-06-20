# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getcomments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(inspect.getcomments(mod), '# line 1\n')
    self.assertEqual(inspect.getcomments(mod.StupidGit), '# line 20\n')
    self.assertEqual(inspect.getcomments(mod2.cls160), '# line 159\n')
    co = compile('x=1', '_non_existing_filename.py', 'exec')
    self.assertIsNone(inspect.getcomments(co))
    self.assertIsNone(inspect.getcomments(list))
