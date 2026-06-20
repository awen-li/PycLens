# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: TestRandomSubclassing_test_random_subclass_with_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Subclass(random.Random):

        def __init__(self, newarg=None):
            random.Random.__init__(self)
    Subclass(newarg=1)
