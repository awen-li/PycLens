# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: ClassCreationTests_test_metaclass_new_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class ModelBase(type):

        def __new__(cls, name, bases, attrs):
            super_new = super().__new__
            new_class = super_new(cls, name, bases, {})
            if name != 'Model':
                raise RuntimeWarning(f'name={name!r}')
            return new_class

    class Model(metaclass=ModelBase):
        pass
    with self.assertRaises(RuntimeWarning):
        type('SouthPonies', (Model,), {})
