# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getdoc

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(inspect.getdoc(mod), 'A module docstring.')
    self.assertEqual(inspect.getdoc(mod.StupidGit), 'A longer,\n\nindented\n\ndocstring.')
    self.assertEqual(inspect.getdoc(git.abuse), 'Another\n\ndocstring\n\ncontaining\n\ntabs')
    self.assertEqual(inspect.getdoc(SlotUser.power), 'measured in kilowatts')
    self.assertEqual(inspect.getdoc(SlotUser.distance), 'measured in kilometers')
