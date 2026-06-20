# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_object_str_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Colors(Enum):
        (RED, GREEN, BLUE) = (1, 2, 3)

        def __repr__(self):
            return 'test.%s' % (self._name_,)
        __str__ = object.__str__
    self.assertEqual(str(Colors.RED), 'test.RED')
