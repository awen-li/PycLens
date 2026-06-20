# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sort.py
# case: TestDecorateSortUndecorate_test_decorated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'The quick Brown fox Jumped over The lazy Dog'.split()
    copy = data[:]
    random.shuffle(data)
    data.sort(key=str.lower)

    def my_cmp(x, y):
        (xlower, ylower) = (x.lower(), y.lower())
        return (xlower > ylower) - (xlower < ylower)
    copy.sort(key=cmp_to_key(my_cmp))
