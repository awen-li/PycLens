# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: ForwardRefTests_test_name_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(a: 'Noode[T]'):
        pass
    with self.assertRaises(NameError):
        get_type_hints(foo, locals())
