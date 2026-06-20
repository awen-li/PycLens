# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_big_dict_literal

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dict_size = 65535 + 1
    the_dict = '{' + ','.join((f'{x}:{x}' for x in range(dict_size))) + '}'
    self.assertEqual(len(eval(the_dict)), dict_size)
