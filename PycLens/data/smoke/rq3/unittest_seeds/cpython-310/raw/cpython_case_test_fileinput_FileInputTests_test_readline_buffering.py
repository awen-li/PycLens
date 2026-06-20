# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fileinput.py
# case: FileInputTests_test_readline_buffering

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    src = LineReader()
    with FileInput(files=['line1\nline2', 'line3\n'], openhook=src.openhook) as fi:
        self.assertEqual(src.linesread, [])
        self.assertEqual(fi.readline(), 'line1\n')
        self.assertEqual(src.linesread, ['line1\n'])
        self.assertEqual(fi.readline(), 'line2')
        self.assertEqual(src.linesread, ['line2'])
        self.assertEqual(fi.readline(), 'line3\n')
        self.assertEqual(src.linesread, ['', 'line3\n'])
        self.assertEqual(fi.readline(), '')
        self.assertEqual(src.linesread, [''])
        self.assertEqual(fi.readline(), '')
        self.assertEqual(src.linesread, [])
