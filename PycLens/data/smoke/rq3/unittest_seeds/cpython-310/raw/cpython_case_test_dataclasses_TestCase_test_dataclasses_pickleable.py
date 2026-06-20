# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dataclasses.py
# case: TestCase_test_dataclasses_pickleable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    global P, Q, R

    @dataclass
    class P:
        x: int
        y: int = 0

    @dataclass
    class Q:
        x: int
        y: int = field(default=0, init=False)

    @dataclass
    class R:
        x: int
        y: List[int] = field(default_factory=list)
    q = Q(1)
    q.y = 2
    samples = [P(1), P(1, 2), Q(1), q, R(1), R(1, [2, 3, 4])]
    for sample in samples:
        for proto in range(pickle.HIGHEST_PROTOCOL + 1):
            with self.subTest(sample=sample, proto=proto):
                new_sample = pickle.loads(pickle.dumps(sample, proto))
                self.assertEqual(sample.x, new_sample.x)
                self.assertEqual(sample.y, new_sample.y)
                self.assertIsNot(sample, new_sample)
                new_sample.x = 42
                another_new_sample = pickle.loads(pickle.dumps(new_sample, proto))
                self.assertEqual(new_sample.x, another_new_sample.x)
                self.assertEqual(sample.y, another_new_sample.y)
