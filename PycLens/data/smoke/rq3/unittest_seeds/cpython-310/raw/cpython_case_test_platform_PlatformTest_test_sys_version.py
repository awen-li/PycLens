# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_platform.py
# case: PlatformTest_test_sys_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (input, output) in (('2.4.3 (#1, Jun 21 2006, 13:54:21) \n[GCC 3.3.4 (pre 3.3.5 20040809)]', ('CPython', '2.4.3', '', '', '1', 'Jun 21 2006 13:54:21', 'GCC 3.3.4 (pre 3.3.5 20040809)')), ('IronPython 1.0.60816 on .NET 2.0.50727.42', ('IronPython', '1.0.60816', '', '', '', '', '.NET 2.0.50727.42')), ('IronPython 1.0 (1.0.61005.1977) on .NET 2.0.50727.42', ('IronPython', '1.0.0', '', '', '', '', '.NET 2.0.50727.42')), ('2.4.3 (truncation, date, t) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', 'date t', 'GCC')), ('2.4.3 (truncation, date, ) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', 'date', 'GCC')), ('2.4.3 (truncation, date,) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', 'date', 'GCC')), ('2.4.3 (truncation, date) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', 'date', 'GCC')), ('2.4.3 (truncation, d) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', 'd', 'GCC')), ('2.4.3 (truncation, ) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', '', 'GCC')), ('2.4.3 (truncation,) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', '', 'GCC')), ('2.4.3 (truncation) \n[GCC]', ('CPython', '2.4.3', '', '', 'truncation', '', 'GCC'))):
        (name, version, branch, revision, buildno, builddate, compiler) = platform._sys_version(input)
        self.assertEqual((name, version, '', '', buildno, builddate, compiler), output)
    sys_versions = {('2.6.1 (r261:67515, Dec  6 2008, 15:26:00) \n[GCC 4.0.1 (Apple Computer, Inc. build 5370)]', ('CPython', 'tags/r261', '67515'), self.save_platform): ('CPython', '2.6.1', 'tags/r261', '67515', ('r261:67515', 'Dec  6 2008 15:26:00'), 'GCC 4.0.1 (Apple Computer, Inc. build 5370)'), ('IronPython 2.0 (2.0.0.0) on .NET 2.0.50727.3053', None, 'cli'): ('IronPython', '2.0.0', '', '', ('', ''), '.NET 2.0.50727.3053'), ('2.6.1 (IronPython 2.6.1 (2.6.10920.0) on .NET 2.0.50727.1433)', None, 'cli'): ('IronPython', '2.6.1', '', '', ('', ''), '.NET 2.0.50727.1433'), ('2.7.4 (IronPython 2.7.4 (2.7.0.40) on Mono 4.0.30319.1 (32-bit))', None, 'cli'): ('IronPython', '2.7.4', '', '', ('', ''), 'Mono 4.0.30319.1 (32-bit)'), ('2.5 (trunk:6107, Mar 26 2009, 13:02:18) \n[Java HotSpot(TM) Client VM ("Apple Computer, Inc.")]', ('Jython', 'trunk', '6107'), 'java1.5.0_16'): ('Jython', '2.5.0', 'trunk', '6107', ('trunk:6107', 'Mar 26 2009'), 'java1.5.0_16'), ('2.5.2 (63378, Mar 26 2009, 18:03:29)\n[PyPy 1.0.0]', ('PyPy', 'trunk', '63378'), self.save_platform): ('PyPy', '2.5.2', 'trunk', '63378', ('63378', 'Mar 26 2009'), '')}
    for ((version_tag, scm, sys_platform), info) in sys_versions.items():
        sys.version = version_tag
        if scm is None:
            if hasattr(sys, '_git'):
                del sys._git
        else:
            sys._git = scm
        if sys_platform is not None:
            sys.platform = sys_platform
        self.assertEqual(platform.python_implementation(), info[0])
        self.assertEqual(platform.python_version(), info[1])
        self.assertEqual(platform.python_branch(), info[2])
        self.assertEqual(platform.python_revision(), info[3])
        self.assertEqual(platform.python_build(), info[4])
        self.assertEqual(platform.python_compiler(), info[5])
