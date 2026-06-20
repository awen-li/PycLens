# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_callbacks_protected

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BogusError(Exception):
        pass
    data = {}

    def remove(k):
        del data[k]

    def encapsulate():
        f = lambda : ()
        data[weakref.ref(f, remove)] = None
        raise BogusError
    try:
        encapsulate()
    except BogusError:
        pass
    else:
        self.fail('exception not properly restored')
    try:
        encapsulate()
    except BogusError:
        pass
    else:
        self.fail('exception not properly restored')
