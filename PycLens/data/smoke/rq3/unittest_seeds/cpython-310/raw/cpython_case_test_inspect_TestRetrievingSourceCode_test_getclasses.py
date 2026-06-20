# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestRetrievingSourceCode_test_getclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    classes = inspect.getmembers(mod, inspect.isclass)
    self.assertEqual(classes, [('FesteringGob', mod.FesteringGob), ('MalodorousPervert', mod.MalodorousPervert), ('ParrotDroppings', mod.ParrotDroppings), ('StupidGit', mod.StupidGit), ('Tit', mod.MalodorousPervert), ('WhichComments', mod.WhichComments)])
    tree = inspect.getclasstree([cls[1] for cls in classes])
    self.assertEqual(tree, [(object, ()), [(mod.ParrotDroppings, (object,)), [(mod.FesteringGob, (mod.MalodorousPervert, mod.ParrotDroppings))], (mod.StupidGit, (object,)), [(mod.MalodorousPervert, (mod.StupidGit,)), [(mod.FesteringGob, (mod.MalodorousPervert, mod.ParrotDroppings))]], (mod.WhichComments, (object,))]])
    tree = inspect.getclasstree([cls[1] for cls in classes], True)
    self.assertEqual(tree, [(object, ()), [(mod.ParrotDroppings, (object,)), (mod.StupidGit, (object,)), [(mod.MalodorousPervert, (mod.StupidGit,)), [(mod.FesteringGob, (mod.MalodorousPervert, mod.ParrotDroppings))]], (mod.WhichComments, (object,))]])
