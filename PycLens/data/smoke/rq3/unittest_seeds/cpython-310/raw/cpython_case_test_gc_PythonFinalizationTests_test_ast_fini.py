# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: PythonFinalizationTests_test_ast_fini

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = textwrap.dedent('\n            import ast\n            import codecs\n\n            # Small AST tree to keep their AST types alive\n            tree = ast.parse("def f(x, y): return 2*x-y")\n            x = [tree]\n            x.append(x)\n\n            # Put the cycle somewhere to survive until the last GC collection.\n            # Codec search functions are only cleared at the end of\n            # interpreter_clear().\n            def search_func(encoding):\n                return None\n            search_func.a = x\n            codecs.register(search_func)\n        ')
    assert_python_ok('-c', code)
