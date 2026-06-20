# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_gzip.py
# case: TestCommandLine_test_decompress_stdin_stdout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with io.BytesIO() as bytes_io:
        with gzip.GzipFile(fileobj=bytes_io, mode='wb') as gzip_file:
            gzip_file.write(self.data)
        args = (sys.executable, '-m', 'gzip', '-d')
        with Popen(args, stdin=PIPE, stdout=PIPE, stderr=PIPE) as proc:
            (out, err) = proc.communicate(bytes_io.getvalue())
    self.assertEqual(err, b'')
    self.assertEqual(out, self.data)
