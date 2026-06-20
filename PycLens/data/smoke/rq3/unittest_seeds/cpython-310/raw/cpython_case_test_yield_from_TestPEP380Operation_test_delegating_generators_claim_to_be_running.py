# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_delegating_generators_claim_to_be_running

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def one():
        yield 0
        yield from two()
        yield 3

    def two():
        yield 1
        try:
            yield from g1
        except ValueError:
            pass
        yield 2
    g1 = one()
    self.assertEqual(list(g1), [0, 1, 2, 3])
    g1 = one()
    res = [next(g1)]
    try:
        while True:
            res.append(g1.send(42))
    except StopIteration:
        pass
    self.assertEqual(res, [0, 1, 2, 3])

    class MyErr(Exception):
        pass

    def one():
        try:
            yield 0
        except MyErr:
            pass
        yield from two()
        try:
            yield 3
        except MyErr:
            pass

    def two():
        try:
            yield 1
        except MyErr:
            pass
        try:
            yield from g1
        except ValueError:
            pass
        try:
            yield 2
        except MyErr:
            pass
    g1 = one()
    res = [next(g1)]
    try:
        while True:
            res.append(g1.throw(MyErr))
    except StopIteration:
        pass
    except:
        self.assertEqual(res, [0, 1, 2, 3])
        raise

    class MyIt(object):

        def __iter__(self):
            return self

        def __next__(self):
            return 42

        def close(self_):
            self.assertTrue(g1.gi_running)
            self.assertRaises(ValueError, next, g1)

    def one():
        yield from MyIt()
    g1 = one()
    next(g1)
    g1.close()
