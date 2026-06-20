# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_conflicting_types_resolved_in_new

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class LabelledIntEnum(int, Enum):

        def __new__(cls, *args):
            (value, label) = args
            obj = int.__new__(cls, value)
            obj.label = label
            obj._value_ = value
            return obj

    class LabelledList(LabelledIntEnum):
        unprocessed = (1, 'Unprocessed')
        payment_complete = (2, 'Payment Complete')
    self.assertEqual(list(LabelledList), [LabelledList.unprocessed, LabelledList.payment_complete])
    self.assertEqual(LabelledList.unprocessed, 1)
    self.assertEqual(LabelledList(1), LabelledList.unprocessed)
