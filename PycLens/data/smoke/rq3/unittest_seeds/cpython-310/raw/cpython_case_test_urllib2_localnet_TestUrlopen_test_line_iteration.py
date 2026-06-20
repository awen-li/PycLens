# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2_localnet.py
# case: TestUrlopen_test_line_iteration

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    lines = [b'We\n', b'got\n', b'here\n', b'verylong ' * 8192 + b'\n']
    expected_response = b''.join(lines)
    handler = self.start_server([(200, [], expected_response)])
    data = urllib.request.urlopen('http://localhost:%s' % handler.port)
    for (index, line) in enumerate(data):
        self.assertEqual(line, lines[index], "Fetched line number %s doesn't match expected:\n    Expected length was %s, got %s" % (index, len(lines[index]), len(line)))
    self.assertEqual(index + 1, len(lines))
