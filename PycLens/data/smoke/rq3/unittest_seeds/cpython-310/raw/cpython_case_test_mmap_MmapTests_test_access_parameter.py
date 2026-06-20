# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mmap.py
# case: MmapTests_test_access_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mapsize = 10
    with open(TESTFN, 'wb') as fp:
        fp.write(b'a' * mapsize)
    with open(TESTFN, 'rb') as f:
        m = mmap.mmap(f.fileno(), mapsize, access=mmap.ACCESS_READ)
        self.assertEqual(m[:], b'a' * mapsize, 'Readonly memory map data incorrect.')
        try:
            m[:] = b'b' * mapsize
        except TypeError:
            pass
        else:
            self.fail('Able to write to readonly memory map')
        try:
            m[0] = b'b'
        except TypeError:
            pass
        else:
            self.fail('Able to write to readonly memory map')
        try:
            m.seek(0, 0)
            m.write(b'abc')
        except TypeError:
            pass
        else:
            self.fail('Able to write to readonly memory map')
        try:
            m.seek(0, 0)
            m.write_byte(b'd')
        except TypeError:
            pass
        else:
            self.fail('Able to write to readonly memory map')
        try:
            m.resize(2 * mapsize)
        except SystemError:
            pass
        except TypeError:
            pass
        else:
            self.fail('Able to resize readonly memory map')
        with open(TESTFN, 'rb') as fp:
            self.assertEqual(fp.read(), b'a' * mapsize, 'Readonly memory map data file was modified')
    with open(TESTFN, 'r+b') as f:
        try:
            m = mmap.mmap(f.fileno(), mapsize + 1)
        except ValueError:
            if sys.platform.startswith('win'):
                self.fail('Opening mmap with size+1 should work on Windows.')
        else:
            if not sys.platform.startswith('win'):
                self.fail('Opening mmap with size+1 should raise ValueError.')
            m.close()
        if sys.platform.startswith('win'):
            with open(TESTFN, 'r+b') as f:
                f.truncate(mapsize)
    with open(TESTFN, 'r+b') as f:
        m = mmap.mmap(f.fileno(), mapsize, access=mmap.ACCESS_WRITE)
        m[:] = b'c' * mapsize
        self.assertEqual(m[:], b'c' * mapsize, 'Write-through memory map memory not updated properly.')
        m.flush()
        m.close()
    with open(TESTFN, 'rb') as f:
        stuff = f.read()
    self.assertEqual(stuff, b'c' * mapsize, 'Write-through memory map data file not updated properly.')
    with open(TESTFN, 'r+b') as f:
        m = mmap.mmap(f.fileno(), mapsize, access=mmap.ACCESS_COPY)
        m[:] = b'd' * mapsize
        self.assertEqual(m[:], b'd' * mapsize, 'Copy-on-write memory map data not written correctly.')
        m.flush()
        with open(TESTFN, 'rb') as fp:
            self.assertEqual(fp.read(), b'c' * mapsize, 'Copy-on-write test data file should not be modified.')
        self.assertRaises(TypeError, m.resize, 2 * mapsize)
        m.close()
    with open(TESTFN, 'r+b') as f:
        self.assertRaises(ValueError, mmap.mmap, f.fileno(), mapsize, access=4)
    if os.name == 'posix':
        with open(TESTFN, 'r+b') as f:
            self.assertRaises(ValueError, mmap.mmap, f.fileno(), mapsize, flags=mmap.MAP_PRIVATE, prot=mmap.PROT_READ, access=mmap.ACCESS_WRITE)
        prot = mmap.PROT_READ | getattr(mmap, 'PROT_EXEC', 0)
        with open(TESTFN, 'r+b') as f:
            m = mmap.mmap(f.fileno(), mapsize, prot=prot)
            self.assertRaises(TypeError, m.write, b'abcdef')
            self.assertRaises(TypeError, m.write_byte, 0)
            m.close()
