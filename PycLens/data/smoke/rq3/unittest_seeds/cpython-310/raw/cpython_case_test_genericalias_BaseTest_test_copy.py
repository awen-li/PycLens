# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genericalias.py
# case: BaseTest_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(list):

        def __copy__(self):
            return self

        def __deepcopy__(self, memo):
            return self
    for origin in (list, deque, X):
        alias = GenericAlias(origin, T)
        copied = copy.copy(alias)
        self.assertEqual(copied.__origin__, alias.__origin__)
        self.assertEqual(copied.__args__, alias.__args__)
        self.assertEqual(copied.__parameters__, alias.__parameters__)
        copied = copy.deepcopy(alias)
        self.assertEqual(copied.__origin__, alias.__origin__)
        self.assertEqual(copied.__args__, alias.__args__)
        self.assertEqual(copied.__parameters__, alias.__parameters__)
