# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gc.py
# case: GCTests_test_is_tracked

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(gc.is_tracked(None))
    self.assertFalse(gc.is_tracked(1))
    self.assertFalse(gc.is_tracked(1.0))
    self.assertFalse(gc.is_tracked(1.0 + 5j))
    self.assertFalse(gc.is_tracked(True))
    self.assertFalse(gc.is_tracked(False))
    self.assertFalse(gc.is_tracked(b'a'))
    self.assertFalse(gc.is_tracked('a'))
    self.assertFalse(gc.is_tracked(bytearray(b'a')))
    self.assertFalse(gc.is_tracked(type))
    self.assertFalse(gc.is_tracked(int))
    self.assertFalse(gc.is_tracked(object))
    self.assertFalse(gc.is_tracked(object()))

    class UserClass:
        pass

    class UserInt(int):
        pass

    class UserClassSlots:
        __slots__ = ()

    class UserFloatSlots(float):
        __slots__ = ()

    class UserIntSlots(int):
        __slots__ = ()
    self.assertTrue(gc.is_tracked(gc))
    self.assertTrue(gc.is_tracked(UserClass))
    self.assertTrue(gc.is_tracked(UserClass()))
    self.assertTrue(gc.is_tracked(UserInt()))
    self.assertTrue(gc.is_tracked([]))
    self.assertTrue(gc.is_tracked(set()))
    self.assertTrue(gc.is_tracked(UserClassSlots()))
    self.assertTrue(gc.is_tracked(UserFloatSlots()))
    self.assertTrue(gc.is_tracked(UserIntSlots()))
