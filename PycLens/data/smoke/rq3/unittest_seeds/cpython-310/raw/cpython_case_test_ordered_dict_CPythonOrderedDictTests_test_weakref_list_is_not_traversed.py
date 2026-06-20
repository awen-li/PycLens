# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: CPythonOrderedDictTests_test_weakref_list_is_not_traversed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gc.collect()
    x = self.OrderedDict()
    x.cycle = x
    cycle = []
    cycle.append(cycle)
    x_ref = weakref.ref(x)
    cycle.append(x_ref)
    del x, cycle, x_ref
    gc.collect()
