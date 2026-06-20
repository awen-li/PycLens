# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binascii.py
# case: BinASCIITest_test_empty_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    empty = self.type2test(b'')
    for func in all_functions:
        if func == 'crc_hqx':
            binascii.crc_hqx(empty, 0)
            continue
        f = getattr(binascii, func)
        try:
            f(empty)
        except Exception as err:
            self.fail('{}({!r}) raises {!r}'.format(func, empty, err))
