# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: UtimeTests_test_issue31577

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def get_bad_int(divmod_ret_val):

        class BadInt:

            def __divmod__(*args):
                return divmod_ret_val
        return BadInt()
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=(get_bad_int(42), 1))
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=(get_bad_int(()), 1))
    with self.assertRaises(TypeError):
        os.utime(self.fname, ns=(get_bad_int((1, 2, 3)), 1))
