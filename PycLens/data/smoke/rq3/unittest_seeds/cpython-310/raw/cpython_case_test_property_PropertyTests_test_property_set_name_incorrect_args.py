# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_property.py
# case: PropertyTests_test_property_set_name_incorrect_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    p = property()
    for i in (0, 1, 3):
        with self.assertRaisesRegex(TypeError, f'^__set_name__\\(\\) takes 2 positional arguments but {i} were given$'):
            p.__set_name__(*[0] * i)
