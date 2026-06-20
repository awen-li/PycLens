# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_warning_for_private_variables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertWarns(DeprecationWarning):

        class Private(Enum):
            __corporal = 'Radar'
    self.assertEqual(Private._Private__corporal.value, 'Radar')
    try:
        with self.assertWarns(DeprecationWarning):

            class Private(Enum):
                __major_ = 'Hoolihan'
    except ValueError:
        pass
