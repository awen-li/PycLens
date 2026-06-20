# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_unpack_iter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (a, b) = (1, 2)
    self.assertEqual((a, b), (1, 2))
    (a, b, c) = IteratingSequenceClass(3)
    self.assertEqual((a, b, c), (0, 1, 2))
    try:
        (a, b) = IteratingSequenceClass(3)
    except ValueError:
        pass
    else:
        self.fail('should have raised ValueError')
    try:
        (a, b, c) = IteratingSequenceClass(2)
    except ValueError:
        pass
    else:
        self.fail('should have raised ValueError')
    try:
        (a, b, c) = len
    except TypeError:
        pass
    else:
        self.fail('should have raised TypeError')
    (a, b, c) = {1: 42, 2: 42, 3: 42}.values()
    self.assertEqual((a, b, c), (42, 42, 42))
    f = open(TESTFN, 'w', encoding='utf-8')
    lines = ('a\n', 'bb\n', 'ccc\n')
    try:
        for line in lines:
            f.write(line)
    finally:
        f.close()
    f = open(TESTFN, 'r', encoding='utf-8')
    try:
        (a, b, c) = f
        self.assertEqual((a, b, c), lines)
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
    ((a, b), (c,)) = (IteratingSequenceClass(2), {42: 24})
    self.assertEqual((a, b, c), (0, 1, 42))
