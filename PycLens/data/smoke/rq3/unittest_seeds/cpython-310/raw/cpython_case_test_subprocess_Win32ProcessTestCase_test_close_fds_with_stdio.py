# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_close_fds_with_stdio

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import msvcrt
    fds = os.pipe()
    self.addCleanup(os.close, fds[0])
    self.addCleanup(os.close, fds[1])
    handles = []
    for fd in fds:
        os.set_inheritable(fd, True)
        handles.append(msvcrt.get_osfhandle(fd))
    p = subprocess.Popen([sys.executable, '-c', 'import msvcrt; print(msvcrt.open_osfhandle({}, 0))'.format(handles[0])], stdout=subprocess.PIPE, close_fds=False)
    (stdout, stderr) = p.communicate()
    self.assertEqual(p.returncode, 0)
    int(stdout.strip())
    p = subprocess.Popen([sys.executable, '-c', 'import msvcrt; print(msvcrt.open_osfhandle({}, 0))'.format(handles[0])], stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)
    (stdout, stderr) = p.communicate()
    self.assertEqual(p.returncode, 1)
    self.assertIn(b'OSError', stderr)
    handle_list = []
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.lpAttributeList = {'handle_list': handle_list}
    p = subprocess.Popen([sys.executable, '-c', 'import msvcrt; print(msvcrt.open_osfhandle({}, 0))'.format(handles[0])], stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, close_fds=True)
    (stdout, stderr) = p.communicate()
    self.assertEqual(p.returncode, 1)
    self.assertIn(b'OSError', stderr)
    with warnings_helper.check_warnings(('.*overriding close_fds', RuntimeWarning)):
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.lpAttributeList = {'handle_list': handles[:]}
        p = subprocess.Popen([sys.executable, '-c', 'import msvcrt; print(msvcrt.open_osfhandle({}, 0))'.format(handles[0])], stdout=subprocess.PIPE, stderr=subprocess.PIPE, startupinfo=startupinfo, close_fds=False)
        (stdout, stderr) = p.communicate()
        self.assertEqual(p.returncode, 0)
