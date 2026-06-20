# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = open(TESTFN, 'w', encoding='utf-8')
    try:
        self.assertRaises(TypeError, f.writelines, None)
        self.assertRaises(TypeError, f.writelines, 42)
        f.writelines(['1\n', '2\n'])
        f.writelines(('3\n', '4\n'))
        f.writelines({'5\n': None})
        f.writelines({})

        class Iterator:

            def __init__(self, start, finish):
                self.start = start
                self.finish = finish
                self.i = self.start

            def __next__(self):
                if self.i >= self.finish:
                    raise StopIteration
                result = str(self.i) + '\n'
                self.i += 1
                return result

            def __iter__(self):
                return self

        class Whatever:

            def __init__(self, start, finish):
                self.start = start
                self.finish = finish

            def __iter__(self):
                return Iterator(self.start, self.finish)
        f.writelines(Whatever(6, 6 + 2000))
        f.close()
        f = open(TESTFN, encoding='utf-8')
        expected = [str(i) + '\n' for i in range(1, 2006)]
        self.assertEqual(list(f), expected)
    finally:
        f.close()
        try:
            unlink(TESTFN)
        except OSError:
            pass
