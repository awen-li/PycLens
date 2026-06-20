# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_docstrings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    docstrings = ('"""simple doc string"""', '"""A more complex one\n            with some newlines"""', '"""Foo bar baz\n\n            empty newline"""', '"""With some \t"""', '"""Foo "bar" baz """', '"""\\r"""', '""""""', '"""\'\'\'"""', '"""\'\'\'\'\'\'"""', '"""🐍⛎𩸽üéş^\\\\X\\\\BB⟿"""', '"""end in single \'quote\'"""', '\'\'\'end in double "quote"\'\'\'', '"""almost end in double "quote"."""')
    for prefix in docstring_prefixes:
        for docstring in docstrings:
            self.check_src_roundtrip(f'{prefix}{docstring}')
