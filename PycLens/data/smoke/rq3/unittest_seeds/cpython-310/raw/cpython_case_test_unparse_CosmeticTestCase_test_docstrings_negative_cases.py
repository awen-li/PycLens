# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unparse.py
# case: CosmeticTestCase_test_docstrings_negative_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    docstrings_negative = ('a = """false"""', '"""false""" + """unless its optimized"""', '1 + 1\n"""false"""', 'f"""no, top level but f-fstring"""')
    for prefix in docstring_prefixes:
        for negative in docstrings_negative:
            src = f'{prefix}{negative}'
            self.check_ast_roundtrip(src)
            self.check_src_dont_roundtrip(src)
