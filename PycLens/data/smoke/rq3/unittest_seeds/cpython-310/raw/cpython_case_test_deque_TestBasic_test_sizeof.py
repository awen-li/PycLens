# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_sizeof

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BLOCKLEN = 64
    basesize = support.calcvobjsize('2P4nP')
    blocksize = struct.calcsize('P%dPP' % BLOCKLEN)
    self.assertEqual(object.__sizeof__(deque()), basesize)
    check = self.check_sizeof
    check(deque(), basesize + blocksize)
    check(deque('a'), basesize + blocksize)
    check(deque('a' * (BLOCKLEN - 1)), basesize + blocksize)
    check(deque('a' * BLOCKLEN), basesize + 2 * blocksize)
    check(deque('a' * (42 * BLOCKLEN)), basesize + 43 * blocksize)
