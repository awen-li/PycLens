# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_custom_object_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test = self
    test.called = False

    class Custom(dict):

        def get(self, key, default=None):
            test.called = True
            super().get(key, default)

    class Foo(object):
        a = 3
    foo = Foo()
    foo.__dict__ = Custom()
    self.assertEqual(inspect.getattr_static(foo, 'a'), 3)
    self.assertFalse(test.called)
