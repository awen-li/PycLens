# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_slice_multidim

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    shape_t = (2, 3, 5)
    ndim = len(shape_t)
    nitems = prod(shape_t)
    for shape in permutations(shape_t):
        (fmt, items, _) = randitems(nitems)
        itemsize = struct.calcsize(fmt)
        for flags in (0, ND_PIL):
            nd = ndarray(items, shape=shape, format=fmt, flags=flags)
            lst = carray(items, shape)
            for slices in rslices_ndim(ndim, shape):
                listerr = None
                try:
                    sliced = multislice(lst, slices)
                except Exception as e:
                    listerr = e.__class__
                nderr = None
                try:
                    ndsliced = nd[slices]
                except Exception as e:
                    nderr = e.__class__
                if nderr or listerr:
                    self.assertIs(nderr, listerr)
                else:
                    self.assertEqual(ndsliced.tolist(), sliced)
