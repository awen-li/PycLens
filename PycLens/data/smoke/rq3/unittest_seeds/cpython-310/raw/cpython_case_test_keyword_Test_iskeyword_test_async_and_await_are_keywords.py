# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_keyword.py
# case: Test_iskeyword_test_async_and_await_are_keywords

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('async', keyword.kwlist)
    self.assertIn('await', keyword.kwlist)
