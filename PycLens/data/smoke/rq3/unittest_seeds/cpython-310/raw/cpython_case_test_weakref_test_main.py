# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    support.run_unittest(ReferencesTestCase, WeakMethodTestCase, MappingTestCase, WeakValueDictionaryTestCase, WeakKeyDictionaryTestCase, SubclassableWeakrefTestCase, FinalizeTestCase)
    support.run_doctest(sys.modules[__name__])
