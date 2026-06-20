# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tokenize.py
# case: TestDetectEncoding_test_filename_in_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    path = 'some_file_path'
    lines = (b'print("\xdf")',)

    class Bunk:

        def __init__(self, lines, path):
            self.name = path
            self._lines = lines
            self._index = 0

        def readline(self):
            if self._index == len(lines):
                raise StopIteration
            line = lines[self._index]
            self._index += 1
            return line
    with self.assertRaises(SyntaxError):
        ins = Bunk(lines, path)
        del ins.name
        detect_encoding(ins.readline)
    with self.assertRaisesRegex(SyntaxError, '.*{}'.format(path)):
        ins = Bunk(lines, path)
        detect_encoding(ins.readline)
