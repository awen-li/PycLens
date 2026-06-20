# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ordered_dict.py
# case: OrderedDictTests_test_issue24667

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    OrderedDict = self.OrderedDict
    od = OrderedDict()
    for c0 in '0123456789ABCDEF':
        for c1 in '0123456789ABCDEF':
            if len(od) == 4:
                od.popitem(last=False)
            key = c0 + c1
            od[key] = key
