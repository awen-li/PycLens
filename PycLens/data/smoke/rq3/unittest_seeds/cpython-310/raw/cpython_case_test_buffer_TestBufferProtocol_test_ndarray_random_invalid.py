# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_buffer.py
# case: TestBufferProtocol_test_ndarray_random_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for _ in range(ITERATIONS):
        for fmt in fmtdict['@']:
            itemsize = struct.calcsize(fmt)
            t = rand_structure(itemsize, False, maxdim=MAXDIM, maxshape=MAXSHAPE)
            self.assertFalse(verify_structure(*t))
            items = randitems_from_structure(fmt, t)
            nderr = False
            try:
                x = ndarray_from_structure(items, fmt, t)
            except Exception as e:
                nderr = e.__class__
            self.assertTrue(nderr)
            if numpy_array:
                numpy_err = False
                try:
                    y = numpy_array_from_structure(items, fmt, t)
                except Exception as e:
                    numpy_err = e.__class__
                if 0:
                    self.assertTrue(numpy_err)
