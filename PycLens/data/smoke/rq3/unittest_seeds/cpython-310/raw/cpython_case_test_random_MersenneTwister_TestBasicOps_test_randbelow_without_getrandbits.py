# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_random.py
# case: MersenneTwister_TestBasicOps_test_randbelow_without_getrandbits

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxsize = 1 << random.BPF
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', UserWarning)
        self.gen._randbelow_without_getrandbits(maxsize + 1, maxsize=maxsize)
    self.gen._randbelow_without_getrandbits(5640, maxsize=maxsize)
    x = self.gen._randbelow_without_getrandbits(0, maxsize=maxsize)
    self.assertEqual(x, 0)
    n = 42
    epsilon = 0.01
    limit = (maxsize - maxsize % n) / maxsize
    with unittest.mock.patch.object(random.Random, 'random') as random_mock:
        random_mock.side_effect = [limit + epsilon, limit - epsilon]
        self.gen._randbelow_without_getrandbits(n, maxsize=maxsize)
        self.assertEqual(random_mock.call_count, 2)
