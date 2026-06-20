# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_object_set_item_single_instance_non_str_key

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Foo:
        pass
    f = Foo()
    f.__dict__[1] = 1
    f.a = 'a'
    self.assertEqual(f.__dict__, {1: 1, 'a': 'a'})
