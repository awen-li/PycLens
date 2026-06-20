# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestWraps_test_selective_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        pass
    f.attr = 'This is a different test'
    f.dict_attr = dict(a=1, b=2, c=3)

    def add_dict_attr(f):
        f.dict_attr = {}
        return f
    assign = ('attr',)
    update = ('dict_attr',)

    @functools.wraps(f, assign, update)
    @add_dict_attr
    def wrapper():
        pass
    self.check_wrapper(wrapper, f, assign, update)
    self.assertEqual(wrapper.__name__, 'wrapper')
    self.assertNotEqual(wrapper.__qualname__, f.__qualname__)
    self.assertEqual(wrapper.__doc__, None)
    self.assertEqual(wrapper.attr, 'This is a different test')
    self.assertEqual(wrapper.dict_attr, f.dict_attr)
