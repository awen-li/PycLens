# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    NamedTupleDocs = doctest.DocTestSuite(module=collections)
    test_classes = [TestNamedTuple, NamedTupleDocs, TestOneTrickPonyABCs, TestCollectionABCs, TestCounter, TestChainMap, TestUserObjects]
    support.run_unittest(*test_classes)
    support.run_doctest(collections, verbose)
