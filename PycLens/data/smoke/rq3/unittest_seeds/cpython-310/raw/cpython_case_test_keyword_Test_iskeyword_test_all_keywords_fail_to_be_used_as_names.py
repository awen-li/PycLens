# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keyword.py
# case: Test_iskeyword_test_all_keywords_fail_to_be_used_as_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for key in keyword.kwlist:
        with self.assertRaises(SyntaxError):
            exec(f'{key} = 42')
