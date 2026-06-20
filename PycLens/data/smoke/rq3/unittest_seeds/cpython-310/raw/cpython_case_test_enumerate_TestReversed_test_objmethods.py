# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enumerate.py
# case: TestReversed_test_objmethods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NoLen(object):

        def __getitem__(self, i):
            return 1
    nl = NoLen()
    self.assertRaises(TypeError, reversed, nl)

    class NoGetItem(object):

        def __len__(self):
            return 2
    ngi = NoGetItem()
    self.assertRaises(TypeError, reversed, ngi)

    class Blocked(object):

        def __getitem__(self, i):
            return 1

        def __len__(self):
            return 2
        __reversed__ = None
    b = Blocked()
    self.assertRaises(TypeError, reversed, b)
