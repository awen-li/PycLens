# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestUpdateWrapper_test_missing_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        pass

    def wrapper():
        pass
    wrapper.dict_attr = {}
    assign = ('attr',)
    update = ('dict_attr',)
    functools.update_wrapper(wrapper, f, assign, update)
    self.assertNotIn('attr', wrapper.__dict__)
    self.assertEqual(wrapper.dict_attr, {})
    del wrapper.dict_attr
    with self.assertRaises(AttributeError):
        functools.update_wrapper(wrapper, f, assign, update)
    wrapper.dict_attr = 1
    with self.assertRaises(AttributeError):
        functools.update_wrapper(wrapper, f, assign, update)
