# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_embed.py
# case: EmbeddingTests_test_forced_io_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = dict(os.environ, PYTHONIOENCODING='utf-8:surrogateescape')
    (out, err) = self.run_embedded_interpreter('test_forced_io_encoding', env=env)
    if support.verbose > 1:
        print()
        print(out)
        print(err)
    expected_stream_encoding = 'utf-8'
    expected_errors = 'surrogateescape'
    expected_output = '\n'.join(['--- Use defaults ---', 'Expected encoding: default', 'Expected errors: default', 'stdin: {in_encoding}:{errors}', 'stdout: {out_encoding}:{errors}', 'stderr: {out_encoding}:backslashreplace', '--- Set errors only ---', 'Expected encoding: default', 'Expected errors: ignore', 'stdin: {in_encoding}:ignore', 'stdout: {out_encoding}:ignore', 'stderr: {out_encoding}:backslashreplace', '--- Set encoding only ---', 'Expected encoding: iso8859-1', 'Expected errors: default', 'stdin: iso8859-1:{errors}', 'stdout: iso8859-1:{errors}', 'stderr: iso8859-1:backslashreplace', '--- Set encoding and errors ---', 'Expected encoding: iso8859-1', 'Expected errors: replace', 'stdin: iso8859-1:replace', 'stdout: iso8859-1:replace', 'stderr: iso8859-1:backslashreplace'])
    expected_output = expected_output.format(in_encoding=expected_stream_encoding, out_encoding=expected_stream_encoding, errors=expected_errors)
    self.maxDiff = None
    self.assertEqual(out.strip(), expected_output)
