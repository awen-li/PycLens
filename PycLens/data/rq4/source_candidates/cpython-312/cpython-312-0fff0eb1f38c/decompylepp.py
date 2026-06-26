# Source Generated with Decompyle++
# File: cpython-312-0fff0eb1f38c.pyc (Python 3.12)


def __pybcsec_seed__():
    with None:
        with self as __pybcsec_self__:
            ns = MockPosixNamespace(os_name = 'darwin', argv0 = 'python', ENV_PATH = '/linkfrom:/usr/bin', PREFIX = '/usr/local', real_executable = '/linkfrom/python')
            ns.add_known_xfile('/linkfrom/python')
            ns.add_known_xfile('/home/cpython/python')
            ns.add_known_link('/linkfrom/python', '/home/cpython/python')
            ns.add_known_xfile('/usr/local/bin/python')
            ns.add_known_file('/home/cpython/pybuilddir.txt', [
                'build/lib.macos-9.8'])
            ns.add_known_file('/home/cpython/Lib/os.py')
            ns.add_known_dir('/home/cpython/lib-dynload')
            expected = dict(executable = '/linkfrom/python', prefix = '/usr/local', exec_prefix = '/usr/local', base_executable = '/linkfrom/python', build_prefix = '/home/cpython', _is_python_build = 1, module_search_paths_set = 1, module_search_paths = [
                '/usr/local/lib/python98.zip',
                '/home/cpython/Lib',
                '/home/cpython/build/lib.macos-9.8'])
            actual = getpath(ns, expected)
            self.assertEqual(expected, actual)
            return None

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
