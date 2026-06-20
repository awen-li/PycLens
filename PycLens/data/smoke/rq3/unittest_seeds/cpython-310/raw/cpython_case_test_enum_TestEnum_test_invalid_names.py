# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_invalid_names

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(ValueError):

        class Wrong(Enum):
            mro = 9
    with self.assertRaises(ValueError):

        class Wrong(Enum):
            _create_ = 11
    with self.assertRaises(ValueError):

        class Wrong(Enum):
            _get_mixins_ = 9
    with self.assertRaises(ValueError):

        class Wrong(Enum):
            _find_new_ = 1
    with self.assertRaises(ValueError):

        class Wrong(Enum):
            _any_name_ = 9
