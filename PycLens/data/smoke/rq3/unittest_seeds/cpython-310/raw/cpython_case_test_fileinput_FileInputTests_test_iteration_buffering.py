# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_iteration_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = LineReader()
    with FileInput(files=['line1\nline2', 'line3\n'], openhook=src.openhook) as fi:
        self.assertEqual(src.linesread, [])
        self.assertEqual(next(fi), 'line1\n')
        self.assertEqual(src.linesread, ['line1\n'])
        self.assertEqual(next(fi), 'line2')
        self.assertEqual(src.linesread, ['line2'])
        self.assertEqual(next(fi), 'line3\n')
        self.assertEqual(src.linesread, ['', 'line3\n'])
        self.assertRaises(StopIteration, next, fi)
        self.assertEqual(src.linesread, [''])
        self.assertRaises(StopIteration, next, fi)
        self.assertEqual(src.linesread, [])
