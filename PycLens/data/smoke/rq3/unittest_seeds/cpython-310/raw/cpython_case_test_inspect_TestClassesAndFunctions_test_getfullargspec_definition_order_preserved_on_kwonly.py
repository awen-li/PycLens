# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestClassesAndFunctions_test_getfullargspec_definition_order_preserved_on_kwonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for fn in signatures_with_lexicographic_keyword_only_parameters():
        signature = inspect.getfullargspec(fn)
        l = list(signature.kwonlyargs)
        sorted_l = sorted(l)
        self.assertTrue(l)
        self.assertEqual(l, sorted_l)
    signature = inspect.getfullargspec(unsorted_keyword_only_parameters_fn)
    l = list(signature.kwonlyargs)
    self.assertEqual(l, unsorted_keyword_only_parameters)
