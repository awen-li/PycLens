# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomFDTests_test_urandom_fd_reopened

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    create_file(os_helper.TESTFN, b'x' * 256)
    code = "if 1:\n            import os\n            import sys\n            import test.support\n            os.urandom(4)\n            with test.support.SuppressCrashReport():\n                for fd in range(3, 256):\n                    try:\n                        os.close(fd)\n                    except OSError:\n                        pass\n                    else:\n                        # Found the urandom fd (XXX hopefully)\n                        break\n                os.closerange(3, 256)\n            with open({TESTFN!r}, 'rb') as f:\n                new_fd = f.fileno()\n                # Issue #26935: posix allows new_fd and fd to be equal but\n                # some libc implementations have dup2 return an error in this\n                # case.\n                if new_fd != fd:\n                    os.dup2(new_fd, fd)\n                sys.stdout.buffer.write(os.urandom(4))\n                sys.stdout.buffer.write(os.urandom(4))\n            ".format(TESTFN=os_helper.TESTFN)
    (rc, out, err) = assert_python_ok('-Sc', code)
    self.assertEqual(len(out), 8)
    self.assertNotEqual(out[0:4], out[4:8])
    (rc, out2, err2) = assert_python_ok('-Sc', code)
    self.assertEqual(len(out2), 8)
    self.assertNotEqual(out2, out)
