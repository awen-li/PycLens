# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_descr.py
# case: ClassPropertiesAndMethods_test_carloverre

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        object.__setattr__(str, 'foo', 42)
    except TypeError:
        pass
    else:
        self.fail('Carlo Verre __setattr__ succeeded!')
    try:
        object.__delattr__(str, 'lower')
    except TypeError:
        pass
    else:
        self.fail('Carlo Verre __delattr__ succeeded!')
