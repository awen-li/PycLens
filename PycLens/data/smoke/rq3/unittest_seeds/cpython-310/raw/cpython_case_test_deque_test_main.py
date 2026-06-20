# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    import sys
    test_classes = (TestBasic, TestVariousIteratorArgs, TestSubclass, TestSubclassWithKwargs, TestSequence)
    support.run_unittest(*test_classes)
    if verbose and hasattr(sys, 'gettotalrefcount'):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            support.run_unittest(*test_classes)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)
    from test import test_deque
    support.run_doctest(test_deque, verbose)
