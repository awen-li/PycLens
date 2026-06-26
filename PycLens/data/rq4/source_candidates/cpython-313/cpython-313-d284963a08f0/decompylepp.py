# Source Generated with Decompyle++
# File: cpython-313-d284963a08f0.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    self.assertEqual(os.popen('exit 0').close(), None)
    status = os.popen('exit 42').close()
    if os.name == 'nt':
        self.assertEqual(status, 42)
    return None
    self.assertEqual(os.waitstatus_to_exitcode(status), 42)

if __name__ == '__main__':
    None()
return None
