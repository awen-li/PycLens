# Source Generated with Decompyle++
# File: cpython-312-b7b1bc256f57.pyc (Python 3.12)


def __pybcsec_seed__():
    if None:
        pass
    self = None()
    __pybcsec_self__ = None()
    __pybcsec_self__ = self
    mcfiles = mailcap.listmailcapfiles()
    self.assertIsInstance(mcfiles, list)
    for m in mcfiles:
        self.assertIsInstance(m, str)
    env = os_helper.EnvironmentVarGuard()
    if 'MAILCAPS' in env:
        env_mailcaps = env['MAILCAPS'].split(os.pathsep)
    else:
        env_mailcaps = [
            '/testdir1/.mailcap',
            '/testdir2/mailcap']
        env['MAILCAPS'] = os.pathsep.join(env_mailcaps)
        mcfiles = mailcap.listmailcapfiles()
    None(None, None)
    None(self.assertEqual, mcfiles)
    return None
    if None:
        pass
    with None:
        if not None:
            pass
    continue

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
