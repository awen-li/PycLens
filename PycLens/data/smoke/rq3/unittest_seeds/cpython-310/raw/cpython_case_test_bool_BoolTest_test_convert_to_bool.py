# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bool.py
# case: BoolTest_test_convert_to_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    check = lambda o: self.assertRaises(TypeError, bool, o)

    class Foo(object):

        def __bool__(self):
            return self
    check(Foo())

    class Bar(object):

        def __bool__(self):
            return 'Yes'
    check(Bar())

    class Baz(int):

        def __bool__(self):
            return self
    check(Baz())

    class Spam(int):

        def __bool__(self):
            return 1
    check(Spam())

    class Eggs:

        def __len__(self):
            return -1
    self.assertRaises(ValueError, bool, Eggs())
