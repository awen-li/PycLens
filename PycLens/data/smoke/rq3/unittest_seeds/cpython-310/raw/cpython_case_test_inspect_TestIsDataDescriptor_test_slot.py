# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestIsDataDescriptor_test_slot

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Slotted:
        __slots__ = ('foo',)
    self.assertTrue(inspect.isdatadescriptor(Slotted.foo), 'a slot is a data descriptor')
