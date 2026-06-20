# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_dict_contain_use_after_free

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class S(str):

        def __eq__(self, other):
            d.clear()
            return NotImplemented

        def __hash__(self):
            return hash('test')
    d = {S(): 'value'}
    self.assertFalse('test' in d)
