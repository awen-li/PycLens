# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: OSErrorTests_test_oserror_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    funcs = [(self.filenames, os.chdir), (self.filenames, os.chmod, 511), (self.filenames, os.lstat), (self.filenames, os.open, os.O_RDONLY), (self.filenames, os.rmdir), (self.filenames, os.stat), (self.filenames, os.unlink)]
    if sys.platform == 'win32':
        funcs.extend(((self.bytes_filenames, os.rename, b'dst'), (self.bytes_filenames, os.replace, b'dst'), (self.unicode_filenames, os.rename, 'dst'), (self.unicode_filenames, os.replace, 'dst'), (self.unicode_filenames, os.listdir)))
    else:
        funcs.extend(((self.filenames, os.listdir), (self.filenames, os.rename, 'dst'), (self.filenames, os.replace, 'dst')))
    if hasattr(os, 'chown'):
        funcs.append((self.filenames, os.chown, 0, 0))
    if hasattr(os, 'lchown'):
        funcs.append((self.filenames, os.lchown, 0, 0))
    if hasattr(os, 'truncate'):
        funcs.append((self.filenames, os.truncate, 0))
    if hasattr(os, 'chflags'):
        funcs.append((self.filenames, os.chflags, 0))
    if hasattr(os, 'lchflags'):
        funcs.append((self.filenames, os.lchflags, 0))
    if hasattr(os, 'chroot'):
        funcs.append((self.filenames, os.chroot))
    if hasattr(os, 'link'):
        if sys.platform == 'win32':
            funcs.append((self.bytes_filenames, os.link, b'dst'))
            funcs.append((self.unicode_filenames, os.link, 'dst'))
        else:
            funcs.append((self.filenames, os.link, 'dst'))
    if hasattr(os, 'listxattr'):
        funcs.extend(((self.filenames, os.listxattr), (self.filenames, os.getxattr, 'user.test'), (self.filenames, os.setxattr, 'user.test', b'user'), (self.filenames, os.removexattr, 'user.test')))
    if hasattr(os, 'lchmod'):
        funcs.append((self.filenames, os.lchmod, 511))
    if hasattr(os, 'readlink'):
        funcs.append((self.filenames, os.readlink))
    for (filenames, func, *func_args) in funcs:
        for name in filenames:
            try:
                if isinstance(name, (str, bytes)):
                    func(name, *func_args)
                else:
                    with self.assertWarnsRegex(DeprecationWarning, 'should be'):
                        func(name, *func_args)
            except OSError as err:
                self.assertIs(err.filename, name, str(func))
            except UnicodeDecodeError:
                pass
            else:
                self.fail('No exception thrown by {}'.format(func))
