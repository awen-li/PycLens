# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: ProcessTestCase_test_nonexisting_with_pipes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import msvcrt
        msvcrt.CrtSetReportMode
    except (AttributeError, ImportError):
        self.skipTest('need msvcrt.CrtSetReportMode')
    code = textwrap.dedent(f'\n            import msvcrt\n            import subprocess\n\n            cmd = {NONEXISTING_CMD!r}\n\n            for report_type in [msvcrt.CRT_WARN,\n                                msvcrt.CRT_ERROR,\n                                msvcrt.CRT_ASSERT]:\n                msvcrt.CrtSetReportMode(report_type, msvcrt.CRTDBG_MODE_FILE)\n                msvcrt.CrtSetReportFile(report_type, msvcrt.CRTDBG_FILE_STDERR)\n\n            try:\n                subprocess.Popen(cmd,\n                                 stdout=subprocess.PIPE,\n                                 stderr=subprocess.PIPE)\n            except OSError:\n                pass\n        ')
    cmd = [sys.executable, '-c', code]
    proc = subprocess.Popen(cmd, stderr=subprocess.PIPE, universal_newlines=True)
    with proc:
        stderr = proc.communicate()[1]
    self.assertEqual(stderr, '')
    self.assertEqual(proc.returncode, 0)
