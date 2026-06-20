# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_override_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict

    class MyOD(OrderedDict):

        def update(self, *args, **kwds):
            raise Exception()
    items = [('a', 1), ('c', 3), ('b', 2)]
    self.assertEqual(list(MyOD(items).items()), items)
