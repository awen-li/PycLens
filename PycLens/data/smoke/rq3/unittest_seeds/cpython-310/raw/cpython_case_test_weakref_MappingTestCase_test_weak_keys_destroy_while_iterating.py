# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: MappingTestCase_test_weak_keys_destroy_while_iterating

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (dict, objects) = self.make_weak_keyed_dict()
    self.check_weak_destroy_while_iterating(dict, objects, 'keys')
    self.check_weak_destroy_while_iterating(dict, objects, 'items')
    self.check_weak_destroy_while_iterating(dict, objects, 'values')
    self.check_weak_destroy_while_iterating(dict, objects, 'keyrefs')
    (dict, objects) = self.make_weak_keyed_dict()

    @contextlib.contextmanager
    def testcontext():
        try:
            it = iter(dict.items())
            next(it)
            v = objects.pop().arg
            gc.collect()
            yield (Object(v), v)
        finally:
            it = None
            gc.collect()
    self.check_weak_destroy_and_mutate_while_iterating(dict, testcontext)
    (dict, objects) = self.make_weak_keyed_dict()
    self.check_weak_del_and_len_while_iterating(dict, testcontext)
