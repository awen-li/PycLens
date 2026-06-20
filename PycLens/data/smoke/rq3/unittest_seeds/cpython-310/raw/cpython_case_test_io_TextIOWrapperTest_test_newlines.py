# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_newlines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    input_lines = ['unix\n', 'windows\r\n', 'os9\r', 'last\n', 'nonl']
    tests = [[None, ['unix\n', 'windows\n', 'os9\n', 'last\n', 'nonl']], ['', input_lines], ['\n', ['unix\n', 'windows\r\n', 'os9\rlast\n', 'nonl']], ['\r\n', ['unix\nwindows\r\n', 'os9\rlast\nnonl']], ['\r', ['unix\nwindows\r', '\nos9\r', 'last\nnonl']]]
    encodings = ('utf-8', 'latin-1', 'utf-16', 'utf-16-le', 'utf-16-be', 'utf-32', 'utf-32-le', 'utf-32-be')
    for encoding in encodings:
        data = bytes(''.join(input_lines).encode(encoding))
        for do_reads in (False, True):
            for bufsize in range(1, 10):
                for (newline, exp_lines) in tests:
                    bufio = self.BufferedReader(self.BytesIO(data), bufsize)
                    textio = self.TextIOWrapper(bufio, newline=newline, encoding=encoding)
                    if do_reads:
                        got_lines = []
                        while True:
                            c2 = textio.read(2)
                            if c2 == '':
                                break
                            self.assertEqual(len(c2), 2)
                            got_lines.append(c2 + textio.readline())
                    else:
                        got_lines = list(textio)
                    for (got_line, exp_line) in zip(got_lines, exp_lines):
                        self.assertEqual(got_line, exp_line)
                    self.assertEqual(len(got_lines), len(exp_lines))
