# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_monotonicity

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Boat(object):
        pass

    class DayBoat(Boat):
        pass

    class WheelBoat(Boat):
        pass

    class EngineLess(DayBoat):
        pass

    class SmallMultihull(DayBoat):
        pass

    class PedalWheelBoat(EngineLess, WheelBoat):
        pass

    class SmallCatamaran(SmallMultihull):
        pass

    class Pedalo(PedalWheelBoat, SmallCatamaran):
        pass
    self.assertEqual(PedalWheelBoat.__mro__, (PedalWheelBoat, EngineLess, DayBoat, WheelBoat, Boat, object))
    self.assertEqual(SmallCatamaran.__mro__, (SmallCatamaran, SmallMultihull, DayBoat, Boat, object))
    self.assertEqual(Pedalo.__mro__, (Pedalo, PedalWheelBoat, EngineLess, SmallCatamaran, SmallMultihull, DayBoat, WheelBoat, Boat, object))
