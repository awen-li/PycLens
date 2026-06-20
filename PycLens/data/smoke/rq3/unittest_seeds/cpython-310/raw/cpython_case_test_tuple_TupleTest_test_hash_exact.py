# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tuple.py
# case: TupleTest_test_hash_exact

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_one_exact(t, e32, e64):
        got = hash(t)
        expected = e32 if support.NHASHBITS == 32 else e64
        if got != expected:
            msg = f'FAIL hash({t!r}) == {got} != {expected}'
            self.fail(msg)
    check_one_exact((), 750394483, 5740354900026072187)
    check_one_exact((0,), 1214856301, -8753497827991233192)
    check_one_exact((0, 0), -168982784, -8458139203682520985)
    check_one_exact((0.5,), 2077348973, -408149959306781352)
    check_one_exact((0.5, (), (-2, 3, (4, 6))), 714642271, -1845940830829704396)
