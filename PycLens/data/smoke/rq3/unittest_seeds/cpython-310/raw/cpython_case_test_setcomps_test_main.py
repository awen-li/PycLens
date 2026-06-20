# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_setcomps.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    import sys
    from test import support
    from test import test_setcomps
    support.run_doctest(test_setcomps, verbose)
    if verbose and hasattr(sys, 'gettotalrefcount'):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            support.run_doctest(test_setcomps, verbose)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)
