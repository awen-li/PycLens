# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_highly_nested_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    deleted = []

    class MyOD(OrderedDict):

        def __del__(self):
            deleted.append(self.i)
    obj = None
    for i in range(100):
        obj = MyOD([(None, obj)])
        obj.i = i
    del obj
    support.gc_collect()
    self.assertEqual(deleted, list(reversed(range(100))))
