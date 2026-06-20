# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_startupinfo_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = subprocess.SW_HIDE
    for _ in range(2):
        cmd = ZERO_RETURN_CMD
        with open(os.devnull, 'w') as null:
            proc = subprocess.Popen(cmd, stdout=null, stderr=subprocess.STDOUT, startupinfo=startupinfo)
            with proc:
                proc.communicate()
            self.assertEqual(proc.returncode, 0)
        self.assertEqual(startupinfo.dwFlags, subprocess.STARTF_USESHOWWINDOW)
        self.assertIsNone(startupinfo.hStdInput)
        self.assertIsNone(startupinfo.hStdOutput)
        self.assertIsNone(startupinfo.hStdError)
        self.assertEqual(startupinfo.wShowWindow, subprocess.SW_HIDE)
        self.assertEqual(startupinfo.lpAttributeList, {'handle_list': []})
