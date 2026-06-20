# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_functools.py
# case: TestLRU_test_deepcopy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cls = self.__class__

    def orig(x, y):
        return 3 * x + y
    part = self.module.partial(orig, 2)
    funcs = (cls.cached_func[0], cls.cached_meth, cls.cached_staticmeth, self.module.lru_cache(2)(part))
    for f in funcs:
        with self.subTest(func=f):
            f_copy = copy.deepcopy(f)
            self.assertIs(f_copy, f)
