# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_genexps.py
# case: test_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    from test import support
    from test import test_genexps
    support.run_doctest(test_genexps, verbose)
    if verbose and hasattr(sys, 'gettotalrefcount'):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            support.run_doctest(test_genexps, verbose)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)
