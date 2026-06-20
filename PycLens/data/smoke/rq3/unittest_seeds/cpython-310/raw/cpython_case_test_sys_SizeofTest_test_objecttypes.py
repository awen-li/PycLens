# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_objecttypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    calcsize = struct.calcsize
    size = test.support.calcobjsize
    vsize = test.support.calcvobjsize
    check = self.check_sizeof
    check(True, vsize('') + self.longdigit)
    check(len, size('5P'))
    samples = [b'', b'u' * 100000]
    for sample in samples:
        x = bytearray(sample)
        check(x, vsize('n2Pi') + x.__alloc__())
    check(iter(bytearray()), size('nP'))
    check(b'', vsize('n') + 1)
    check(b'x' * 10, vsize('n') + 11)

    def get_cell():
        x = 42

        def inner():
            return x
        return inner
    check(get_cell().__closure__[0], size('P'))

    def check_code_size(a, expected_size):
        self.assertGreaterEqual(sys.getsizeof(a), expected_size)
    check_code_size(get_cell().__code__, size('6i13P'))
    check_code_size(get_cell.__code__, size('6i13P'))

    def get_cell2(x):

        def inner():
            return x
        return inner
    check_code_size(get_cell2.__code__, size('6i13P') + calcsize('n'))
    check(complex(0, 1), size('2d'))
    check(str.lower, size('3PPP'))
    import datetime
    check(datetime.timedelta.days, size('3PP'))
    import collections
    check(collections.defaultdict.default_factory, size('3PP'))
    check(int.__add__, size('3P2P'))
    check({}.__iter__, size('2P'))
    check({}, size('nQ2P'))
    check({'a': 1}, size('nQ2P') + calcsize('2nP2n') + 8 + 8 * 2 // 3 * calcsize('n2P'))
    longdict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8}
    check(longdict, size('nQ2P') + calcsize('2nP2n') + 16 + 16 * 2 // 3 * calcsize('n2P'))
    check({}.keys(), size('P'))
    check({}.values(), size('P'))
    check({}.items(), size('P'))
    check(iter({}), size('P2nPn'))
    check(iter({}.keys()), size('P2nPn'))
    check(iter({}.values()), size('P2nPn'))
    check(iter({}.items()), size('P2nPn'))

    class C(object):
        pass
    check(C.__dict__, size('P'))
    check(BaseException(), size('5Pb'))
    check(UnicodeEncodeError('', '', 0, 0, ''), size('5Pb 2P2nP'))
    check(UnicodeDecodeError('', b'', 0, 0, ''), size('5Pb 2P2nP'))
    check(UnicodeTranslateError('', 0, 1, ''), size('5Pb 2P2nP'))
    check(Ellipsis, size(''))
    import codecs, encodings.iso8859_3
    x = codecs.charmap_build(encodings.iso8859_3.decoding_table)
    check(x, size('32B2iB'))
    check(enumerate([]), size('n3P'))
    check(reversed(''), size('nP'))
    check(float(0), size('d'))
    check(sys.float_info, vsize('') + self.P * len(sys.float_info))
    import inspect
    CO_MAXBLOCKS = 20
    x = inspect.currentframe()
    ncells = len(x.f_code.co_cellvars)
    nfrees = len(x.f_code.co_freevars)
    extras = x.f_code.co_stacksize + x.f_code.co_nlocals + ncells + nfrees - 1
    check(x, vsize('4Pi2c4P3ic' + CO_MAXBLOCKS * '3i' + 'P' + extras * 'P'))

    def func():
        pass
    check(func, size('14P'))

    class c:

        @staticmethod
        def foo():
            pass

        @classmethod
        def bar(cls):
            pass
        check(foo, size('PP'))
        check(bar, size('PP'))

    def get_gen():
        yield 1
    check(get_gen(), size('P2PPP4P'))
    check(iter('abc'), size('lP'))
    import re
    check(re.finditer('', ''), size('2P'))
    check(list([]), vsize('Pn'))
    check(list([1]), vsize('Pn') + 2 * self.P)
    check(list([1, 2]), vsize('Pn') + 2 * self.P)
    check(list([1, 2, 3]), vsize('Pn') + 4 * self.P)
    check(iter([]), size('lP'))
    check(reversed([]), size('nP'))
    check(0, vsize(''))
    check(1, vsize('') + self.longdigit)
    check(-1, vsize('') + self.longdigit)
    PyLong_BASE = 2 ** sys.int_info.bits_per_digit
    check(int(PyLong_BASE), vsize('') + 2 * self.longdigit)
    check(int(PyLong_BASE ** 2 - 1), vsize('') + 2 * self.longdigit)
    check(int(PyLong_BASE ** 2), vsize('') + 3 * self.longdigit)
    check(unittest, size('PnPPP'))
    check(None, size(''))
    check(NotImplemented, size(''))
    check(object(), size(''))

    class C(object):

        def getx(self):
            return self.__x

        def setx(self, value):
            self.__x = value

        def delx(self):
            del self.__x
        x = property(getx, setx, delx, '')
        check(x, size('5Pi'))
    check(iter(range(1)), size('4l'))
    check(reversed(''), size('nP'))
    check(range(1), size('4P'))
    check(range(66000), size('4P'))
    PySet_MINSIZE = 8
    samples = [[], range(10), range(50)]
    s = size('3nP' + PySet_MINSIZE * 'nP' + '2nP')
    for sample in samples:
        minused = len(sample)
        if minused == 0:
            tmp = 1
        minused = minused * 2
        newsize = PySet_MINSIZE
        while newsize <= minused:
            newsize = newsize << 1
        if newsize <= 8:
            check(set(sample), s)
            check(frozenset(sample), s)
        else:
            check(set(sample), s + newsize * calcsize('nP'))
            check(frozenset(sample), s + newsize * calcsize('nP'))
    check(iter(set()), size('P3n'))
    check(slice(0), size('3P'))
    check(super(int), size('3P'))
    check((), vsize(''))
    check((1, 2, 3), vsize('') + 3 * self.P)
    fmt = 'P2nPI13Pl4Pn9Pn11PIPP'
    s = vsize(fmt)
    check(int, s)
    s = vsize(fmt + '4P36P3P10P2P5P')

    class newstyleclass(object):
        pass
    check(newstyleclass, s + calcsize('2nP2n0P') + 8 + 5 * calcsize('n2P'))
    check(newstyleclass().__dict__, size('nQ2P') + 5 * self.P)
    o = newstyleclass()
    o.a = o.b = o.c = o.d = o.e = o.f = o.g = o.h = 1
    check(newstyleclass, s + calcsize('2nP2n0P') + 16 + 10 * calcsize('n2P'))
    check(newstyleclass().__dict__, size('nQ2P') + 10 * self.P)
    samples = ['1' * 100, 'ÿ' * 50, 'Ā' * 40, '\uffff' * 100, '𐀀' * 30, '\U0010ffff' * 100]
    asciifields = 'nnbP'
    compactfields = asciifields + 'nPn'
    unicodefields = compactfields + 'P'
    for s in samples:
        maxchar = ord(max(s))
        if maxchar < 128:
            L = size(asciifields) + len(s) + 1
        elif maxchar < 256:
            L = size(compactfields) + len(s) + 1
        elif maxchar < 65536:
            L = size(compactfields) + 2 * (len(s) + 1)
        else:
            L = size(compactfields) + 4 * (len(s) + 1)
        check(s, L)
    s = chr(16384)
    check(s, size(compactfields) + 4)
    compile(s, '<stdin>', 'eval')
    check(s, size(compactfields) + 4 + 4)
    import weakref
    check(weakref.ref(int), size('2Pn2P'))
    check(weakref.proxy(int), size('2Pn2P'))
