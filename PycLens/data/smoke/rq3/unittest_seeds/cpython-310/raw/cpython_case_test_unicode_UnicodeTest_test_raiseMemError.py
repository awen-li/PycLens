# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_raiseMemError

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if struct.calcsize('P') == 8:
        ascii_struct_size = 48
        compact_struct_size = 72
    else:
        ascii_struct_size = 24
        compact_struct_size = 36
    for char in ('a', 'é', '€', '\U0010ffff'):
        code = ord(char)
        if code < 256:
            char_size = 1
            struct_size = ascii_struct_size
        elif code < 65536:
            char_size = 2
            struct_size = compact_struct_size
        else:
            char_size = 4
            struct_size = compact_struct_size
        maxlen = (sys.maxsize - struct_size) // char_size
        alloc = lambda : char * maxlen
        self.assertRaises(MemoryError, alloc)
        self.assertRaises(MemoryError, alloc)
