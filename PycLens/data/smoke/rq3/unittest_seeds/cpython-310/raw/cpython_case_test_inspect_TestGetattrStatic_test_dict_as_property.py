# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestGetattrStatic_test_dict_as_property

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test = self
    test.called = False

    class Foo(dict):
        a = 3

        @property
        def __dict__(self):
            test.called = True
            return {}
    foo = Foo()
    foo.a = 4
    self.assertEqual(inspect.getattr_static(foo, 'a'), 3)
    self.assertFalse(test.called)
