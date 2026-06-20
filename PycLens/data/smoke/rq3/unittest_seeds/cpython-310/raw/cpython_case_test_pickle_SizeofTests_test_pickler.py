# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pickle.py
# case: SizeofTests_test_pickler

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    basesize = support.calcobjsize('7P2n3i2n3i2P')
    p = _pickle.Pickler(io.BytesIO())
    self.assertEqual(object.__sizeof__(p), basesize)
    MT_size = struct.calcsize('3nP0n')
    ME_size = struct.calcsize('Pn0P')
    check = self.check_sizeof
    check(p, basesize + MT_size + 8 * ME_size + sys.getsizeof(b'x' * 4096))
    for i in range(6):
        p.dump(chr(i))
    check(p, basesize + MT_size + 32 * ME_size + 0)
