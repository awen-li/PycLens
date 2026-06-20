# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_posix.py
# case: PosixTester_test_register_at_fork

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError, msg='Positional args not allowed'):
        os.register_at_fork(lambda : None)
    with self.assertRaises(TypeError, msg='Args must be callable'):
        os.register_at_fork(before=2)
    with self.assertRaises(TypeError, msg='Args must be callable'):
        os.register_at_fork(after_in_child='three')
    with self.assertRaises(TypeError, msg='Args must be callable'):
        os.register_at_fork(after_in_parent=b'Five')
    with self.assertRaises(TypeError, msg='Args must not be None'):
        os.register_at_fork(before=None)
    with self.assertRaises(TypeError, msg='Args must not be None'):
        os.register_at_fork(after_in_child=None)
    with self.assertRaises(TypeError, msg='Args must not be None'):
        os.register_at_fork(after_in_parent=None)
    with self.assertRaises(TypeError, msg='Invalid arg was allowed'):
        os.register_at_fork(before=None, after_in_parent=lambda : 3)
    with self.assertRaises(TypeError, msg='Invalid arg was allowed'):
        os.register_at_fork(before=lambda : None, after_in_child='')
    code = 'if 1:\n            import os\n\n            r, w = os.pipe()\n            fin_r, fin_w = os.pipe()\n\n            os.register_at_fork(before=lambda: os.write(w, b\'A\'))\n            os.register_at_fork(after_in_parent=lambda: os.write(w, b\'C\'))\n            os.register_at_fork(after_in_child=lambda: os.write(w, b\'E\'))\n            os.register_at_fork(before=lambda: os.write(w, b\'B\'),\n                                after_in_parent=lambda: os.write(w, b\'D\'),\n                                after_in_child=lambda: os.write(w, b\'F\'))\n\n            pid = os.fork()\n            if pid == 0:\n                # At this point, after-forkers have already been executed\n                os.close(w)\n                # Wait for parent to tell us to exit\n                os.read(fin_r, 1)\n                os._exit(0)\n            else:\n                try:\n                    os.close(w)\n                    with open(r, "rb") as f:\n                        data = f.read()\n                        assert len(data) == 6, data\n                        # Check before-fork callbacks\n                        assert data[:2] == b\'BA\', data\n                        # Check after-fork callbacks\n                        assert sorted(data[2:]) == list(b\'CDEF\'), data\n                        assert data.index(b\'C\') < data.index(b\'D\'), data\n                        assert data.index(b\'E\') < data.index(b\'F\'), data\n                finally:\n                    os.write(fin_w, b\'!\')\n            '
    assert_python_ok('-c', code)
