# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import pickle
    mods = [pickle]
    try:
        import cPickle
        mods.append(cPickle)
    except ImportError:
        pass
    protocols = [0, 1, 2]
    for mod in mods:
        for protocol in protocols:
            for ast in (compile(i, '?', 'exec', 1024) for i in exec_tests):
                ast2 = mod.loads(mod.dumps(ast, protocol))
                self.assertEqual(to_tuple(ast2), to_tuple(ast))
