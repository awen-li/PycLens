# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_random

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for _ in range(ITERATIONS):
        for fmt in fmtdict['@']:
            itemsize = struct.calcsize(fmt)
            t = rand_structure(itemsize, True, maxdim=MAXDIM, maxshape=MAXSHAPE)
            self.assertTrue(verify_structure(*t))
            items = randitems_from_structure(fmt, t)
            x = ndarray_from_structure(items, fmt, t)
            xlist = x.tolist()
            mv = memoryview(x)
            if is_memoryview_format(fmt):
                mvlist = mv.tolist()
                self.assertEqual(mvlist, xlist)
            if t[2] > 0:
                y = ndarray_from_structure(items, fmt, t, flags=ND_PIL)
                ylist = y.tolist()
                self.assertEqual(xlist, ylist)
                mv = memoryview(y)
                if is_memoryview_format(fmt):
                    self.assertEqual(mv, y)
                    mvlist = mv.tolist()
                    self.assertEqual(mvlist, ylist)
            if numpy_array:
                shape = t[3]
                if 0 in shape:
                    continue
                z = numpy_array_from_structure(items, fmt, t)
                self.verify(x, obj=None, itemsize=z.itemsize, fmt=fmt, readonly=False, ndim=z.ndim, shape=z.shape, strides=z.strides, lst=z.tolist())
