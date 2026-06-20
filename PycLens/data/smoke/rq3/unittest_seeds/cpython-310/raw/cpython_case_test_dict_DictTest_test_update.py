# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_update

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {}
    d.update({1: 100})
    d.update({2: 20})
    d.update({1: 1, 2: 2, 3: 3})
    self.assertEqual(d, {1: 1, 2: 2, 3: 3})
    d.update()
    self.assertEqual(d, {1: 1, 2: 2, 3: 3})
    self.assertRaises((TypeError, AttributeError), d.update, None)

    class SimpleUserDict:

        def __init__(self):
            self.d = {1: 1, 2: 2, 3: 3}

        def keys(self):
            return self.d.keys()

        def __getitem__(self, i):
            return self.d[i]
    d.clear()
    d.update(SimpleUserDict())
    self.assertEqual(d, {1: 1, 2: 2, 3: 3})

    class Exc(Exception):
        pass
    d.clear()

    class FailingUserDict:

        def keys(self):
            raise Exc
    self.assertRaises(Exc, d.update, FailingUserDict())

    class FailingUserDict:

        def keys(self):

            class BogonIter:

                def __init__(self):
                    self.i = 1

                def __iter__(self):
                    return self

                def __next__(self):
                    if self.i:
                        self.i = 0
                        return 'a'
                    raise Exc
            return BogonIter()

        def __getitem__(self, key):
            return key
    self.assertRaises(Exc, d.update, FailingUserDict())

    class FailingUserDict:

        def keys(self):

            class BogonIter:

                def __init__(self):
                    self.i = ord('a')

                def __iter__(self):
                    return self

                def __next__(self):
                    if self.i <= ord('z'):
                        rtn = chr(self.i)
                        self.i += 1
                        return rtn
                    raise StopIteration
            return BogonIter()

        def __getitem__(self, key):
            raise Exc
    self.assertRaises(Exc, d.update, FailingUserDict())

    class badseq(object):

        def __iter__(self):
            return self

        def __next__(self):
            raise Exc()
    self.assertRaises(Exc, {}.update, badseq())
    self.assertRaises(ValueError, {}.update, [(1, 2, 3)])
