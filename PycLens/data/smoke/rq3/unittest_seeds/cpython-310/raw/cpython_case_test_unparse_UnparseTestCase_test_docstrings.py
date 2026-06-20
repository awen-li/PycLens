# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: UnparseTestCase_test_docstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    docstrings = ('this ends with double quote"', 'this includes a """triple quote"""', '\r', '\\r', '\t', '\\t', '\n', '\\n', '\r\\r\t\\t\n\\n', '""">>> content = """blabla""" <<<"""', 'foo\\n\\x00', '\' \\\'\\\'\\\'""" ""\\\'\\\' \\\'', '🐍⛎𩸽üéş^\\\\X\\\\BB⟿')
    for docstring in docstrings:
        self.check_ast_roundtrip(f"'''{docstring}'''")
