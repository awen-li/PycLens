# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getsourcefile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(normcase(inspect.getsourcefile(mod.spam)), modfile)
    self.assertEqual(normcase(inspect.getsourcefile(git.abuse)), modfile)
    fn = '_non_existing_filename_used_for_sourcefile_test.py'
    co = compile('x=1', fn, 'exec')
    self.assertEqual(inspect.getsourcefile(co), None)
    linecache.cache[co.co_filename] = (1, None, 'None', co.co_filename)
    try:
        self.assertEqual(normcase(inspect.getsourcefile(co)), fn)
    finally:
        del linecache.cache[co.co_filename]
