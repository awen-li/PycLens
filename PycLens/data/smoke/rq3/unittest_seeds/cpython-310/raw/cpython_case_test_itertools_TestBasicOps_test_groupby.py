# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_groupby

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual([], list(groupby([])))
    self.assertEqual([], list(groupby([], key=id)))
    self.assertRaises(TypeError, list, groupby('abc', []))
    self.assertRaises(TypeError, groupby, None)
    self.assertRaises(TypeError, groupby, 'abc', lambda x: x, 10)
    s = [(0, 10, 20), (0, 11, 21), (0, 12, 21), (1, 13, 21), (1, 14, 22), (2, 15, 22), (3, 16, 23), (3, 17, 23)]
    dup = []
    for (k, g) in groupby(s, lambda r: r[0]):
        for elem in g:
            self.assertEqual(k, elem[0])
            dup.append(elem)
    self.assertEqual(s, dup)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        dup = []
        for (k, g) in pickle.loads(pickle.dumps(groupby(s, testR), proto)):
            for elem in g:
                self.assertEqual(k, elem[0])
                dup.append(elem)
        self.assertEqual(s, dup)
    dup = []
    for (k, g) in groupby(s, testR):
        for (ik, ig) in groupby(g, testR2):
            for elem in ig:
                self.assertEqual(k, elem[0])
                self.assertEqual(ik, elem[2])
                dup.append(elem)
    self.assertEqual(s, dup)
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        dup = []
        for (k, g) in pickle.loads(pickle.dumps(groupby(s, testR), proto)):
            for (ik, ig) in pickle.loads(pickle.dumps(groupby(g, testR2), proto)):
                for elem in ig:
                    self.assertEqual(k, elem[0])
                    self.assertEqual(ik, elem[2])
                    dup.append(elem)
        self.assertEqual(s, dup)
    keys = [k for (k, g) in groupby(s, testR)]
    expectedkeys = set([r[0] for r in s])
    self.assertEqual(set(keys), expectedkeys)
    self.assertEqual(len(keys), len(expectedkeys))
    s = list(zip('AABBBAAAA', range(9)))
    it = groupby(s, testR)
    (_, g1) = next(it)
    (_, g2) = next(it)
    (_, g3) = next(it)
    self.assertEqual(list(g1), [])
    self.assertEqual(list(g2), [])
    self.assertEqual(next(g3), ('A', 5))
    list(it)
    self.assertEqual(list(g3), [])
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        it = groupby(s, testR)
        (_, g) = next(it)
        next(it)
        next(it)
        self.assertEqual(list(pickle.loads(pickle.dumps(g, proto))), [])
    s = 'abracadabra'
    r = [k for (k, g) in groupby(sorted(s))]
    self.assertEqual(r, ['a', 'b', 'c', 'd', 'r'])
    r = [k for (k, g) in groupby(sorted(s)) if list(islice(g, 1, 2))]
    self.assertEqual(r, ['a', 'b', 'r'])
    r = [(len(list(g)), k) for (k, g) in groupby(sorted(s))]
    self.assertEqual(r, [(5, 'a'), (2, 'b'), (1, 'c'), (1, 'd'), (2, 'r')])
    r = sorted([(len(list(g)), k) for (k, g) in groupby(sorted(s))], reverse=True)[:3]
    self.assertEqual(r, [(5, 'a'), (2, 'r'), (2, 'b')])

    class ExpectedError(Exception):
        pass

    def delayed_raise(n=0):
        for i in range(n):
            yield 'yo'
        raise ExpectedError

    def gulp(iterable, keyp=None, func=list):
        return [func(g) for (k, g) in groupby(iterable, keyp)]
    self.assertRaises(ExpectedError, gulp, delayed_raise(0))
    self.assertRaises(ExpectedError, gulp, delayed_raise(1))

    class DummyCmp:

        def __eq__(self, dst):
            raise ExpectedError
    s = [DummyCmp(), DummyCmp(), None]
    self.assertRaises(ExpectedError, gulp, s, func=id)
    self.assertRaises(ExpectedError, gulp, s)

    def keyfunc(obj):
        if keyfunc.skip > 0:
            keyfunc.skip -= 1
            return obj
        else:
            raise ExpectedError
    keyfunc.skip = 0
    self.assertRaises(ExpectedError, gulp, [None], keyfunc)
    keyfunc.skip = 1
    self.assertRaises(ExpectedError, gulp, [None, None], keyfunc)
