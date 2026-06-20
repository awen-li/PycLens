# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_collections.py
# case: TestCounter_test_copying

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    words = Counter('which witch had which witches wrist watch'.split())

    def check(dup):
        msg = '\ncopy: %s\nwords: %s' % (dup, words)
        self.assertIsNot(dup, words, msg)
        self.assertEqual(dup, words)
    check(words.copy())
    check(copy.copy(words))
    check(copy.deepcopy(words))
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        with self.subTest(proto=proto):
            check(pickle.loads(pickle.dumps(words, proto)))
    check(eval(repr(words)))
    update_test = Counter()
    update_test.update(words)
    check(update_test)
    check(Counter(words))
