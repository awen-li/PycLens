# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_zipfile.py
# case: TestPath_test_encoding_warnings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'import io, zipfile\nwith zipfile.ZipFile(io.BytesIO(), "w") as zf:\n    zf.filename = \'<test_encoding_warnings in memory zip file>\'\n    zf.writestr("path/file.txt", b"Spanish Inquisition")\n    root = zipfile.Path(zf)\n    (path,) = root.iterdir()\n    file_path = path.joinpath("file.txt")\n    unused = file_path.read_text()  # should warn\n    file_path.open("r").close()  # should warn\n'
    proc = assert_python_ok('-X', 'warn_default_encoding', '-c', code)
    warnings = proc.err.splitlines()
    self.assertEqual(len(warnings), 2, proc.err)
    self.assertRegex(warnings[0], b'^<string>:8: EncodingWarning:')
    self.assertRegex(warnings[1], b'^<string>:9: EncodingWarning:')
