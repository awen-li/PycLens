# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_startupinfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    STARTF_USESHOWWINDOW = 1
    SW_MAXIMIZE = 3
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags = STARTF_USESHOWWINDOW
    startupinfo.wShowWindow = SW_MAXIMIZE
    subprocess.call(ZERO_RETURN_CMD, startupinfo=startupinfo)
