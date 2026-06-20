# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_splittable_setattr_after_pop

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi

    class C:
        pass
    a = C()
    a.a = 1
    self.assertTrue(_testcapi.dict_hassplittable(a.__dict__))
    a.__dict__.pop('a')
    self.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a.a = 1
    self.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a = C()
    a.a = 2
    self.assertTrue(_testcapi.dict_hassplittable(a.__dict__))
    a.__dict__.popitem()
    self.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
    a.a = 3
    self.assertFalse(_testcapi.dict_hassplittable(a.__dict__))
