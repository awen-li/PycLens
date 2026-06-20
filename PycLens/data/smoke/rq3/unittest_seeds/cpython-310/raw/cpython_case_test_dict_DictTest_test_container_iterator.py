# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_container_iterator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C(object):
        pass
    views = (dict.items, dict.values, dict.keys)
    for v in views:
        obj = C()
        ref = weakref.ref(obj)
        container = {obj: 1}
        obj.v = v(container)
        obj.x = iter(obj.v)
        del obj, container
        gc.collect()
        self.assertIs(ref(), None, 'Cycle was not collected')
