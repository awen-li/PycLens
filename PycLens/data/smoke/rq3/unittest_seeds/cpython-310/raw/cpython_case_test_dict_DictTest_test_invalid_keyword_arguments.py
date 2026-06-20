# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_invalid_keyword_arguments

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Custom(dict):
        pass
    for invalid in ({1: 2}, Custom({1: 2})):
        with self.assertRaises(TypeError):
            dict(**invalid)
        with self.assertRaises(TypeError):
            {}.update(**invalid)
