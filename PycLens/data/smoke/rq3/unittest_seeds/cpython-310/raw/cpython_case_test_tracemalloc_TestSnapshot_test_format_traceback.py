# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tracemalloc.py
# case: TestSnapshot_test_format_traceback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (snapshot, snapshot2) = create_snapshots()

    def getline(filename, lineno):
        return '  <%s, %s>' % (filename, lineno)
    with unittest.mock.patch('tracemalloc.linecache.getline', side_effect=getline):
        tb = snapshot.traces[0].traceback
        self.assertEqual(tb.format(), ['  File "b.py", line 4', '    <b.py, 4>', '  File "a.py", line 2', '    <a.py, 2>'])
        self.assertEqual(tb.format(limit=1), ['  File "a.py", line 2', '    <a.py, 2>'])
        self.assertEqual(tb.format(limit=-1), ['  File "b.py", line 4', '    <b.py, 4>'])
        self.assertEqual(tb.format(most_recent_first=True), ['  File "a.py", line 2', '    <a.py, 2>', '  File "b.py", line 4', '    <b.py, 4>'])
        self.assertEqual(tb.format(limit=1, most_recent_first=True), ['  File "a.py", line 2', '    <a.py, 2>'])
        self.assertEqual(tb.format(limit=-1, most_recent_first=True), ['  File "b.py", line 4', '    <b.py, 4>'])
