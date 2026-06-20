# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_resize2

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class X(object):

        def __hash__(self):
            return 5

        def __eq__(self, other):
            if resizing:
                d.clear()
            return False
    d = {}
    resizing = False
    d[X()] = 1
    d[X()] = 2
    d[X()] = 3
    d[X()] = 4
    d[X()] = 5
    resizing = True
    d[9] = 6
