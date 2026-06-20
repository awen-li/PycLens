# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_opcache.py
# case: TestLoadAttrCache_test_descriptor_added_after_optimization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Descriptor:
        pass

    class C:

        def __init__(self):
            self.x = 1
        x = Descriptor()

    def f(o):
        return o.x
    o = C()
    for i in range(1025):
        assert f(o) == 1
    Descriptor.__get__ = lambda self, instance, value: 2
    Descriptor.__set__ = lambda *args: None
    self.assertEqual(f(o), 2)
