# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_subprocess.py
# case: Win32ProcessTestCase_test_empty_handle_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.lpAttributeList = {'handle_list': []}
    subprocess.call(ZERO_RETURN_CMD, startupinfo=startupinfo)
