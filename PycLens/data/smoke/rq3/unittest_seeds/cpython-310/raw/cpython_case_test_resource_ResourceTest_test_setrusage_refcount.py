# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_resource.py
# case: ResourceTest_test_setrusage_refcount

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        limits = resource.getrlimit(resource.RLIMIT_CPU)
    except AttributeError:
        pass
    else:

        class BadSequence:

            def __len__(self):
                return 2

            def __getitem__(self, key):
                if key in (0, 1):
                    return len(tuple(range(1000000)))
                raise IndexError
        resource.setrlimit(resource.RLIMIT_CPU, BadSequence())
