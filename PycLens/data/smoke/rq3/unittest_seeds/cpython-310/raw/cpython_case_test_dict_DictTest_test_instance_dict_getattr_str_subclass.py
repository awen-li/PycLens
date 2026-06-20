# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_instance_dict_getattr_str_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:

        def __init__(self, msg):
            self.msg = msg
    f = Foo('123')

    class _str(str):
        pass
    self.assertEqual(f.msg, getattr(f, _str('msg')))
    self.assertEqual(f.msg, f.__dict__[_str('msg')])
