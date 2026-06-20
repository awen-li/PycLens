# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_3720

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadIterator(object):

        def __iter__(self):
            return self

        def __next__(self):
            del BadIterator.__next__
            return 1
    try:
        for i in BadIterator():
            pass
    except TypeError:
        pass
