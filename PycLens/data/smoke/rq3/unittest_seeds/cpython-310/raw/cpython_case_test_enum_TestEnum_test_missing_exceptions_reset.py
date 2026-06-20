# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_missing_exceptions_reset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import weakref

    class TestEnum(enum.Enum):
        VAL1 = 'val1'
        VAL2 = 'val2'

    class Class1:

        def __init__(self):
            try:
                raise ValueError()
            except ValueError:
                pass

    class Class2:

        def __init__(self):
            try:
                TestEnum('invalid_value')
            except ValueError:
                pass
    class_1_ref = weakref.ref(Class1())
    class_2_ref = weakref.ref(Class2())
    self.assertIs(class_1_ref(), None)
    self.assertIs(class_2_ref(), None)
