# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: SizeofTests_test_unpickler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('2P2n2P 2P2n2i5P 2P3n8P2n2i')
    unpickler = _pickle.Unpickler
    P = struct.calcsize('P')
    n = struct.calcsize('n')
    check = self.check_sizeof
    for encoding in ('ASCII', 'UTF-16', 'latin-1'):
        for errors in ('strict', 'replace'):
            u = unpickler(io.BytesIO(), encoding=encoding, errors=errors)
            self.assertEqual(object.__sizeof__(u), basesize)
            check(u, basesize + 32 * P + len(encoding) + 1 + len(errors) + 1)
    stdsize = basesize + len('ASCII') + 1 + len('strict') + 1

    def check_unpickler(data, memo_size, marks_size):
        dump = pickle.dumps(data)
        u = unpickler(io.BytesIO(dump), encoding='ASCII', errors='strict')
        u.load()
        check(u, stdsize + memo_size * P + marks_size * n)
    check_unpickler(0, 32, 0)
    check_unpickler([0] * 100, 32, 20)
    check_unpickler([chr(i) for i in range(100)], 128, 20)

    def recurse(deep):
        data = 0
        for i in range(deep):
            data = [data, data]
        return data
    check_unpickler(recurse(0), 32, 0)
    check_unpickler(recurse(1), 32, 20)
    check_unpickler(recurse(20), 32, 20)
    check_unpickler(recurse(50), 64, 60)
    check_unpickler(recurse(100), 128, 140)
    u = unpickler(io.BytesIO(pickle.dumps('a', 0)), encoding='ASCII', errors='strict')
    u.load()
    check(u, stdsize + 32 * P + 2 + 1)
