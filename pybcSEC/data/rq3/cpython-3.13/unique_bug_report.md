# RQ3 Unique Bug Report: cpython-3.13

## Summary

- Crash findings: 3342
- Unique bugs: 244
- Representative pyc artifacts: 244

## Unique Bugs

### 1. cpython-313-3bd6a6fc56ad

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fb8291b08`
- Honggfuzz stack hash: `fb8291b08`
- PC: `0x0`
- Fault address: `0x0`
- Instruction: `[NOT_MMAPED]`
- Findings: 861
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3bd6a6fc56ad.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.fb8291b08.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.fb8291b08.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.fb8291b08.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.20.STACK.fb8291b08.CODE.1.ADDR.20.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5556b19d00f9.STACK.fb8291b08.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555b1382a8f6.STACK.fb8291b08.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555d9a4b864e.STACK.fb8291b08.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - ... 856 more

### 2. cpython-313-b44da3117bd4

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b45caf733`
- Honggfuzz stack hash: `1b45caf733`
- PC: `0x6fffa53bb9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 696
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b44da3117bd4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.6fffa53bb9fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.6fffa53bb9fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.6fffa53bb9fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.701189d489fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7019590399fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.701c8b0299fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.701fe130c9fc.STACK.1b45caf733.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 691 more

### 3. cpython-313-1625c60794c2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c7d9487dc`
- Honggfuzz stack hash: `c7d9487dc`
- PC: `0x0`
- Fault address: `0x0`
- Instruction: `[NOT_MMAPED]`
- Findings: 223
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1625c60794c2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.c7d9487dc.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.c7d9487dc.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.0.STACK.c7d9487dc.CODE.1.ADDR.0.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55666d3e5214.STACK.c7d9487dc.CODE.1.ADDR.51555555fd.INSTR.mov____0xa8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55672136915e.STACK.c7d9487dc.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.556894cbd145.STACK.c7d9487dc.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557bb84c73f0.STACK.c7d9487dc.CODE.1.ADDR.ffffffff.INSTR.mov____(%r15),%r13.pyc`
  - ... 218 more

### 4. cpython-313-77025e7c9dc9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f348f1eef`
- Honggfuzz stack hash: `f348f1eef`
- PC: `0x5567d3b382b7`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 139
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-77025e7c9dc9.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5567d3b382b7.STACK.f348f1eef.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5567d3b382b7.STACK.f348f1eef.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5567d3b382b7.STACK.f348f1eef.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557e0dec6331.STACK.f348f1eef.CODE.1.ADDR.28.INSTR.cmp____%rax,0x20(%r13).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558096ee7331.STACK.f348f1eef.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r13).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558ca60cc2b7.STACK.f348f1eef.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558db18ce2b7.STACK.f348f1eef.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - ... 134 more

### 5. cpython-313-0968259d1a22

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dff5927e6`
- Honggfuzz stack hash: `dff5927e6`
- PC: `0x5582d5e2770e`
- Fault address: `0x310`
- Instruction: `mov____0x8(%r14,%rbx,8),%r14`
- Findings: 91
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0968259d1a22.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5582d5e2770e.STACK.dff5927e6.CODE.1.ADDR.310.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5582d5e2770e.STACK.dff5927e6.CODE.1.ADDR.310.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5582d5e2770e.STACK.dff5927e6.CODE.1.ADDR.310.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a58bdff70e.STACK.dff5927e6.CODE.1.ADDR.4f0.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55b7e84bb70e.STACK.dff5927e6.CODE.1.ADDR.10.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e5dc48570e.STACK.dff5927e6.CODE.1.ADDR.350.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.560f2d94070e.STACK.dff5927e6.CODE.1.ADDR.280.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - ... 86 more

### 6. cpython-313-dbb4c27d1edd

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b86ae438`
- Honggfuzz stack hash: `19b86ae438`
- PC: `0x557d1ea582b7`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 65
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-dbb4c27d1edd.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557d1ea582b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557d1ea582b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557d1ea582b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5583c0d272b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e3b7dba2b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e5d149a2b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56152d1f52b7.STACK.19b86ae438.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rax.pyc`
  - ... 60 more

### 7. cpython-313-3b8f1f5a4285

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b0fa8b4c9`
- Honggfuzz stack hash: `1b0fa8b4c9`
- PC: `0x555c3fc812a0`
- Fault address: `0x30`
- Instruction: `mov____0x30(%rax),%rbx`
- Findings: 63
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3b8f1f5a4285.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555c3fc812a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555c3fc812a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555c3fc812a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558da7f272a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a1cb88e24d.STACK.1b0fa8b4c9.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ef125412a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5644179802a0.STACK.1b0fa8b4c9.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
  - ... 58 more

### 8. cpython-313-8b6a6c559fc4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:da68cfe12`
- Honggfuzz stack hash: `da68cfe12`
- PC: `0x555d91605443`
- Fault address: `0xa`
- Instruction: `mov____(%r12),%ebx`
- Findings: 58
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8b6a6c559fc4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555d91605443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555d91605443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555d91605443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a323621443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55c02704e443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ddedb07443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56096f681443.STACK.da68cfe12.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - ... 53 more

### 9. cpython-313-f7a0eb6418d8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:df76d542d`
- Honggfuzz stack hash: `df76d542d`
- PC: `0x5570d8adda7e`
- Fault address: `0x0`
- Instruction: `mov____0x78(%r15),%rbx`
- Findings: 50
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f7a0eb6418d8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5570d8adda7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5570d8adda7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5570d8adda7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55d023bbca7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5605771eca7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.568ba249fa7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.576d32859a7e.STACK.df76d542d.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - ... 45 more

### 10. cpython-313-ab348f7810b9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a6a220127`
- Honggfuzz stack hash: `1a6a220127`
- PC: `0x55692f0be077`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 46
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ab348f7810b9.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55692f0be077.STACK.1a6a220127.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55692f0be077.STACK.1a6a220127.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55692f0be077.STACK.1a6a220127.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a81d095077.STACK.1a6a220127.CODE.1.ADDR.1010425.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55cc39e25077.STACK.1a6a220127.CODE.1.ADDR.59.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.562205ca0077.STACK.1a6a220127.CODE.1.ADDR.99.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56993f994077.STACK.1a6a220127.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rax.pyc`
  - ... 41 more

### 11. cpython-313-54ee2c36432d

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b48a39a35`
- Honggfuzz stack hash: `1b48a39a35`
- PC: `0x70325a1489fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 39
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-54ee2c36432d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70325a1489fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70325a1489fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70325a1489fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.706c103b39fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70ab9eac89fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70f3642769fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.716d3713e9fc.STACK.1b48a39a35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 34 more

### 12. cpython-313-c8f31bc2da49

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c28237118`
- Honggfuzz stack hash: `c28237118`
- PC: `0x558665a9eac7`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r12),%r13`
- Findings: 33
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c8f31bc2da49.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558665a9eac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558665a9eac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.558665a9eac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55897a7eeac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.567a631ebac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.573101055ac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.579bece64ac7.STACK.c28237118.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%r13.pyc`
  - ... 28 more

### 13. cpython-313-6ba05923d946

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f2661024d`
- Honggfuzz stack hash: `f2661024d`
- PC: `0x569798b045cc`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 31
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6ba05923d946.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569798b045cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569798b045cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569798b045cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58921b9fe5d5.STACK.f2661024d.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.590438a045cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.599e4bc465cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a1bc73ec5cc.STACK.f2661024d.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
  - ... 26 more

### 14. cpython-313-0459c7ef6eca

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fb819e3f9`
- Honggfuzz stack hash: `fb819e3f9`
- PC: `0x5593b4afdb36`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 30
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0459c7ef6eca.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5593b4afdb36.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5593b4afdb36.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5593b4afdb36.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5643a400dac7.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56658b9b4ac7.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.567696a0db36.STACK.fb819e3f9.CODE.1.ADDR.12.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56bcd2febac7.STACK.fb819e3f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r13.pyc`
  - ... 25 more

### 15. cpython-313-28d3637f8d76

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a699e9c02`
- Honggfuzz stack hash: `1a699e9c02`
- PC: `0x557b83fba6fd`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r15),%rdi`
- Findings: 30
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-28d3637f8d76.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557b83fba6fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557b83fba6fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557b83fba6fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e25f8716fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56658868b6fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5781d672a6fd.STACK.1a699e9c02.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57b4c89a46fd.STACK.1a699e9c02.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - ... 25 more

### 16. cpython-313-a985eee26591

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ce412a337`
- Honggfuzz stack hash: `ce412a337`
- PC: `0x55cce2106320`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%rsi`
- Findings: 28
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a985eee26591.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55cce2106320.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rsi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55cce2106320.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rsi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55cce2106320.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d66b63a31c.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5880fe47c320.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e1c3edd3ff.STACK.ce412a337.CODE.128.ADDR.0.INSTR.mov____0xc8(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a07d1e23320.STACK.ce412a337.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rsi.pyc`
  - ... 23 more

### 17. cpython-313-723064451927

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d743994c7`
- Honggfuzz stack hash: `d743994c7`
- PC: `0x55863dacf91f`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 27
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-723064451927.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55863dacf91f.STACK.d743994c7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55863dacf91f.STACK.d743994c7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55863dacf91f.STACK.d743994c7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56b3dfc3791f.STACK.d743994c7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56cb9cb2891f.STACK.d743994c7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.577a9ee1e923.STACK.d743994c7.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57805cdc0923.STACK.d743994c7.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - ... 22 more

### 18. cpython-313-4c352f3d6921

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:e4a535e56`
- Honggfuzz stack hash: `e4a535e56`
- PC: `0x70ea559e59fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 24
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4c352f3d6921.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70ea559e59fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70ea559e59fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70ea559e59fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70f8703ba9fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.715a4c4379fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71967daaa9fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71f7eb1679fc.STACK.e4a535e56.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 19 more

### 19. cpython-313-565f1a6615dc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b05c1351`
- Honggfuzz stack hash: `19b05c1351`
- PC: `0x5587cba34906`
- Fault address: `0xb1555555b5`
- Instruction: `cmpq___$0x0,0x60(%rbx)`
- Findings: 24
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-565f1a6615dc.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5587cba34906.STACK.19b05c1351.CODE.1.ADDR.b1555555b5.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5587cba34906.STACK.19b05c1351.CODE.1.ADDR.b1555555b5.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5587cba34906.STACK.19b05c1351.CODE.1.ADDR.b1555555b5.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56068a5e8906.STACK.19b05c1351.CODE.1.ADDR.41555555b5.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569fbc7ff456.STACK.19b05c1351.CODE.128.ADDR.0.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5718030ef456.STACK.19b05c1351.CODE.128.ADDR.0.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.579396578906.STACK.19b05c1351.CODE.1.ADDR.b1555555b5.INSTR.cmpq___$0x0,0x60(%rbx).pyc`
  - ... 19 more

### 20. cpython-313-bab3ad528531

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b01c5378`
- Honggfuzz stack hash: `18b01c5378`
- PC: `0x555e2a84332b`
- Fault address: `0x51`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 23
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-bab3ad528531.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e2a84332b.STACK.18b01c5378.CODE.1.ADDR.51.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e2a84332b.STACK.18b01c5378.CODE.1.ADDR.51.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e2a84332b.STACK.18b01c5378.CODE.1.ADDR.51.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a867da632b.STACK.18b01c5378.CODE.1.ADDR.a.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56e745e3c32b.STACK.18b01c5378.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57974805a32b.STACK.18b01c5378.CODE.1.ADDR.6c.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58970c09832b.STACK.18b01c5378.CODE.1.ADDR.b.INSTR.mov____0x8(%r15),%rbx.pyc`
  - ... 18 more

### 21. cpython-313-6d9320bb1c90

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1a07e3bef7`
- Honggfuzz stack hash: `1a07e3bef7`
- PC: `0x700566bd99fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 19
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6d9320bb1c90.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700566bd99fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700566bd99fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700566bd99fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71e901b9a9fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.722956f739fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.724ac2db99fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.725a217cb9fc.STACK.1a07e3bef7.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 14 more

### 22. cpython-313-7ed12ae324b5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:198da9ebfb`
- Honggfuzz stack hash: `198da9ebfb`
- PC: `0x56e0f618c86f`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 19
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7ed12ae324b5.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56e0f618c86f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56e0f618c86f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56e0f618c86f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57e64760186f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.589b1609186f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.591b66d7486f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa31920986f.STACK.198da9ebfb.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - ... 14 more

### 23. cpython-313-ca42dc45eb08

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d796229e7`
- Honggfuzz stack hash: `d796229e7`
- PC: `0x55987033862f`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 19
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ca42dc45eb08.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55987033862f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55987033862f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55987033862f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56dfbf0a262f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.576ec4b3262f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.581acfa5b62f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58c2a73b162f.STACK.d796229e7.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - ... 14 more

### 24. cpython-313-3ab71073c19b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:186de57cc0`
- Honggfuzz stack hash: `186de57cc0`
- PC: `0x566c3ba336ce`
- Fault address: `0x2b0`
- Instruction: `mov____0x8(%r14,%rbx,8),%r14`
- Findings: 18
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3ab71073c19b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566c3ba336ce.STACK.186de57cc0.CODE.1.ADDR.2b0.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566c3ba336ce.STACK.186de57cc0.CODE.1.ADDR.2b0.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566c3ba336ce.STACK.186de57cc0.CODE.1.ADDR.2b0.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56acde7086ce.STACK.186de57cc0.CODE.1.ADDR.2b0.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.574aac2896ce.STACK.186de57cc0.CODE.1.ADDR.270.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5775a4c1e6ce.STACK.186de57cc0.CODE.1.ADDR.298.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57fa3758f6ce.STACK.186de57cc0.CODE.1.ADDR.2c8.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - ... 13 more

### 25. cpython-313-9b0e5fa97c13

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1935855f3e`
- Honggfuzz stack hash: `1935855f3e`
- PC: `0x559f370f86fd`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r15),%rdi`
- Findings: 17
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9b0e5fa97c13.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.559f370f86fd.STACK.1935855f3e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.559f370f86fd.STACK.1935855f3e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.559f370f86fd.STACK.1935855f3e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55c905e956fd.STACK.1935855f3e.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5891971606fd.STACK.1935855f3e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a94930106fd.STACK.1935855f3e.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b518c32e6fd.STACK.1935855f3e.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rdi.pyc`
  - ... 12 more

### 26. cpython-313-ca110854130b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf2f6460e`
- Honggfuzz stack hash: `cf2f6460e`
- PC: `0x55be0ecd9fdd`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 17
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ca110854130b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55be0ecd9fdd.STACK.cf2f6460e.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55be0ecd9fdd.STACK.cf2f6460e.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55be0ecd9fdd.STACK.cf2f6460e.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56bfbf3b3fdd.STACK.cf2f6460e.CODE.1.ADDR.51555555fd.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56ff0f819fdd.STACK.cf2f6460e.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.586b65e4dfdd.STACK.cf2f6460e.CODE.1.ADDR.b1555555fd.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59cf801bcfdd.STACK.cf2f6460e.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - ... 12 more

### 27. cpython-313-e4b7f1de04ee

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dfbb647e4`
- Honggfuzz stack hash: `dfbb647e4`
- PC: `0x556b088af0f9`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 17
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e4b7f1de04ee.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.556b088af0f9.STACK.dfbb647e4.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.556b088af0f9.STACK.dfbb647e4.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.556b088af0f9.STACK.dfbb647e4.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56db774ca4a6.STACK.dfbb647e4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59a9ef70ae28.STACK.dfbb647e4.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59f11d60c0f9.STACK.dfbb647e4.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b0f02477e28.STACK.dfbb647e4.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - ... 12 more

### 28. cpython-313-6b36dd041f16

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fb96e7e0f`
- Honggfuzz stack hash: `fb96e7e0f`
- PC: `0x56f732e1b68b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 16
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6b36dd041f16.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f732e1b68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f732e1b68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f732e1b68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a5e53d1468b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a84408bd68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ad627a8b68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b40579cb68b.STACK.fb96e7e0f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - ... 11 more

### 29. cpython-313-54ae6932b97d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f6ccb6b4`
- Honggfuzz stack hash: `18f6ccb6b4`
- PC: `0x555e7e47bb7b`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r14),%ebx`
- Findings: 15
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-54ae6932b97d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e7e47bb7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e7e47bb7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e7e47bb7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56bae6b69b7b.STACK.18f6ccb6b4.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.577c03f70b7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58eaa0d62b7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59ca21962b7b.STACK.18f6ccb6b4.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - ... 10 more

### 30. cpython-313-da82af161b55

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f7742db3`
- Honggfuzz stack hash: `18f7742db3`
- PC: `0x5794bc73da49`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%rcx`
- Findings: 15
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-da82af161b55.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5794bc73da49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5794bc73da49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5794bc73da49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.589388e54a49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58bae6cb3a49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.596ab46a4a49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.596c2804ea49.STACK.18f7742db3.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - ... 10 more

### 31. cpython-313-01204375a289

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fa3c79581`
- Honggfuzz stack hash: `fa3c79581`
- PC: `0x563a50617e39`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%r12`
- Findings: 14
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-01204375a289.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563a50617e39.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563a50617e39.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563a50617e39.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59c6cb062e39.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ab45d17de39.STACK.fa3c79581.CODE.1.ADDR.4f70000000e.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b3d6f6ade35.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b6f3c070e35.STACK.fa3c79581.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r13.pyc`
  - ... 9 more

### 32. cpython-313-d4d5bb4f11e4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1be9d866d5`
- Honggfuzz stack hash: `1be9d866d5`
- PC: `0x5574da7bb16e`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r13d`
- Findings: 13
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d4d5bb4f11e4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5574da7bb16e.STACK.1be9d866d5.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5574da7bb16e.STACK.1be9d866d5.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5574da7bb16e.STACK.1be9d866d5.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55b669c3e063.STACK.1be9d866d5.CODE.1.ADDR.7.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ad5015a7063.STACK.1be9d866d5.CODE.1.ADDR.49.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e10ee99a063.STACK.1be9d866d5.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e1d8cfbb063.STACK.1be9d866d5.CODE.1.ADDR.49.INSTR.mov____0x8(%rax),%rax.pyc`
  - ... 8 more

### 33. cpython-313-0ea4e4628b13

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19358b84d8`
- Honggfuzz stack hash: `19358b84d8`
- PC: `0x5742c4fee68b`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 12
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0ea4e4628b13.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5742c4fee68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5742c4fee68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5742c4fee68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59d746e3d68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a174543368b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c5c6063d68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f274eecd68b.STACK.19358b84d8.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - ... 7 more

### 34. cpython-313-a29d48e2eec8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cffdc56bd`
- Honggfuzz stack hash: `cffdc56bd`
- PC: `0x55e683a55e35`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r13`
- Findings: 12
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a29d48e2eec8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e683a55e35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e683a55e35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e683a55e35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5681da89fe35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.585ac0e54e39.STACK.cffdc56bd.CODE.1.ADDR.47ef008.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a52a5d0de35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a8bd0552e35.STACK.cffdc56bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
  - ... 7 more

### 35. cpython-313-8b8edfe752cc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:186895b6fa`
- Honggfuzz stack hash: `186895b6fa`
- PC: `0x568b3653662b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 11
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8b8edfe752cc.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.568b3653662b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.568b3653662b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.568b3653662b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.571f9745f62b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57e9ec83d62b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59b59c29b62b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b499d33b62b.STACK.186895b6fa.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - ... 6 more

### 36. cpython-313-ab53e3148375

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:e4a9ebc85`
- Honggfuzz stack hash: `e4a9ebc85`
- PC: `0x705bd26199fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 11
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ab53e3148375.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.705bd26199fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.705bd26199fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.705bd26199fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.73fe936429fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.76f0822599fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.788033a839fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.789db46cf9fc.STACK.e4a9ebc85.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 6 more

### 37. cpython-313-13674f152f94

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cff390e48`
- Honggfuzz stack hash: `cff390e48`
- PC: `0x57173ecc1b41`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r12),%rdi`
- Findings: 10
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-13674f152f94.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57173ecc1b41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57173ecc1b41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57173ecc1b41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a6c63e10b41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b0bc7aceb41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bdc74721b41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c985185fb41.STACK.cff390e48.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - ... 5 more

### 38. cpython-313-b52eeeba0956

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ff88d2448`
- Honggfuzz stack hash: `ff88d2448`
- PC: `0x5636c45ad608`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 10
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b52eeeba0956.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5636c45ad608.STACK.ff88d2448.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5636c45ad608.STACK.ff88d2448.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5636c45ad608.STACK.ff88d2448.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58ccbb518610.STACK.ff88d2448.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5977ab3ae610.STACK.ff88d2448.CODE.1.ADDR.1c.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c989c659610.STACK.ff88d2448.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c9b2ea8a610.STACK.ff88d2448.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
  - ... 5 more

### 39. cpython-313-d13c6d0ad234

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c78e4f78d`
- Honggfuzz stack hash: `c78e4f78d`
- PC: `0x557fbff4e68b`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 10
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d13c6d0ad234.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557fbff4e68b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557fbff4e68b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.557fbff4e68b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.572087fac68f.STACK.c78e4f78d.CODE.128.ADDR.0.INSTR.mov____0xd8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aef662ec68b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b000cafa68b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dea5c42368b.STACK.c78e4f78d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - ... 5 more

### 40. cpython-313-e8fe8b7b5d4e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a304ad7b1`
- Honggfuzz stack hash: `1a304ad7b1`
- PC: `0x56adff51c86f`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 10
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e8fe8b7b5d4e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56adff51c86f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56adff51c86f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56adff51c86f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f8b0e7c86f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57cdb15d086f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ab53dcf586f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b984561b86f.STACK.1a304ad7b1.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - ... 5 more

### 41. cpython-313-3d1213ed1fd4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b7a1da84`
- Honggfuzz stack hash: `19b7a1da84`
- PC: `0x5949dcb718d0`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r13d`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3d1213ed1fd4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5949dcb718d0.STACK.19b7a1da84.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5949dcb718d0.STACK.19b7a1da84.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5949dcb718d0.STACK.19b7a1da84.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d681b4328d0.STACK.19b7a1da84.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d80367698d0.STACK.19b7a1da84.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60133ad398d0.STACK.19b7a1da84.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60826bce88d0.STACK.19b7a1da84.CODE.1.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
  - ... 4 more

### 42. cpython-313-d43a4f964ff5

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:192630f409`
- Honggfuzz stack hash: `192630f409`
- PC: `0x71e73bb8d9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d43a4f964ff5.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71e73bb8d9fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71e73bb8d9fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71e73bb8d9fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7712aa90d9fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.77fda0dc79fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.781c63dd79fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.78351c4529fc.STACK.192630f409.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 4 more

### 43. cpython-313-e38e64639bc8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b2a6904c5`
- Honggfuzz stack hash: `1b2a6904c5`
- PC: `0x56232d99f443`
- Fault address: `0x9`
- Instruction: `mov____(%r12),%ebx`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e38e64639bc8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56232d99f443.STACK.1b2a6904c5.CODE.1.ADDR.9.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56232d99f443.STACK.1b2a6904c5.CODE.1.ADDR.9.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56232d99f443.STACK.1b2a6904c5.CODE.1.ADDR.9.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56c9f3c393e6.STACK.1b2a6904c5.CODE.1.ADDR.3.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f9e419e3e6.STACK.1b2a6904c5.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5af9fd6f23e6.STACK.1b2a6904c5.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e3bcbdc63e6.STACK.1b2a6904c5.CODE.1.ADDR.47d00000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - ... 4 more

### 44. cpython-313-3bb82a375b2f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f21afb137`
- Honggfuzz stack hash: `f21afb137`
- PC: `0x57bab37f719f`
- Fault address: `0x0`
- Instruction: `mov____(%r12),%ebx`
- Findings: 8
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3bb82a375b2f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bab37f719f.STACK.f21afb137.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bab37f719f.STACK.f21afb137.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bab37f719f.STACK.f21afb137.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c1b93144063.STACK.f21afb137.CODE.1.ADDR.4019.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5db8109a319f.STACK.f21afb137.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f257664d063.STACK.f21afb137.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60c037a05063.STACK.f21afb137.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
  - ... 3 more

### 45. cpython-313-c1743be46b8e

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f40b71089`
- Honggfuzz stack hash: `f40b71089`
- PC: `0x700f9ab159fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 8
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c1743be46b8e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700f9ab159fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700f9ab159fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700f9ab159fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70c6382e99fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.71bd76b519fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.73dc067d39fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.74d74441d9fc.STACK.f40b71089.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 3 more

### 46. cpython-313-cfc29475c3b0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bab9ce9ee`
- Honggfuzz stack hash: `1bab9ce9ee`
- PC: `0x56eaa2165b4d`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 8
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-cfc29475c3b0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56eaa2165b4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56eaa2165b4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56eaa2165b4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5861bedc9b4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e4f9e6eb4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58f799dbab7b.STACK.1bab9ce9ee.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e661205cb4d.STACK.1bab9ce9ee.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - ... 3 more

### 47. cpython-313-0e561a475660

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1970ee768c`
- Honggfuzz stack hash: `1970ee768c`
- PC: `0x57bb57ebdb4d`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0e561a475660.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bb57ebdb4d.STACK.1970ee768c.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bb57ebdb4d.STACK.1970ee768c.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bb57ebdb4d.STACK.1970ee768c.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b4801cd5b4d.STACK.1970ee768c.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dc0239a4b4d.STACK.1970ee768c.CODE.1.ADDR.50.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dd4541d7b7b.STACK.1970ee768c.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61ce873d4b4d.STACK.1970ee768c.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - ... 2 more

### 48. cpython-313-430b652de5db

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d361fae90`
- Honggfuzz stack hash: `d361fae90`
- PC: `0x5b43dfc88744`
- Fault address: `0x21`
- Instruction: `mov____0x9(%r14),%cl`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-430b652de5db.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b43dfc88744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b43dfc88744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b43dfc88744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bcf1d231744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5efb9561b744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60c5544d6744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.615ad4e78744.STACK.d361fae90.CODE.1.ADDR.21.INSTR.mov____0x9(%r14),%cl.pyc`
  - ... 2 more

### 49. cpython-313-a4c7ff490bab

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cbe25fa87`
- Honggfuzz stack hash: `cbe25fa87`
- PC: `0x555e9ec1c32f`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a4c7ff490bab.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e9ec1c32f.STACK.cbe25fa87.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e9ec1c32f.STACK.cbe25fa87.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.555e9ec1c32f.STACK.cbe25fa87.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59203c48932f.STACK.cbe25fa87.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5962257c932f.STACK.cbe25fa87.CODE.1.ADDR.21.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cd3361dd32f.STACK.cbe25fa87.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e620753d368.STACK.cbe25fa87.CODE.2.ADDR.5e62075b1570.INSTR.mov____%ebx,(%r14).pyc`
  - ... 2 more

### 50. cpython-313-f1f3707deb24

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1aec47d06d`
- Honggfuzz stack hash: `1aec47d06d`
- PC: `0x56f3f0a4497c`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r14`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f1f3707deb24.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f3f0a4497c.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f3f0a4497c.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f3f0a4497c.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57cecedac902.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57db8bef1939.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59e1f1e89485.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5af7d74b4485.STACK.1aec47d06d.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%r14.pyc`
  - ... 2 more

### 51. cpython-313-135bdfe7b913

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e282257fb`
- Honggfuzz stack hash: `e282257fb`
- PC: `0x56799e85191f`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-135bdfe7b913.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56799e85191f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56799e85191f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56799e85191f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d92e2f991f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5781187a991f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a7f5951791f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b20ff6ad91f.STACK.e282257fb.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - ... 1 more

### 52. cpython-313-1bf212650693

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19747b70f4`
- Honggfuzz stack hash: `19747b70f4`
- PC: `0x56f49d5a284e`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1bf212650693.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f49d5a284e.STACK.19747b70f4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f49d5a284e.STACK.19747b70f4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56f49d5a284e.STACK.19747b70f4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c94f6add84e.STACK.19747b70f4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f3db70d9852.STACK.19747b70f4.CODE.128.ADDR.0.INSTR.mov____0x70(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f7ce957784e.STACK.19747b70f4.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fc0f98d1852.STACK.19747b70f4.CODE.128.ADDR.0.INSTR.mov____0x70(%r15),%rax.pyc`
  - ... 1 more

### 53. cpython-313-267dff1304e6

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:d70448624`
- Honggfuzz stack hash: `d70448624`
- PC: `0x7077490549fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-267dff1304e6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7077490549fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7077490549fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7077490549fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.716b2d0429fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.758ace9749fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.76c98d76e9fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.784066efb9fc.STACK.d70448624.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 1 more

### 54. cpython-313-3b1bae0d8c9c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3ba11fc0`
- Honggfuzz stack hash: `c3ba11fc0`
- PC: `0x5890010664a8`
- Fault address: `0x10000000f`
- Instruction: `mov____0x10(%r12),%r15`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3b1bae0d8c9c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5890010664a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5890010664a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5890010664a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5933e17a74a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ba0d35084a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eef2205c41d.STACK.c3ba11fc0.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f35e3c744a8.STACK.c3ba11fc0.CODE.1.ADDR.10000000f.INSTR.mov____0x10(%r12),%r15.pyc`
  - ... 1 more

### 55. cpython-313-5d0d7c9fe736

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1ab744e517`
- Honggfuzz stack hash: `1ab744e517`
- PC: `0x5985c2bc85e0`
- Fault address: `0x10`
- Instruction: `mov____0x10(%r12),%rax`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-5d0d7c9fe736.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5985c2bc85e0.STACK.1ab744e517.CODE.1.ADDR.10.INSTR.mov____0x10(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5985c2bc85e0.STACK.1ab744e517.CODE.1.ADDR.10.INSTR.mov____0x10(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5985c2bc85e0.STACK.1ab744e517.CODE.1.ADDR.10.INSTR.mov____0x10(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a38160df41d.STACK.1ab744e517.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a9f8090d5e0.STACK.1ab744e517.CODE.1.ADDR.10.INSTR.mov____0x10(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e02e63e441d.STACK.1ab744e517.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e9228ea34a8.STACK.1ab744e517.CODE.1.ADDR.10.INSTR.mov____0x10(%r12),%r15.pyc`
  - ... 1 more

### 56. cpython-313-6d3accf54014

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f24ff34b1`
- Honggfuzz stack hash: `f24ff34b1`
- PC: `0x565dc2cd568b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6d3accf54014.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.565dc2cd568b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.565dc2cd568b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.565dc2cd568b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bb7687e68b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b1d8cb6068b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b6be21c868b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cb20eef768b.STACK.f24ff34b1.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - ... 1 more

### 57. cpython-313-72c40e55192e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193ffb4240`
- Honggfuzz stack hash: `193ffb4240`
- PC: `0x56ad9051fc9b`
- Fault address: `0x4a`
- Instruction: `movzbl_0xa(%r12),%ebx`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-72c40e55192e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56ad9051fc9b.STACK.193ffb4240.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56ad9051fc9b.STACK.193ffb4240.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56ad9051fc9b.STACK.193ffb4240.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578c20e39c9b.STACK.193ffb4240.CODE.1.ADDR.22.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57ae4837ec9b.STACK.193ffb4240.CODE.128.ADDR.0.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cd9bf13ec9b.STACK.193ffb4240.CODE.1.ADDR.c.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e01e02a5c9b.STACK.193ffb4240.CODE.1.ADDR.22.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - ... 1 more

### 58. cpython-313-e07f52f06934

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cd27ce450`
- Honggfuzz stack hash: `cd27ce450`
- PC: `0x566933f78ae8`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%rax),%r14`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e07f52f06934.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566933f78ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566933f78ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.566933f78ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a1d682ddae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c609eff8ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6aa7966ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.635ec8ca4ae8.STACK.cd27ce450.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r14.pyc`
  - ... 1 more

### 59. cpython-313-f2b10b74b73b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183267e7bd`
- Honggfuzz stack hash: `183267e7bd`
- PC: `0x5d1fc9cb251a`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f2b10b74b73b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d1fc9cb251a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d1fc9cb251a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d1fc9cb251a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e43e614751a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60620c0f351a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6109c78a851a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.614d65efb51a.STACK.183267e7bd.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
  - ... 1 more

### 60. cpython-313-1df61cb9f515

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f56c30465`
- Honggfuzz stack hash: `f56c30465`
- PC: `0x70be0b9579fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1df61cb9f515.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70be0b9579fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70be0b9579fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70be0b9579fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7729a7aff9fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7ecc0b46e9fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7f00bef419fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7fcbdf33a9fc.STACK.f56c30465.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 61. cpython-313-2abdeadf7715

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b29b52204`
- Honggfuzz stack hash: `1b29b52204`
- PC: `0x5668e5963a49`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rcx`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2abdeadf7715.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5668e5963a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5668e5963a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5668e5963a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5879df559a60.STACK.1b29b52204.CODE.1.ADDR.180.INSTR.mov____0x180(%rcx),%r14d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dcaf7310a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fd7dc506a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.602d06ea2a49.STACK.1b29b52204.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`

### 62. cpython-313-446186484d79

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bb6723aa3`
- Honggfuzz stack hash: `1bb6723aa3`
- PC: `0x597cf713b48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-446186484d79.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.597cf713b48c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.597cf713b48c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.597cf713b48c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d61489e848c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eca6a04748c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.609064ed648c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63c44e19948c.STACK.1bb6723aa3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 63. cpython-313-7cb26cd127c4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1af5ca3102`
- Honggfuzz stack hash: `1af5ca3102`
- PC: `0x578fc745951a`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7cb26cd127c4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578fc745951a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578fc745951a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578fc745951a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59313e86e51a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c5f6e59b51a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ce1d302551a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.637c6ad8151a.STACK.1af5ca3102.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`

### 64. cpython-313-848d2843d56f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d3d4e4290`
- Honggfuzz stack hash: `d3d4e4290`
- PC: `0x569999f2b32b`
- Fault address: `0xffffffff0000006a`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-848d2843d56f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569999f2b32b.STACK.d3d4e4290.CODE.1.ADDR.ffffffff0000006a.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569999f2b32b.STACK.d3d4e4290.CODE.1.ADDR.ffffffff0000006a.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.569999f2b32b.STACK.d3d4e4290.CODE.1.ADDR.ffffffff0000006a.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58c5d7f1732b.STACK.d3d4e4290.CODE.1.ADDR.a.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dc09144d32b.STACK.d3d4e4290.CODE.1.ADDR.11.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e337628532b.STACK.d3d4e4290.CODE.1.ADDR.ffffffff0000013c.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61aa35fb132b.STACK.d3d4e4290.CODE.1.ADDR.79.INSTR.mov____0x8(%r15),%rbx.pyc`

### 65. cpython-313-a13091ad8446

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3b34585f`
- Honggfuzz stack hash: `c3b34585f`
- PC: `0x58a5a24cff80`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r12`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a13091ad8446.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a24cff80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a24cff80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a24cff80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58c684167088.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____0xb8(%rax),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a59f1279f80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bbe50bebf80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ff422697f80.STACK.c3b34585f.CODE.128.ADDR.0.INSTR.mov____(%r14),%r12.pyc`

### 66. cpython-313-da1130ea42ca

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1ab3250001`
- Honggfuzz stack hash: `1ab3250001`
- PC: `0x5b0b290e7960`
- Fault address: `0x5b0b3bf43000`
- Instruction: `cmpq___$0x1,0x48(%rax,%rbx,8)`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-da1130ea42ca.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b0b290e7960.STACK.1ab3250001.CODE.1.ADDR.5b0b3bf43000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b0b290e7960.STACK.1ab3250001.CODE.1.ADDR.5b0b3bf43000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b0b290e7960.STACK.1ab3250001.CODE.1.ADDR.5b0b3bf43000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c05122720cd.STACK.1ab3250001.CODE.1.ADDR.7be7bc83bb20.INSTR.mov____%r14,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f8914e0f960.STACK.1ab3250001.CODE.1.ADDR.5f8931bab000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60e213edf960.STACK.1ab3250001.CODE.1.ADDR.60e25986e000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63b015482960.STACK.1ab3250001.CODE.1.ADDR.63b05b812000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`

### 67. cpython-313-e52662a9df29

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e06b474d7`
- Honggfuzz stack hash: `e06b474d7`
- PC: `0x594e88ff324d`
- Fault address: `0x20`
- Instruction: `mov____0x20(%rax),%r13`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e52662a9df29.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.594e88ff324d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.594e88ff324d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.594e88ff324d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ac20658a24d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c93c0ac324d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60b925a4124d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61b3502d624d.STACK.e06b474d7.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`

### 68. cpython-313-e90961a27110

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e6958f0e5`
- Honggfuzz stack hash: `e6958f0e5`
- PC: `0x5760bcbbe860`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e90961a27110.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5760bcbbe860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5760bcbbe860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5760bcbbe860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a83af6ad860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a99a693a860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cb80c91b860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64f803beb860.STACK.e6958f0e5.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`

### 69. cpython-313-f2dacc5c4f14

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c64a98858`
- Honggfuzz stack hash: `c64a98858`
- PC: `0x57a59aba68d0`
- Fault address: `0x1d1`
- Instruction: `mov____(%r14),%r13d`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f2dacc5c4f14.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57a59aba68d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57a59aba68d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57a59aba68d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.581b8c6b98d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59923ab5b8d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e9ee10f08d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6114cf7e38d0.STACK.c64a98858.CODE.1.ADDR.1d1.INSTR.mov____(%r14),%r13d.pyc`

### 70. cpython-313-03bc6b0358c5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1829e6ad12`
- Honggfuzz stack hash: `1829e6ad12`
- PC: `0x5a575276068b`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-03bc6b0358c5.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a575276068b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a575276068b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a575276068b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d3f383f168b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e5e1f10568b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64205a8b468b.STACK.1829e6ad12.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`

### 71. cpython-313-0db0b74015ae

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b4b47e41a`
- Honggfuzz stack hash: `1b4b47e41a`
- PC: `0x5b2c0bcb31c7`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0db0b74015ae.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2c0bcb31c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2c0bcb31c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2c0bcb31c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e0e6ea141c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.62e453c961c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63139e7541c7.STACK.1b4b47e41a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 72. cpython-313-15ee33316cf6

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f56c3fba2`
- Honggfuzz stack hash: `f56c3fba2`
- PC: `0x700c7ef799fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-15ee33316cf6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700c7ef799fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700c7ef799fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.700c7ef799fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.763dce74e9fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7788489d59fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7b29762649fc.STACK.f56c3fba2.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 73. cpython-313-5a825f849914

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1baad77588`
- Honggfuzz stack hash: `1baad77588`
- PC: `0x5a84b7102b7b`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-5a825f849914.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a84b7102b7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a84b7102b7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a84b7102b7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60726b80ab7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60f389d72b7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.614d79d6fb7b.STACK.1baad77588.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 74. cpython-313-91bc3838db54

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1876f092dc`
- Honggfuzz stack hash: `1876f092dc`
- PC: `0x5e1adb2cba9a`
- Fault address: `0x20`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-91bc3838db54.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e1adb2cba9a.STACK.1876f092dc.CODE.1.ADDR.20.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e1adb2cba9a.STACK.1876f092dc.CODE.1.ADDR.20.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e1adb2cba9a.STACK.1876f092dc.CODE.1.ADDR.20.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e2012235a9a.STACK.1876f092dc.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f76cfd748f6.STACK.1876f092dc.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60d113b64e28.STACK.1876f092dc.CODE.1.ADDR.c0.INSTR.mov____(%r15),%ebx.pyc`

### 75. cpython-313-9fe9c94b5861

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bb168e252`
- Honggfuzz stack hash: `1bb168e252`
- PC: `0x51`
- Fault address: `0x51`
- Instruction: `[NOT_MMAPED]`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9fe9c94b5861.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.51.STACK.1bb168e252.CODE.1.ADDR.51.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.51.STACK.1bb168e252.CODE.1.ADDR.51.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.51.STACK.1bb168e252.CODE.1.ADDR.51.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.627e497734e0.STACK.1bb168e252.CODE.2.ADDR.627e497734e0.INSTR.(bad)__.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6501a232ca7e.STACK.1bb168e252.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.b1.STACK.1bb168e252.CODE.1.ADDR.b1.INSTR.[NOT_MMAPED].pyc`

### 76. cpython-313-af64cf4c2267

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d712b45f2`
- Honggfuzz stack hash: `d712b45f2`
- PC: `0x55e97275ec9b`
- Fault address: `0x4a`
- Instruction: `movzbl_0xa(%r12),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-af64cf4c2267.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e97275ec9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e97275ec9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e97275ec9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa156765c9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f789ce44c9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64ca17397c9b.STACK.d712b45f2.CODE.1.ADDR.4a.INSTR.movzbl_0xa(%r12),%ebx.pyc`

### 77. cpython-313-b727fb8a2814

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ee47eb6f7`
- Honggfuzz stack hash: `ee47eb6f7`
- PC: `0x5b014c89a31e`
- Fault address: `0x80`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b727fb8a2814.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b014c89a31e.STACK.ee47eb6f7.CODE.1.ADDR.80.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b014c89a31e.STACK.ee47eb6f7.CODE.1.ADDR.80.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b014c89a31e.STACK.ee47eb6f7.CODE.1.ADDR.80.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e414084d31e.STACK.ee47eb6f7.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fadcab4131e.STACK.ee47eb6f7.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.644d0d12331e.STACK.ee47eb6f7.CODE.1.ADDR.9.INSTR.mov____0x8(%r15),%rax.pyc`

### 78. cpython-313-c01584854864

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b348e75c6`
- Honggfuzz stack hash: `1b348e75c6`
- PC: `0x579c637fe62b`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c01584854864.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.579c637fe62b.STACK.1b348e75c6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.579c637fe62b.STACK.1b348e75c6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.579c637fe62b.STACK.1b348e75c6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58febdded62b.STACK.1b348e75c6.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c382836862b.STACK.1b348e75c6.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60439d90162b.STACK.1b348e75c6.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`

### 79. cpython-313-c03582dffcdb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e053a5e2e`
- Honggfuzz stack hash: `e053a5e2e`
- PC: `0x57f3b8bf8837`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c03582dffcdb.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57f3b8bf8837.STACK.e053a5e2e.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57f3b8bf8837.STACK.e053a5e2e.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57f3b8bf8837.STACK.e053a5e2e.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a80dafd7837.STACK.e053a5e2e.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c6a6640d837.STACK.e053a5e2e.CODE.1.ADDR.7.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.651e6ba23837.STACK.e053a5e2e.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`

### 80. cpython-313-dfb31e45a150

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fb819e7ea`
- Honggfuzz stack hash: `fb819e7ea`
- PC: `0x56002ee8b8c8`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-dfb31e45a150.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56002ee8b8c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56002ee8b8c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56002ee8b8c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bcf5f1788c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6297ae74b8c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64f0c07768c8.STACK.fb819e7ea.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`

### 81. cpython-313-e01d675b8d5e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b5567666`
- Honggfuzz stack hash: `18b5567666`
- PC: `0x5c3d8492195f`
- Fault address: `0x2c`
- Instruction: `mov____(%r14),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e01d675b8d5e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c3d8492195f.STACK.18b5567666.CODE.1.ADDR.2c.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c3d8492195f.STACK.18b5567666.CODE.1.ADDR.2c.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c3d8492195f.STACK.18b5567666.CODE.1.ADDR.2c.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d3d614e995f.STACK.18b5567666.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e383d13095f.STACK.18b5567666.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.642b220bf95f.STACK.18b5567666.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`

### 82. cpython-313-e9260dcc0fe1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1ac71de238`
- Honggfuzz stack hash: `1ac71de238`
- PC: `0x55f6fa8f77ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e9260dcc0fe1.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f6fa8f77ef.STACK.1ac71de238.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f6fa8f77ef.STACK.1ac71de238.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f6fa8f77ef.STACK.1ac71de238.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d5b46ea7ef.STACK.1ac71de238.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2ab9afb7ef.STACK.1ac71de238.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cfc03d3b7ef.STACK.1ac71de238.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r15),%r12.pyc`

### 83. cpython-313-08ba83999c8e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bab6fee8f`
- Honggfuzz stack hash: `1bab6fee8f`
- PC: `0x5df2a002aa49`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rcx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-08ba83999c8e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5df2a002aa49.STACK.1bab6fee8f.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5df2a002aa49.STACK.1bab6fee8f.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5df2a002aa49.STACK.1bab6fee8f.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61d4f8f1da49.STACK.1bab6fee8f.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.636acaad1a49.STACK.1bab6fee8f.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rcx.pyc`

### 84. cpython-313-1f0a3657a3c0

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b8576628f`
- Honggfuzz stack hash: `1b8576628f`
- PC: `0x7317f2d5b9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1f0a3657a3c0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7317f2d5b9fc.STACK.1b8576628f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7317f2d5b9fc.STACK.1b8576628f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7317f2d5b9fc.STACK.1b8576628f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.78b02ef889fc.STACK.1b8576628f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7f20632179fc.STACK.1b8576628f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 85. cpython-313-259786d8bac2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e62d7e6b3`
- Honggfuzz stack hash: `e62d7e6b3`
- PC: `0x5744c62694a3`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-259786d8bac2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744c62694a3.STACK.e62d7e6b3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744c62694a3.STACK.e62d7e6b3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744c62694a3.STACK.e62d7e6b3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6109130d74a3.STACK.e62d7e6b3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61c60b65a4a3.STACK.e62d7e6b3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`

### 86. cpython-313-48bcaee7d433

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b76fb7b1b`
- Honggfuzz stack hash: `1b76fb7b1b`
- PC: `0x58e5ee62c7ae`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r13`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-48bcaee7d433.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e5ee62c7ae.STACK.1b76fb7b1b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e5ee62c7ae.STACK.1b76fb7b1b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e5ee62c7ae.STACK.1b76fb7b1b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e34483cf7ae.STACK.1b76fb7b1b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.62f54eb7c7ae.STACK.1b76fb7b1b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r13.pyc`

### 87. cpython-313-4a0ea59d58a7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fa322cd74`
- Honggfuzz stack hash: `fa322cd74`
- PC: `0x567f1972db41`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r12),%rdi`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4a0ea59d58a7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.567f1972db41.STACK.fa322cd74.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.567f1972db41.STACK.fa322cd74.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.567f1972db41.STACK.fa322cd74.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c662efc2b41.STACK.fa322cd74.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e665774db41.STACK.fa322cd74.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`

### 88. cpython-313-4d663483f93a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dbe22512b`
- Honggfuzz stack hash: `dbe22512b`
- PC: `0x5cdc099d832b`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4d663483f93a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cdc099d832b.STACK.dbe22512b.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cdc099d832b.STACK.dbe22512b.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cdc099d832b.STACK.dbe22512b.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eb9fe17d32b.STACK.dbe22512b.CODE.128.ADDR.0.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61900d09f32b.STACK.dbe22512b.CODE.1.ADDR.49.INSTR.mov____0x8(%r15),%rbx.pyc`

### 89. cpython-313-61a8bfd440e1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:194fbe3a55`
- Honggfuzz stack hash: `194fbe3a55`
- PC: `0x5ba7e59c2396`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-61a8bfd440e1.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ba7e59c2396.STACK.194fbe3a55.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ba7e59c2396.STACK.194fbe3a55.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ba7e59c2396.STACK.194fbe3a55.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6300125d5396.STACK.194fbe3a55.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64df30a26396.STACK.194fbe3a55.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 90. cpython-313-6410fc2e7115

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c7ad679f6`
- Honggfuzz stack hash: `c7ad679f6`
- PC: `0x5c142efe87eb`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6410fc2e7115.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c142efe87eb.STACK.c7ad679f6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c142efe87eb.STACK.c7ad679f6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c142efe87eb.STACK.c7ad679f6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.618a045eb7eb.STACK.c7ad679f6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63c4f4f157eb.STACK.c7ad679f6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`

### 91. cpython-313-66087d114881

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f014c112c`
- Honggfuzz stack hash: `f014c112c`
- PC: `0x57416a42186f`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-66087d114881.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57416a42186f.STACK.f014c112c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57416a42186f.STACK.f014c112c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57416a42186f.STACK.f014c112c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57c87b6e4873.STACK.f014c112c.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5856db89386f.STACK.f014c112c.CODE.1.ADDR.9.INSTR.mov____0x8(%r14),%rax.pyc`

### 92. cpython-313-72cd5b675ae1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e25f92120`
- Honggfuzz stack hash: `e25f92120`
- PC: `0x571f16a5196c`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%r12`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-72cd5b675ae1.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.571f16a5196c.STACK.e25f92120.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.571f16a5196c.STACK.e25f92120.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.571f16a5196c.STACK.e25f92120.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa0185339cf.STACK.e25f92120.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6106bfc719cf.STACK.e25f92120.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`

### 93. cpython-313-7bebb570939a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ef85abf8b`
- Honggfuzz stack hash: `ef85abf8b`
- PC: `0x57da7fb9148c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7bebb570939a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57da7fb9148c.STACK.ef85abf8b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57da7fb9148c.STACK.ef85abf8b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57da7fb9148c.STACK.ef85abf8b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58470846548c.STACK.ef85abf8b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61afbc0cf48c.STACK.ef85abf8b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 94. cpython-313-808113f73180

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183c81397c`
- Honggfuzz stack hash: `183c81397c`
- PC: `0x58e2eda9495f`
- Fault address: `0x100000003`
- Instruction: `mov____(%r14),%ebx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-808113f73180.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e2eda9495f.STACK.183c81397c.CODE.1.ADDR.100000003.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e2eda9495f.STACK.183c81397c.CODE.1.ADDR.100000003.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58e2eda9495f.STACK.183c81397c.CODE.1.ADDR.100000003.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59864738d95f.STACK.183c81397c.CODE.1.ADDR.ffffffff00790079.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c95db56d95f.STACK.183c81397c.CODE.1.ADDR.ffffffff00790079.INSTR.mov____(%r14),%ebx.pyc`

### 95. cpython-313-8c439b747068

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1be9d8b259`
- Honggfuzz stack hash: `1be9d8b259`
- PC: `0x5a754995696c`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%r12`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8c439b747068.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a754995696c.STACK.1be9d8b259.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a754995696c.STACK.1be9d8b259.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a754995696c.STACK.1be9d8b259.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60e58248196c.STACK.1be9d8b259.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.610b85cd296c.STACK.1be9d8b259.CODE.1.ADDR.0.INSTR.mov____(%r15),%r12.pyc`

### 96. cpython-313-8cc5d7fd7e5c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3fa70b2e`
- Honggfuzz stack hash: `c3fa70b2e`
- PC: `0x5c9a5577924a`
- Fault address: `0xffffffff`
- Instruction: `mov____0x0(%r13),%r14`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8cc5d7fd7e5c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c9a5577924a.STACK.c3fa70b2e.CODE.1.ADDR.ffffffff.INSTR.mov____0x0(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c9a5577924a.STACK.c3fa70b2e.CODE.1.ADDR.ffffffff.INSTR.mov____0x0(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c9a5577924a.STACK.c3fa70b2e.CODE.1.ADDR.ffffffff.INSTR.mov____0x0(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6416ff9f324a.STACK.c3fa70b2e.CODE.1.ADDR.ffffffff.INSTR.mov____0x0(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64656d98d24a.STACK.c3fa70b2e.CODE.1.ADDR.ffffffff.INSTR.mov____0x0(%r13),%r14.pyc`

### 97. cpython-313-977000d3b2ec

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1aae57dafa`
- Honggfuzz stack hash: `1aae57dafa`
- PC: `0x56fd6f7d9849`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-977000d3b2ec.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56fd6f7d9849.STACK.1aae57dafa.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56fd6f7d9849.STACK.1aae57dafa.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56fd6f7d9849.STACK.1aae57dafa.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.591adaf64849.STACK.1aae57dafa.CODE.1.ADDR.9.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e50e0476849.STACK.1aae57dafa.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rax.pyc`

### 98. cpython-313-9e3eefef4885

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d7bf9040b`
- Honggfuzz stack hash: `d7bf9040b`
- PC: `0x583b0f0238e0`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9e3eefef4885.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.583b0f0238e0.STACK.d7bf9040b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.583b0f0238e0.STACK.d7bf9040b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.583b0f0238e0.STACK.d7bf9040b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d62f24bb8e0.STACK.d7bf9040b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6089a5d248e0.STACK.d7bf9040b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`

### 99. cpython-313-9fb7c38d048f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:182ae0b827`
- Honggfuzz stack hash: `182ae0b827`
- PC: `0x55b1f6e327ae`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r13`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9fb7c38d048f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55b1f6e327ae.STACK.182ae0b827.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55b1f6e327ae.STACK.182ae0b827.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55b1f6e327ae.STACK.182ae0b827.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa139f037ae.STACK.182ae0b827.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.65444ceba7ae.STACK.182ae0b827.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r13.pyc`

### 100. cpython-313-bd7e49045219

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f21b3c63`
- Honggfuzz stack hash: `19f21b3c63`
- PC: `0x575d6ed56e6d`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-bd7e49045219.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575d6ed56e6d.STACK.19f21b3c63.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575d6ed56e6d.STACK.19f21b3c63.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575d6ed56e6d.STACK.19f21b3c63.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.576f627e7e6d.STACK.19f21b3c63.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58f31e3d3e6d.STACK.19f21b3c63.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`

### 101. cpython-313-c58ef9df4c79

- Status: crash
- Signal: SIGBUS
- Stack source: honggfuzz-filename
- Stack signature: `SIGBUS:fa313feae`
- Honggfuzz stack hash: `fa313feae`
- PC: `0x5a8ba9ca8960`
- Fault address: `0x74845b900000`
- Instruction: `cmpq___$0x1,0x48(%rax,%rbx,8)`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c58ef9df4c79.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.5a8ba9ca8960.STACK.fa313feae.CODE.2.ADDR.74845b900000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.5a8ba9ca8960.STACK.fa313feae.CODE.2.ADDR.74845b900000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.5a8ba9ca8960.STACK.fa313feae.CODE.2.ADDR.74845b900000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.6038f3023960.STACK.fa313feae.CODE.2.ADDR.76894eb9c000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.60881a82a960.STACK.fa313feae.CODE.2.ADDR.71baedc32000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`

### 102. cpython-313-ce0c4a896be7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c5953f107`
- Honggfuzz stack hash: `c5953f107`
- PC: `0x572d273fb48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ce0c4a896be7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.572d273fb48c.STACK.c5953f107.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.572d273fb48c.STACK.c5953f107.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.572d273fb48c.STACK.c5953f107.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c076b05048c.STACK.c5953f107.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e46e3bb348c.STACK.c5953f107.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 103. cpython-313-fd01f143667f

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:c720497b9`
- Honggfuzz stack hash: `c720497b9`
- PC: `0x77b368f359fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-fd01f143667f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.77b368f359fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.77b368f359fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.77b368f359fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.798131d959fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7fd64633b9fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 104. cpython-313-09879db9f2d7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f36039b9`
- Honggfuzz stack hash: `19f36039b9`
- PC: `0x5e60a116962f`
- Fault address: `0xf8`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-09879db9f2d7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e60a116962f.STACK.19f36039b9.CODE.1.ADDR.f8.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e60a116962f.STACK.19f36039b9.CODE.1.ADDR.f8.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e60a116962f.STACK.19f36039b9.CODE.1.ADDR.f8.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fced288f6b3.STACK.19f36039b9.CODE.128.ADDR.0.INSTR.call___*%r14.pyc`

### 105. cpython-313-0c065fed8971

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197e9bf2d3`
- Honggfuzz stack hash: `197e9bf2d3`
- PC: `0x6183ebcac43e`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0c065fed8971.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6183ebcac43e.STACK.197e9bf2d3.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6183ebcac43e.STACK.197e9bf2d3.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6183ebcac43e.STACK.197e9bf2d3.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63ee7f04043e.STACK.197e9bf2d3.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r12.pyc`

### 106. cpython-313-13b00fcd4bba

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193639c21b`
- Honggfuzz stack hash: `193639c21b`
- PC: `0x5e03fb102077`
- Fault address: `0xa`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-13b00fcd4bba.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e03fb102077.STACK.193639c21b.CODE.1.ADDR.a.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e03fb102077.STACK.193639c21b.CODE.1.ADDR.a.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e03fb102077.STACK.193639c21b.CODE.1.ADDR.a.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e63f6613077.STACK.193639c21b.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`

### 107. cpython-313-17373ed44d17

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e42ca8974`
- Honggfuzz stack hash: `e42ca8974`
- PC: `0x5a7934e6a7ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-17373ed44d17.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a7934e6a7ef.STACK.e42ca8974.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a7934e6a7ef.STACK.e42ca8974.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a7934e6a7ef.STACK.e42ca8974.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.614a7644d7ef.STACK.e42ca8974.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 108. cpython-313-25e6360db24f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f66cf874`
- Honggfuzz stack hash: `18f66cf874`
- PC: `0x5866cd8bd950`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r12),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-25e6360db24f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5866cd8bd950.STACK.18f66cf874.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5866cd8bd950.STACK.18f66cf874.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5866cd8bd950.STACK.18f66cf874.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ce5f6348980.STACK.18f66cf874.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`

### 109. cpython-313-30f3d88050d8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a28600155`
- Honggfuzz stack hash: `1a28600155`
- PC: `0x5877d1244e96`
- Fault address: `0x7810e9fe8955`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-30f3d88050d8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5877d1244e96.STACK.1a28600155.CODE.1.ADDR.7810e9fe8955.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5877d1244e96.STACK.1a28600155.CODE.1.ADDR.7810e9fe8955.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5877d1244e96.STACK.1a28600155.CODE.1.ADDR.7810e9fe8955.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eea8fd45e96.STACK.1a28600155.CODE.1.ADDR.7810e9fe8955.INSTR.mov____0x8(%r13),%r14.pyc`

### 110. cpython-313-329439676076

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e03309d6c`
- Honggfuzz stack hash: `e03309d6c`
- PC: `0x60701ea7b7eb`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-329439676076.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60701ea7b7eb.STACK.e03309d6c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60701ea7b7eb.STACK.e03309d6c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60701ea7b7eb.STACK.e03309d6c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60ed9b8977eb.STACK.e03309d6c.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`

### 111. cpython-313-390e45bf1f4e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1873b0e117`
- Honggfuzz stack hash: `1873b0e117`
- PC: `0x60714fe08d55`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-390e45bf1f4e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60714fe08d55.STACK.1873b0e117.CODE.128.ADDR.0.INSTR.mov____(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60714fe08d55.STACK.1873b0e117.CODE.128.ADDR.0.INSTR.mov____(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60714fe08d55.STACK.1873b0e117.CODE.128.ADDR.0.INSTR.mov____(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64597c8140f1.STACK.1873b0e117.CODE.1.ADDR.41.INSTR.mov____(%r12),%ebx.pyc`

### 112. cpython-313-390f6f081676

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ca496e774`
- Honggfuzz stack hash: `ca496e774`
- PC: `0x5975f2feb608`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-390f6f081676.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5975f2feb608.STACK.ca496e774.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5975f2feb608.STACK.ca496e774.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5975f2feb608.STACK.ca496e774.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.644ad488a608.STACK.ca496e774.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r12.pyc`

### 113. cpython-313-3a9f3c093376

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a67e7aef8`
- Honggfuzz stack hash: `1a67e7aef8`
- PC: `0x60cc1dd55fdd`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3a9f3c093376.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60cc1dd55fdd.STACK.1a67e7aef8.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60cc1dd55fdd.STACK.1a67e7aef8.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60cc1dd55fdd.STACK.1a67e7aef8.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60eeee61bfdd.STACK.1a67e7aef8.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`

### 114. cpython-313-3c22138e2541

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a57f2e548`
- Honggfuzz stack hash: `1a57f2e548`
- PC: `0x5d55aa5322b3`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r14),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3c22138e2541.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d55aa5322b3.STACK.1a57f2e548.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d55aa5322b3.STACK.1a57f2e548.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d55aa5322b3.STACK.1a57f2e548.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.65489c8402b3.STACK.1a57f2e548.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r12.pyc`

### 115. cpython-313-45460386dc16

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b6bc096bd`
- Honggfuzz stack hash: `1b6bc096bd`
- PC: `0x55a7fb023261`
- Fault address: `0x1`
- Instruction: `mov____(%r14),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-45460386dc16.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a7fb023261.STACK.1b6bc096bd.CODE.1.ADDR.1.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a7fb023261.STACK.1b6bc096bd.CODE.1.ADDR.1.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55a7fb023261.STACK.1b6bc096bd.CODE.1.ADDR.1.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57bad0a61396.STACK.1b6bc096bd.CODE.1.ADDR.1.INSTR.mov____(%r15),%ebx.pyc`

### 116. cpython-313-4bd83ccc7d70

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c20ae3e2a`
- Honggfuzz stack hash: `c20ae3e2a`
- PC: `0x610f5ea6f3b4`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r14),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4bd83ccc7d70.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.610f5ea6f3b4.STACK.c20ae3e2a.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.610f5ea6f3b4.STACK.c20ae3e2a.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.610f5ea6f3b4.STACK.c20ae3e2a.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.648a817393e6.STACK.c20ae3e2a.CODE.1.ADDR.f.INSTR.mov____0x0(%r13),%ebx.pyc`

### 117. cpython-313-578d7a4cf233

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b4d65d525`
- Honggfuzz stack hash: `1b4d65d525`
- PC: `0x592531cd324d`
- Fault address: `0x20`
- Instruction: `mov____0x20(%rax),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-578d7a4cf233.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.592531cd324d.STACK.1b4d65d525.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.592531cd324d.STACK.1b4d65d525.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.592531cd324d.STACK.1b4d65d525.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c900dd0f24d.STACK.1b4d65d525.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`

### 118. cpython-313-58deb18341fe

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e20f4faed`
- Honggfuzz stack hash: `e20f4faed`
- PC: `0x58a5a582d48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-58deb18341fe.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a582d48c.STACK.e20f4faed.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a582d48c.STACK.e20f4faed.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a5a582d48c.STACK.e20f4faed.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.591aecfd148c.STACK.e20f4faed.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 119. cpython-313-593f0c4f49e0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fa313feae`
- Honggfuzz stack hash: `fa313feae`
- PC: `0x6072e95ddffc`
- Fault address: `0x60733159e000`
- Instruction: `movq___$0x0,0x48(%rax,%rbx,8)`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-593f0c4f49e0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6072e95ddffc.STACK.fa313feae.CODE.1.ADDR.60733159e000.INSTR.movq___$0x0,0x48(%rax,%rbx,8).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6072e95ddffc.STACK.fa313feae.CODE.1.ADDR.60733159e000.INSTR.movq___$0x0,0x48(%rax,%rbx,8).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6072e95ddffc.STACK.fa313feae.CODE.1.ADDR.60733159e000.INSTR.movq___$0x0,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60be948011fc.STACK.fa313feae.CODE.1.ADDR.0.INSTR.mov____(%r15),%rbx.pyc`

### 120. cpython-313-5c4fa7d7c4c3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ebf97da3d`
- Honggfuzz stack hash: `ebf97da3d`
- PC: `0x5895943f0d64`
- Fault address: `0x10`
- Instruction: `mov____0x10(%r13),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-5c4fa7d7c4c3.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5895943f0d64.STACK.ebf97da3d.CODE.1.ADDR.10.INSTR.mov____0x10(%r13),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5895943f0d64.STACK.ebf97da3d.CODE.1.ADDR.10.INSTR.mov____0x10(%r13),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5895943f0d64.STACK.ebf97da3d.CODE.1.ADDR.10.INSTR.mov____0x10(%r13),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64faefa25d64.STACK.ebf97da3d.CODE.1.ADDR.10.INSTR.mov____0x10(%r13),%r12.pyc`

### 121. cpython-313-64546f8592cb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b75fd6e2e`
- Honggfuzz stack hash: `1b75fd6e2e`
- PC: `0x59d83ff5168b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-64546f8592cb.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59d83ff5168b.STACK.1b75fd6e2e.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59d83ff5168b.STACK.1b75fd6e2e.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59d83ff5168b.STACK.1b75fd6e2e.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60644fcdf68b.STACK.1b75fd6e2e.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`

### 122. cpython-313-6788250b0fef

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cbcaf2d66`
- Honggfuzz stack hash: `cbcaf2d66`
- PC: `0x6168e220d86f`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6788250b0fef.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6168e220d86f.STACK.cbcaf2d66.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6168e220d86f.STACK.cbcaf2d66.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6168e220d86f.STACK.cbcaf2d66.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64e09074c86f.STACK.cbcaf2d66.CODE.1.ADDR.9.INSTR.mov____0x8(%r14),%rax.pyc`

### 123. cpython-313-69b580729ac2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b8ebf13c`
- Honggfuzz stack hash: `19b8ebf13c`
- PC: `0x55f21aacb9c8`
- Fault address: `0x41131ed83`
- Instruction: `mov____0x180(%rbx),%r14d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-69b580729ac2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f21aacb9c8.STACK.19b8ebf13c.CODE.1.ADDR.41131ed83.INSTR.mov____0x180(%rbx),%r14d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f21aacb9c8.STACK.19b8ebf13c.CODE.1.ADDR.41131ed83.INSTR.mov____0x180(%rbx),%r14d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55f21aacb9c8.STACK.19b8ebf13c.CODE.1.ADDR.41131ed83.INSTR.mov____0x180(%rbx),%r14d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.621337a229c8.STACK.19b8ebf13c.CODE.128.ADDR.0.INSTR.mov____0x180(%rbx),%r14d.pyc`

### 124. cpython-313-6c0a799f328f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1868fad025`
- Honggfuzz stack hash: `1868fad025`
- PC: `0x586796ebe2ce`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6c0a799f328f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.586796ebe2ce.STACK.1868fad025.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.586796ebe2ce.STACK.1868fad025.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.586796ebe2ce.STACK.1868fad025.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fe8eb9e52ce.STACK.1868fad025.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r13.pyc`

### 125. cpython-313-811b32e8f8e6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b38faf6f`
- Honggfuzz stack hash: `19b38faf6f`
- PC: `0x56d059bc3920`
- Fault address: `0x0`
- Instruction: `mov____0x158(%rbx),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-811b32e8f8e6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d059bc3920.STACK.19b38faf6f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d059bc3920.STACK.19b38faf6f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56d059bc3920.STACK.19b38faf6f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e0e46e95920.STACK.19b38faf6f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`

### 126. cpython-313-8b1d9ac79041

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ebb1b1c03`
- Honggfuzz stack hash: `ebb1b1c03`
- PC: `0x5a91bb39bd82`
- Fault address: `0x0`
- Instruction: `movaps_%xmm0,-0x50(%rbp)`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8b1d9ac79041.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a91bb39bd82.STACK.ebb1b1c03.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a91bb39bd82.STACK.ebb1b1c03.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a91bb39bd82.STACK.ebb1b1c03.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.600e059d5d82.STACK.ebb1b1c03.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`

### 127. cpython-313-8b8bba9e67de

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1889dfa4f9`
- Honggfuzz stack hash: `1889dfa4f9`
- PC: `0x575c84a1c837`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8b8bba9e67de.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575c84a1c837.STACK.1889dfa4f9.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575c84a1c837.STACK.1889dfa4f9.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.575c84a1c837.STACK.1889dfa4f9.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60dc98254837.STACK.1889dfa4f9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`

### 128. cpython-313-989f85653227

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db8c57f73`
- Honggfuzz stack hash: `db8c57f73`
- PC: `0x5aa06650032f`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-989f85653227.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa06650032f.STACK.db8c57f73.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa06650032f.STACK.db8c57f73.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aa06650032f.STACK.db8c57f73.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.647af163b32f.STACK.db8c57f73.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 129. cpython-313-9d45011eb05d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:da22e1052`
- Honggfuzz stack hash: `da22e1052`
- PC: `0x5e9802b570bc`
- Fault address: `0x0`
- Instruction: `mov____(%r14,%rbx,8),%r14`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9d45011eb05d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e9802b570bc.STACK.da22e1052.CODE.128.ADDR.0.INSTR.mov____(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e9802b570bc.STACK.da22e1052.CODE.128.ADDR.0.INSTR.mov____(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5e9802b570bc.STACK.da22e1052.CODE.128.ADDR.0.INSTR.mov____(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.653d13a030bc.STACK.da22e1052.CODE.128.ADDR.0.INSTR.mov____(%r14,%rbx,8),%r14.pyc`

### 130. cpython-313-9ec77fed266a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a31de9c01`
- Honggfuzz stack hash: `1a31de9c01`
- PC: `0x5563818e448c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9ec77fed266a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5563818e448c.STACK.1a31de9c01.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5563818e448c.STACK.1a31de9c01.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5563818e448c.STACK.1a31de9c01.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b7e0488448c.STACK.1a31de9c01.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 131. cpython-313-a85e90a31081

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1935c4f066`
- Honggfuzz stack hash: `1935c4f066`
- PC: `0x5d2ea54f676f`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a85e90a31081.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d2ea54f676f.STACK.1935c4f066.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d2ea54f676f.STACK.1935c4f066.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d2ea54f676f.STACK.1935c4f066.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.62543e99276f.STACK.1935c4f066.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`

### 132. cpython-313-ace318db6377

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b0328ea35`
- Honggfuzz stack hash: `1b0328ea35`
- PC: `0x7d58b31ce9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ace318db6377.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d58b31ce9fc.STACK.1b0328ea35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d58b31ce9fc.STACK.1b0328ea35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d58b31ce9fc.STACK.1b0328ea35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7e1374b1f9fc.STACK.1b0328ea35.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 133. cpython-313-ae532bd9d2a9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b5c37165`
- Honggfuzz stack hash: `18b5c37165`
- PC: `0x55ad5612e9cf`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r15),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ae532bd9d2a9.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ad5612e9cf.STACK.18b5c37165.CODE.1.ADDR.ffffffff.INSTR.mov____(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ad5612e9cf.STACK.18b5c37165.CODE.1.ADDR.ffffffff.INSTR.mov____(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ad5612e9cf.STACK.18b5c37165.CODE.1.ADDR.ffffffff.INSTR.mov____(%r15),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56479854a96c.STACK.18b5c37165.CODE.1.ADDR.ffffffff.INSTR.mov____(%r15),%r12.pyc`

### 134. cpython-313-ca852bf160a2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c7a7ac171`
- Honggfuzz stack hash: `c7a7ac171`
- PC: `0x59f342fe15cc`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ca852bf160a2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59f342fe15cc.STACK.c7a7ac171.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59f342fe15cc.STACK.c7a7ac171.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59f342fe15cc.STACK.c7a7ac171.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c9f3fda35cc.STACK.c7a7ac171.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r12),%rax.pyc`

### 135. cpython-313-d065b3eaa19b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a28114763`
- Honggfuzz stack hash: `1a28114763`
- PC: `0x61b730b85b84`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d065b3eaa19b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61b730b85b84.STACK.1a28114763.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61b730b85b84.STACK.1a28114763.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61b730b85b84.STACK.1a28114763.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.62d539ff8b84.STACK.1a28114763.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`

### 136. cpython-313-de180ada4603

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f40eeebb0`
- Honggfuzz stack hash: `f40eeebb0`
- PC: `0x5d4643141e7e`
- Fault address: `0x30`
- Instruction: `mov____0x30(%rax),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-de180ada4603.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d4643141e7e.STACK.f40eeebb0.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d4643141e7e.STACK.f40eeebb0.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d4643141e7e.STACK.f40eeebb0.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5dff43bdfa9a.STACK.f40eeebb0.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%rax.pyc`

### 137. cpython-313-de741779cdd3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a6952992f`
- Honggfuzz stack hash: `1a6952992f`
- PC: `0x57db217ca920`
- Fault address: `0x0`
- Instruction: `mov____0x158(%rbx),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-de741779cdd3.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57db217ca920.STACK.1a6952992f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57db217ca920.STACK.1a6952992f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57db217ca920.STACK.1a6952992f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ca4f112e920.STACK.1a6952992f.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`

### 138. cpython-313-e0a78dec4980

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bd69d00c2`
- Honggfuzz stack hash: `1bd69d00c2`
- PC: `0x73b64e2c671f`
- Fault address: `0x0`
- Instruction: `cmp____(%rdi,%rax,1),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e0a78dec4980.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.73b64e2c671f.STACK.1bd69d00c2.CODE.128.ADDR.0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.73b64e2c671f.STACK.1bd69d00c2.CODE.128.ADDR.0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.73b64e2c671f.STACK.1bd69d00c2.CODE.128.ADDR.0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7d49f3f1d71f.STACK.1bd69d00c2.CODE.128.ADDR.0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`

### 139. cpython-313-eb4fe0297900

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e00edcdd3`
- Honggfuzz stack hash: `e00edcdd3`
- PC: `0x5b822ffb824d`
- Fault address: `0x20`
- Instruction: `mov____0x20(%rax),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-eb4fe0297900.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b822ffb824d.STACK.e00edcdd3.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b822ffb824d.STACK.e00edcdd3.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b822ffb824d.STACK.e00edcdd3.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d2e996b224d.STACK.e00edcdd3.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`

### 140. cpython-313-fb7fc714c467

- Status: crash
- Signal: SIGBUS
- Stack source: honggfuzz-filename
- Stack signature: `SIGBUS:1ab3250001`
- Honggfuzz stack hash: `1ab3250001`
- PC: `0x56f97a41b960`
- Fault address: `0x7cab4722b000`
- Instruction: `cmpq___$0x1,0x48(%rax,%rbx,8)`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-fb7fc714c467.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.56f97a41b960.STACK.1ab3250001.CODE.2.ADDR.7cab4722b000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.56f97a41b960.STACK.1ab3250001.CODE.2.ADDR.7cab4722b000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.56f97a41b960.STACK.1ab3250001.CODE.2.ADDR.7cab4722b000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGBUS.PC.5be31376c960.STACK.1ab3250001.CODE.2.ADDR.73b2756ee000.INSTR.cmpq___$0x1,0x48(%rax,%rbx,8).pyc`

### 141. cpython-313-00bd8c82af22

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b03f2aa71`
- Honggfuzz stack hash: `1b03f2aa71`
- PC: `0x70d444bd29fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-00bd8c82af22.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70d444bd29fc.STACK.1b03f2aa71.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70d444bd29fc.STACK.1b03f2aa71.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.70d444bd29fc.STACK.1b03f2aa71.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 142. cpython-313-0461c83caf3f

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:1b459bde96`
- Honggfuzz stack hash: `1b459bde96`
- PC: `0x7d3cb16fd9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0461c83caf3f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d3cb16fd9fc.STACK.1b459bde96.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d3cb16fd9fc.STACK.1b459bde96.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d3cb16fd9fc.STACK.1b459bde96.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 143. cpython-313-0580938bd56b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18721e7142`
- Honggfuzz stack hash: `18721e7142`
- PC: `0x5b29625497ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0580938bd56b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b29625497ef.STACK.18721e7142.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b29625497ef.STACK.18721e7142.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b29625497ef.STACK.18721e7142.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 144. cpython-313-07045726f31a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f7872ad2`
- Honggfuzz stack hash: `18f7872ad2`
- PC: `0x6040fb97cb7b`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-07045726f31a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6040fb97cb7b.STACK.18f7872ad2.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6040fb97cb7b.STACK.18f7872ad2.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6040fb97cb7b.STACK.18f7872ad2.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%ebx.pyc`

### 145. cpython-313-0e21002d1965

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1aca2047d4`
- Honggfuzz stack hash: `1aca2047d4`
- PC: `0x6505a982124d`
- Fault address: `0x20`
- Instruction: `mov____0x20(%rax),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-0e21002d1965.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6505a982124d.STACK.1aca2047d4.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6505a982124d.STACK.1aca2047d4.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6505a982124d.STACK.1aca2047d4.CODE.1.ADDR.20.INSTR.mov____0x20(%rax),%r13.pyc`

### 146. cpython-313-119ff7d38eda

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dbecfd961`
- Honggfuzz stack hash: `dbecfd961`
- PC: `0x5bead259c8d0`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r14),%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-119ff7d38eda.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bead259c8d0.STACK.dbecfd961.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bead259c8d0.STACK.dbecfd961.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5bead259c8d0.STACK.dbecfd961.CODE.1.ADDR.ffffffff.INSTR.mov____(%r14),%r13d.pyc`

### 147. cpython-313-13f25b6f0b11

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c35bcd182`
- Honggfuzz stack hash: `c35bcd182`
- PC: `0x7cf13ef7c795`
- Fault address: `0x39`
- Instruction: `mov____-0x8(%rbp),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-13f25b6f0b11.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7cf13ef7c795.STACK.c35bcd182.CODE.1.ADDR.39.INSTR.mov____-0x8(%rbp),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7cf13ef7c795.STACK.c35bcd182.CODE.1.ADDR.39.INSTR.mov____-0x8(%rbp),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7cf13ef7c795.STACK.c35bcd182.CODE.1.ADDR.39.INSTR.mov____-0x8(%rbp),%rax.pyc`

### 148. cpython-313-1bc9ccbfc6bb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18548046b7`
- Honggfuzz stack hash: `18548046b7`
- PC: `0x5b49b98594c9`
- Fault address: `0x0`
- Instruction: `mov____(%r12),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1bc9ccbfc6bb.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b49b98594c9.STACK.18548046b7.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b49b98594c9.STACK.18548046b7.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b49b98594c9.STACK.18548046b7.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15.pyc`

### 149. cpython-313-1bee2075bab9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c782a0116`
- Honggfuzz stack hash: `c782a0116`
- PC: `0x5a750b8def90`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-1bee2075bab9.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a750b8def90.STACK.c782a0116.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a750b8def90.STACK.c782a0116.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a750b8def90.STACK.c782a0116.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%rax.pyc`

### 150. cpython-313-20a66c8d0836

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:db73cfd37`
- Honggfuzz stack hash: `db73cfd37`
- PC: `0x7eeb1f5139fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-20a66c8d0836.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7eeb1f5139fc.STACK.db73cfd37.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7eeb1f5139fc.STACK.db73cfd37.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7eeb1f5139fc.STACK.db73cfd37.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 151. cpython-313-240219fd96c1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cb6330e16`
- Honggfuzz stack hash: `cb6330e16`
- PC: `0x5feecda837eb`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-240219fd96c1.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5feecda837eb.STACK.cb6330e16.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5feecda837eb.STACK.cb6330e16.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5feecda837eb.STACK.cb6330e16.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`

### 152. cpython-313-251ef333e6f0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f596a72dd`
- Honggfuzz stack hash: `f596a72dd`
- PC: `0x7c7fd4c53449`
- Fault address: `0x5b6504000000`
- Instruction: `mov____(%rax),%rdi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-251ef333e6f0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7c7fd4c53449.STACK.f596a72dd.CODE.1.ADDR.5b6504000000.INSTR.mov____(%rax),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7c7fd4c53449.STACK.f596a72dd.CODE.1.ADDR.5b6504000000.INSTR.mov____(%rax),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7c7fd4c53449.STACK.f596a72dd.CODE.1.ADDR.5b6504000000.INSTR.mov____(%rax),%rdi.pyc`

### 153. cpython-313-277d29178c82

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f5d181c7c`
- Honggfuzz stack hash: `f5d181c7c`
- PC: `0x5affc50d5e8f`
- Fault address: `0x90`
- Instruction: `mov____0x90(%r13),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-277d29178c82.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5affc50d5e8f.STACK.f5d181c7c.CODE.1.ADDR.90.INSTR.mov____0x90(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5affc50d5e8f.STACK.f5d181c7c.CODE.1.ADDR.90.INSTR.mov____0x90(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5affc50d5e8f.STACK.f5d181c7c.CODE.1.ADDR.90.INSTR.mov____0x90(%r13),%rbx.pyc`

### 154. cpython-313-28d304ee9adc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bc8f816e9`
- Honggfuzz stack hash: `1bc8f816e9`
- PC: `0x5d6162523a9a`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-28d304ee9adc.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6162523a9a.STACK.1bc8f816e9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6162523a9a.STACK.1bc8f816e9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6162523a9a.STACK.1bc8f816e9.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rax.pyc`

### 155. cpython-313-2aad2a218d35

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3acefd77`
- Honggfuzz stack hash: `c3acefd77`
- PC: `0x593f2aa47063`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rax),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2aad2a218d35.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.593f2aa47063.STACK.c3acefd77.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.593f2aa47063.STACK.c3acefd77.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.593f2aa47063.STACK.c3acefd77.CODE.1.ADDR.8.INSTR.mov____0x8(%rax),%rax.pyc`

### 156. cpython-313-2e3d7630a9bc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f2431c22a`
- Honggfuzz stack hash: `f2431c22a`
- PC: `0x63a03b23ff90`
- Fault address: `0x0`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-2e3d7630a9bc.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63a03b23ff90.STACK.f2431c22a.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63a03b23ff90.STACK.f2431c22a.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63a03b23ff90.STACK.f2431c22a.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%rax.pyc`

### 157. cpython-313-316b863bfc88

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:efb091a7b`
- Honggfuzz stack hash: `efb091a7b`
- PC: `0x563d7165048c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-316b863bfc88.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563d7165048c.STACK.efb091a7b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563d7165048c.STACK.efb091a7b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.563d7165048c.STACK.efb091a7b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 158. cpython-313-3a020f9937b3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18af037ef7`
- Honggfuzz stack hash: `18af037ef7`
- PC: `0x74dfb766b88d`
- Fault address: `0x74df975cfd60`
- Instruction: `vmovdqu_(%rsi),%ymm0`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3a020f9937b3.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.74dfb766b88d.STACK.18af037ef7.CODE.1.ADDR.74df975cfd60.INSTR.vmovdqu_(%rsi),%ymm0.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.74dfb766b88d.STACK.18af037ef7.CODE.1.ADDR.74df975cfd60.INSTR.vmovdqu_(%rsi),%ymm0.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.74dfb766b88d.STACK.18af037ef7.CODE.1.ADDR.74df975cfd60.INSTR.vmovdqu_(%rsi),%ymm0.pyc`

### 159. cpython-313-3e5cfc440e9d

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f78fb5c47`
- Honggfuzz stack hash: `f78fb5c47`
- PC: `0x7048ddb749fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-3e5cfc440e9d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7048ddb749fc.STACK.f78fb5c47.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7048ddb749fc.STACK.f78fb5c47.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7048ddb749fc.STACK.f78fb5c47.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 160. cpython-313-437a25de9c4c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1acf88d9cc`
- Honggfuzz stack hash: `1acf88d9cc`
- PC: `0x5a5228f1648c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-437a25de9c4c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a5228f1648c.STACK.1acf88d9cc.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a5228f1648c.STACK.1acf88d9cc.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5a5228f1648c.STACK.1acf88d9cc.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 161. cpython-313-43d2447f4640

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193ed0a330`
- Honggfuzz stack hash: `193ed0a330`
- PC: `0x5d71192ab95f`
- Fault address: `0x8`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-43d2447f4640.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d71192ab95f.STACK.193ed0a330.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d71192ab95f.STACK.193ed0a330.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d71192ab95f.STACK.193ed0a330.CODE.1.ADDR.8.INSTR.mov____(%r14),%ebx.pyc`

### 162. cpython-313-4495e50f68c0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f8345f47a`
- Honggfuzz stack hash: `f8345f47a`
- PC: `0x75d0fd8ff229`
- Fault address: `0x0`
- Instruction: `xor____(%rax),%rsi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4495e50f68c0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.75d0fd8ff229.STACK.f8345f47a.CODE.128.ADDR.0.INSTR.xor____(%rax),%rsi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.75d0fd8ff229.STACK.f8345f47a.CODE.128.ADDR.0.INSTR.xor____(%rax),%rsi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.75d0fd8ff229.STACK.f8345f47a.CODE.128.ADDR.0.INSTR.xor____(%rax),%rsi.pyc`

### 163. cpython-313-4925b1780ebd

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:180ffff1b2`
- Honggfuzz stack hash: `180ffff1b2`
- PC: `0x5fe16c41c0f9`
- Fault address: `0x4`
- Instruction: `mov____(%r15),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4925b1780ebd.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fe16c41c0f9.STACK.180ffff1b2.CODE.1.ADDR.4.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fe16c41c0f9.STACK.180ffff1b2.CODE.1.ADDR.4.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fe16c41c0f9.STACK.180ffff1b2.CODE.1.ADDR.4.INSTR.mov____(%r15),%ebx.pyc`

### 164. cpython-313-4c5b0f8c82b7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db51acc73`
- Honggfuzz stack hash: `db51acc73`
- PC: `0x5fddd3dcb7bf`
- Fault address: `0x71`
- Instruction: `mov____0x30(%rax),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4c5b0f8c82b7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fddd3dcb7bf.STACK.db51acc73.CODE.1.ADDR.71.INSTR.mov____0x30(%rax),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fddd3dcb7bf.STACK.db51acc73.CODE.1.ADDR.71.INSTR.mov____0x30(%rax),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fddd3dcb7bf.STACK.db51acc73.CODE.1.ADDR.71.INSTR.mov____0x30(%rax),%r15.pyc`

### 165. cpython-313-4f400f074785

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18794fe741`
- Honggfuzz stack hash: `18794fe741`
- PC: `0x77588311c8bd`
- Fault address: `0x0`
- Instruction: `vpcmpeqb_(%rdi),%ymm0,%ymm1`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4f400f074785.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.77588311c8bd.STACK.18794fe741.CODE.128.ADDR.0.INSTR.vpcmpeqb_(%rdi),%ymm0,%ymm1.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.77588311c8bd.STACK.18794fe741.CODE.128.ADDR.0.INSTR.vpcmpeqb_(%rdi),%ymm0,%ymm1.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.77588311c8bd.STACK.18794fe741.CODE.128.ADDR.0.INSTR.vpcmpeqb_(%rdi),%ymm0,%ymm1.pyc`

### 166. cpython-313-4f4dce922887

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1874bf455c`
- Honggfuzz stack hash: `1874bf455c`
- PC: `0x55e0b010e48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-4f4dce922887.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e0b010e48c.STACK.1874bf455c.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e0b010e48c.STACK.1874bf455c.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55e0b010e48c.STACK.1874bf455c.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 167. cpython-313-51c18548f524

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1839e3c313`
- Honggfuzz stack hash: `1839e3c313`
- PC: `0x7629423f9449`
- Fault address: `0x5c01f0000000`
- Instruction: `mov____(%rax),%rdi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-51c18548f524.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7629423f9449.STACK.1839e3c313.CODE.1.ADDR.5c01f0000000.INSTR.mov____(%rax),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7629423f9449.STACK.1839e3c313.CODE.1.ADDR.5c01f0000000.INSTR.mov____(%rax),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7629423f9449.STACK.1839e3c313.CODE.1.ADDR.5c01f0000000.INSTR.mov____(%rax),%rdi.pyc`

### 168. cpython-313-593237368bab

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf6720537`
- Honggfuzz stack hash: `cf6720537`
- PC: `0x732590748449`
- Fault address: `0x5f610c000000`
- Instruction: `mov____(%rax),%rdi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-593237368bab.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.732590748449.STACK.cf6720537.CODE.1.ADDR.5f610c000000.INSTR.mov____(%rax),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.732590748449.STACK.cf6720537.CODE.1.ADDR.5f610c000000.INSTR.mov____(%rax),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.732590748449.STACK.cf6720537.CODE.1.ADDR.5f610c000000.INSTR.mov____(%rax),%rdi.pyc`

### 169. cpython-313-59893f04ede1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c7c81dd13`
- Honggfuzz stack hash: `c7c81dd13`
- PC: `0x7e0c98bc5900`
- Fault address: `0x0`
- Instruction: `mov____-0x8(%rsi,%rdx,1),%rcx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-59893f04ede1.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7e0c98bc5900.STACK.c7c81dd13.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7e0c98bc5900.STACK.c7c81dd13.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7e0c98bc5900.STACK.c7c81dd13.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`

### 170. cpython-313-5bb05796a411

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b63b749e`
- Honggfuzz stack hash: `18b63b749e`
- PC: `0x64dfbe9ba7eb`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-5bb05796a411.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64dfbe9ba7eb.STACK.18b63b749e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64dfbe9ba7eb.STACK.18b63b749e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64dfbe9ba7eb.STACK.18b63b749e.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r15.pyc`

### 171. cpython-313-5ed49e6260fe

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1971aa89c2`
- Honggfuzz stack hash: `1971aa89c2`
- PC: `0x5eedbb73d920`
- Fault address: `0x6045`
- Instruction: `mov____0x158(%rbx),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-5ed49e6260fe.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eedbb73d920.STACK.1971aa89c2.CODE.1.ADDR.6045.INSTR.mov____0x158(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eedbb73d920.STACK.1971aa89c2.CODE.1.ADDR.6045.INSTR.mov____0x158(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eedbb73d920.STACK.1971aa89c2.CODE.1.ADDR.6045.INSTR.mov____0x158(%rbx),%r13.pyc`

### 172. cpython-313-60e188fe2eb4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c714f9415`
- Honggfuzz stack hash: `c714f9415`
- PC: `0x641fe57e3a7e`
- Fault address: `0x0`
- Instruction: `mov____0x78(%r15),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-60e188fe2eb4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.641fe57e3a7e.STACK.c714f9415.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.641fe57e3a7e.STACK.c714f9415.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.641fe57e3a7e.STACK.c714f9415.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`

### 173. cpython-313-6148292ae7da

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:ecf651792`
- Honggfuzz stack hash: `ecf651792`
- PC: `0x79884f5e89fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6148292ae7da.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.79884f5e89fc.STACK.ecf651792.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.79884f5e89fc.STACK.ecf651792.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.79884f5e89fc.STACK.ecf651792.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 174. cpython-313-6181a4bdfcc2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cfbca7a25`
- Honggfuzz stack hash: `cfbca7a25`
- PC: `0x58a4cb2f63dd`
- Fault address: `0x0`
- Instruction: `mov____%rbx,(%rax)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6181a4bdfcc2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a4cb2f63dd.STACK.cfbca7a25.CODE.1.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a4cb2f63dd.STACK.cfbca7a25.CODE.1.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58a4cb2f63dd.STACK.cfbca7a25.CODE.1.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`

### 175. cpython-313-61c8ecd43574

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cff40e9df`
- Honggfuzz stack hash: `cff40e9df`
- PC: `0x6147fb8c362f`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-61c8ecd43574.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6147fb8c362f.STACK.cff40e9df.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6147fb8c362f.STACK.cff40e9df.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6147fb8c362f.STACK.cff40e9df.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`

### 176. cpython-313-65efe1cae49d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b0a34b5ff`
- Honggfuzz stack hash: `1b0a34b5ff`
- PC: `0x56b3d555a037`
- Fault address: `0x1d9`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-65efe1cae49d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56b3d555a037.STACK.1b0a34b5ff.CODE.1.ADDR.1d9.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56b3d555a037.STACK.1b0a34b5ff.CODE.1.ADDR.1d9.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56b3d555a037.STACK.1b0a34b5ff.CODE.1.ADDR.1d9.INSTR.mov____0x8(%r13),%rbx.pyc`

### 177. cpython-313-68cc7e23af20

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18562f76c3`
- Honggfuzz stack hash: `18562f76c3`
- PC: `0x5fb471048037`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-68cc7e23af20.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fb471048037.STACK.18562f76c3.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fb471048037.STACK.18562f76c3.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fb471048037.STACK.18562f76c3.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`

### 178. cpython-313-6bb70e6634be

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b5c3a5e9`
- Honggfuzz stack hash: `18b5c3a5e9`
- PC: `0x5fdb0fa86060`
- Fault address: `0x100000017`
- Instruction: `mov____(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-6bb70e6634be.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdb0fa86060.STACK.18b5c3a5e9.CODE.1.ADDR.100000017.INSTR.mov____(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdb0fa86060.STACK.18b5c3a5e9.CODE.1.ADDR.100000017.INSTR.mov____(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdb0fa86060.STACK.18b5c3a5e9.CODE.1.ADDR.100000017.INSTR.mov____(%r14),%rax.pyc`

### 179. cpython-313-70f052247ee4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c09b0df85`
- Honggfuzz stack hash: `c09b0df85`
- PC: `0xffffffff08261114`
- Fault address: `0xffffffff08261114`
- Instruction: `[NOT_MMAPED]`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-70f052247ee4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.ffffffff08261114.STACK.c09b0df85.CODE.1.ADDR.ffffffff08261114.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.ffffffff08261114.STACK.c09b0df85.CODE.1.ADDR.ffffffff08261114.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.ffffffff08261114.STACK.c09b0df85.CODE.1.ADDR.ffffffff08261114.INSTR.[NOT_MMAPED].pyc`

### 180. cpython-313-72b6ef006cff

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e2579eadb`
- Honggfuzz stack hash: `e2579eadb`
- PC: `0x5970916e662f`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-72b6ef006cff.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5970916e662f.STACK.e2579eadb.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5970916e662f.STACK.e2579eadb.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5970916e662f.STACK.e2579eadb.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`

### 181. cpython-313-73d9094770f0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cfac17416`
- Honggfuzz stack hash: `cfac17416`
- PC: `0x64c3508b39b5`
- Fault address: `0xffffffff`
- Instruction: `mov____(%r12),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-73d9094770f0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64c3508b39b5.STACK.cfac17416.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64c3508b39b5.STACK.cfac17416.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64c3508b39b5.STACK.cfac17416.CODE.1.ADDR.ffffffff.INSTR.mov____(%r12),%r13.pyc`

### 182. cpython-313-74ab761bee88

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d3ecc258f`
- Honggfuzz stack hash: `d3ecc258f`
- PC: `0x6006e829e4a3`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-74ab761bee88.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6006e829e4a3.STACK.d3ecc258f.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6006e829e4a3.STACK.d3ecc258f.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6006e829e4a3.STACK.d3ecc258f.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`

### 183. cpython-313-79131be11a0a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a47ca2a81`
- Honggfuzz stack hash: `1a47ca2a81`
- PC: `0x56a65268b3dd`
- Fault address: `0x0`
- Instruction: `mov____%rbx,(%rax)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-79131be11a0a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56a65268b3dd.STACK.1a47ca2a81.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56a65268b3dd.STACK.1a47ca2a81.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.56a65268b3dd.STACK.1a47ca2a81.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`

### 184. cpython-313-794c505461e4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1922f6c7da`
- Honggfuzz stack hash: `1922f6c7da`
- PC: `0x5f6a7154a95f`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-794c505461e4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f6a7154a95f.STACK.1922f6c7da.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f6a7154a95f.STACK.1922f6c7da.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f6a7154a95f.STACK.1922f6c7da.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 185. cpython-313-7a22e6dc6aa4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19a9ef74e9`
- Honggfuzz stack hash: `19a9ef74e9`
- PC: `0x582b33534818`
- Fault address: `0x0`
- Instruction: `movzbl_(%r15,%r14,1),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7a22e6dc6aa4.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.582b33534818.STACK.19a9ef74e9.CODE.128.ADDR.0.INSTR.movzbl_(%r15,%r14,1),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.582b33534818.STACK.19a9ef74e9.CODE.128.ADDR.0.INSTR.movzbl_(%r15,%r14,1),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.582b33534818.STACK.19a9ef74e9.CODE.128.ADDR.0.INSTR.movzbl_(%r15,%r14,1),%ebx.pyc`

### 186. cpython-313-7c73eb0c9e3c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ea45452b5`
- Honggfuzz stack hash: `ea45452b5`
- PC: `0x5c297b0cc980`
- Fault address: `0x0`
- Instruction: `mov____0x100(%rbx),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7c73eb0c9e3c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c297b0cc980.STACK.ea45452b5.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c297b0cc980.STACK.ea45452b5.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c297b0cc980.STACK.ea45452b5.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`

### 187. cpython-313-7d037d3edbf6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e41831c4b`
- Honggfuzz stack hash: `e41831c4b`
- PC: `0x5db24a35a7ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7d037d3edbf6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5db24a35a7ef.STACK.e41831c4b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5db24a35a7ef.STACK.e41831c4b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5db24a35a7ef.STACK.e41831c4b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 188. cpython-313-7e08bd42b83c

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f04560ebc`
- Honggfuzz stack hash: `f04560ebc`
- PC: `0x7134da93e9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-7e08bd42b83c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7134da93e9fc.STACK.f04560ebc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7134da93e9fc.STACK.f04560ebc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7134da93e9fc.STACK.f04560ebc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 189. cpython-313-83d02ce9842f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f1a770e3`
- Honggfuzz stack hash: `18f1a770e3`
- PC: `0x5875df7e648c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-83d02ce9842f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5875df7e648c.STACK.18f1a770e3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5875df7e648c.STACK.18f1a770e3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5875df7e648c.STACK.18f1a770e3.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 190. cpython-313-846a1a857bda

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ce40224d6`
- Honggfuzz stack hash: `ce40224d6`
- PC: `0x5744b09df8c8`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-846a1a857bda.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744b09df8c8.STACK.ce40224d6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744b09df8c8.STACK.ce40224d6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5744b09df8c8.STACK.ce40224d6.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`

### 191. cpython-313-88922b04e32a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18746ed9fe`
- Honggfuzz stack hash: `18746ed9fe`
- PC: `0x55eaf6731849`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-88922b04e32a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55eaf6731849.STACK.18746ed9fe.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55eaf6731849.STACK.18746ed9fe.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55eaf6731849.STACK.18746ed9fe.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`

### 192. cpython-313-88bc4afd353c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b407134b`
- Honggfuzz stack hash: `18b407134b`
- PC: `0x5f16af68648c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-88bc4afd353c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f16af68648c.STACK.18b407134b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f16af68648c.STACK.18b407134b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f16af68648c.STACK.18b407134b.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 193. cpython-313-899320f7d86c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dbcad5049`
- Honggfuzz stack hash: `dbcad5049`
- PC: `0x577d71bbfe6d`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-899320f7d86c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.577d71bbfe6d.STACK.dbcad5049.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.577d71bbfe6d.STACK.dbcad5049.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.577d71bbfe6d.STACK.dbcad5049.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`

### 194. cpython-313-89fd113f3d21

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de67e44ef`
- Honggfuzz stack hash: `de67e44ef`
- PC: `0x61919447048c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-89fd113f3d21.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61919447048c.STACK.de67e44ef.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61919447048c.STACK.de67e44ef.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61919447048c.STACK.de67e44ef.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 195. cpython-313-8bbc8c58678c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19dd84363a`
- Honggfuzz stack hash: `19dd84363a`
- PC: `0x7b51b585d71f`
- Fault address: `0x5a039d7f36e0`
- Instruction: `cmp____(%rdi,%rax,1),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8bbc8c58678c.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7b51b585d71f.STACK.19dd84363a.CODE.1.ADDR.5a039d7f36e0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7b51b585d71f.STACK.19dd84363a.CODE.1.ADDR.5a039d7f36e0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7b51b585d71f.STACK.19dd84363a.CODE.1.ADDR.5a039d7f36e0.INSTR.cmp____(%rdi,%rax,1),%rax.pyc`

### 196. cpython-313-8d786d4a199e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b75ede51f`
- Honggfuzz stack hash: `1b75ede51f`
- PC: `0x5ae6a5bda131`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r12),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8d786d4a199e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6a5bda131.STACK.1b75ede51f.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6a5bda131.STACK.1b75ede51f.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6a5bda131.STACK.1b75ede51f.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%r14.pyc`

### 197. cpython-313-8dbd21026b4d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b972f6891`
- Honggfuzz stack hash: `1b972f6891`
- PC: `0x61cc6bb70e6d`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8dbd21026b4d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cc6bb70e6d.STACK.1b972f6891.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cc6bb70e6d.STACK.1b972f6891.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cc6bb70e6d.STACK.1b972f6891.CODE.128.ADDR.0.INSTR.mov____(%r14),%rbx.pyc`

### 198. cpython-313-8e26ca7de03e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c40f2927a`
- Honggfuzz stack hash: `c40f2927a`
- PC: `0x5826a2953cda`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-8e26ca7de03e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5826a2953cda.STACK.c40f2927a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5826a2953cda.STACK.c40f2927a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5826a2953cda.STACK.c40f2927a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 199. cpython-313-931e9c4fbea5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cff293fe6`
- Honggfuzz stack hash: `cff293fe6`
- PC: `0x5eefceafdb8a`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-931e9c4fbea5.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eefceafdb8a.STACK.cff293fe6.CODE.128.ADDR.0.INSTR.mov____(%r15),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eefceafdb8a.STACK.cff293fe6.CODE.128.ADDR.0.INSTR.mov____(%r15),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5eefceafdb8a.STACK.cff293fe6.CODE.128.ADDR.0.INSTR.mov____(%r15),%r13.pyc`

### 200. cpython-313-956302f4ceef

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18f0f91701`
- Honggfuzz stack hash: `18f0f91701`
- PC: `0x5f0880dde442`
- Fault address: `0xa8`
- Instruction: `mov____0xa8(%r12),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-956302f4ceef.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f0880dde442.STACK.18f0f91701.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r12),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f0880dde442.STACK.18f0f91701.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r12),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f0880dde442.STACK.18f0f91701.CODE.1.ADDR.a8.INSTR.mov____0xa8(%r12),%r13.pyc`

### 201. cpython-313-980688a95294

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197212d927`
- Honggfuzz stack hash: `197212d927`
- PC: `0x5fa6ec67148c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-980688a95294.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ec67148c.STACK.197212d927.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ec67148c.STACK.197212d927.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ec67148c.STACK.197212d927.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 202. cpython-313-9ae582b373ff

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19fa320adc`
- Honggfuzz stack hash: `19fa320adc`
- PC: `0x772ede1f09fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-9ae582b373ff.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.772ede1f09fc.STACK.19fa320adc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.772ede1f09fc.STACK.19fa320adc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.772ede1f09fc.STACK.19fa320adc.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 203. cpython-313-a45fc97732ec

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d7f283547`
- Honggfuzz stack hash: `d7f283547`
- PC: `0x61cfae19b7ef`
- Fault address: `0xe9`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a45fc97732ec.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cfae19b7ef.STACK.d7f283547.CODE.1.ADDR.e9.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cfae19b7ef.STACK.d7f283547.CODE.1.ADDR.e9.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61cfae19b7ef.STACK.d7f283547.CODE.1.ADDR.e9.INSTR.mov____0xa8(%r15),%r12.pyc`

### 204. cpython-313-a670d7f84f8f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:edae88ab7`
- Honggfuzz stack hash: `edae88ab7`
- PC: `0x642c0edab304`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r14),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a670d7f84f8f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.642c0edab304.STACK.edae88ab7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.642c0edab304.STACK.edae88ab7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.642c0edab304.STACK.edae88ab7.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r14),%r12.pyc`

### 205. cpython-313-a8623d4d3af2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1ad5b60bd0`
- Honggfuzz stack hash: `1ad5b60bd0`
- PC: `0x650deda3d48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-a8623d4d3af2.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.650deda3d48c.STACK.1ad5b60bd0.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.650deda3d48c.STACK.1ad5b60bd0.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.650deda3d48c.STACK.1ad5b60bd0.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 206. cpython-313-ab54ef179c4a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e25c87ce2`
- Honggfuzz stack hash: `e25c87ce2`
- PC: `0x63fdd357acfe`
- Fault address: `0xb9`
- Instruction: `movslq_0xb8(%r12),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ab54ef179c4a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63fdd357acfe.STACK.e25c87ce2.CODE.1.ADDR.b9.INSTR.movslq_0xb8(%r12),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63fdd357acfe.STACK.e25c87ce2.CODE.1.ADDR.b9.INSTR.movslq_0xb8(%r12),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63fdd357acfe.STACK.e25c87ce2.CODE.1.ADDR.b9.INSTR.movslq_0xb8(%r12),%rbx.pyc`

### 207. cpython-313-afb11148016e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dcab2a29d`
- Honggfuzz stack hash: `dcab2a29d`
- PC: `0x59659ffdb7ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-afb11148016e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59659ffdb7ef.STACK.dcab2a29d.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59659ffdb7ef.STACK.dcab2a29d.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59659ffdb7ef.STACK.dcab2a29d.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 208. cpython-313-afefe2990619

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a52cf9f69`
- Honggfuzz stack hash: `1a52cf9f69`
- PC: `0x7989acd77840`
- Fault address: `0x61a7400757c0`
- Instruction: `testb__$0x1,0x8(%r14,%r10,1)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-afefe2990619.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7989acd77840.STACK.1a52cf9f69.CODE.1.ADDR.61a7400757c0.INSTR.testb__$0x1,0x8(%r14,%r10,1).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7989acd77840.STACK.1a52cf9f69.CODE.1.ADDR.61a7400757c0.INSTR.testb__$0x1,0x8(%r14,%r10,1).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7989acd77840.STACK.1a52cf9f69.CODE.1.ADDR.61a7400757c0.INSTR.testb__$0x1,0x8(%r14,%r10,1).pyc`

### 209. cpython-313-b07927216b12

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19ee2a935a`
- Honggfuzz stack hash: `19ee2a935a`
- PC: `0x57447e5997eb`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b07927216b12.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57447e5997eb.STACK.19ee2a935a.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57447e5997eb.STACK.19ee2a935a.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.57447e5997eb.STACK.19ee2a935a.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%r15.pyc`

### 210. cpython-313-b0e8da3e3b59

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b0bc0ba8f`
- Honggfuzz stack hash: `1b0bc0ba8f`
- PC: `0x59986f3fb599`
- Fault address: `0xffffff7ae901c78b`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b0e8da3e3b59.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59986f3fb599.STACK.1b0bc0ba8f.CODE.1.ADDR.ffffff7ae901c78b.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59986f3fb599.STACK.1b0bc0ba8f.CODE.1.ADDR.ffffff7ae901c78b.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.59986f3fb599.STACK.1b0bc0ba8f.CODE.1.ADDR.ffffff7ae901c78b.INSTR.mov____0x8(%rbx),%rax.pyc`

### 211. cpython-313-b484f968181e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e7d428a34`
- Honggfuzz stack hash: `e7d428a34`
- PC: `0x5d6ae612e48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b484f968181e.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6ae612e48c.STACK.e7d428a34.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6ae612e48c.STACK.e7d428a34.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d6ae612e48c.STACK.e7d428a34.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 212. cpython-313-b72fb1a77ad7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fa32393c9`
- Honggfuzz stack hash: `fa32393c9`
- PC: `0x652d73857e16`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b72fb1a77ad7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.652d73857e16.STACK.fa32393c9.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.652d73857e16.STACK.fa32393c9.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.652d73857e16.STACK.fa32393c9.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`

### 213. cpython-313-b841a991c1ba

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:f4760f1ae`
- Honggfuzz stack hash: `f4760f1ae`
- PC: `0x7d7b6da2e9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b841a991c1ba.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d7b6da2e9fc.STACK.f4760f1ae.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d7b6da2e9fc.STACK.f4760f1ae.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGABRT.PC.7d7b6da2e9fc.STACK.f4760f1ae.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 214. cpython-313-b86db31504fd

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f213bb4c3`
- Honggfuzz stack hash: `f213bb4c3`
- PC: `0x5b2adab51860`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-b86db31504fd.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2adab51860.STACK.f213bb4c3.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2adab51860.STACK.f213bb4c3.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b2adab51860.STACK.f213bb4c3.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`

### 215. cpython-313-bdc371ce3bd8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f35fe972`
- Honggfuzz stack hash: `19f35fe972`
- PC: `0x5aed6be08e94`
- Fault address: `0x30`
- Instruction: `mov____0x30(%rax),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-bdc371ce3bd8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aed6be08e94.STACK.19f35fe972.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aed6be08e94.STACK.19f35fe972.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5aed6be08e94.STACK.19f35fe972.CODE.1.ADDR.30.INSTR.mov____0x30(%rax),%r13.pyc`

### 216. cpython-313-bdcb9d01fecb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193686058b`
- Honggfuzz stack hash: `193686058b`
- PC: `0x5f49dfff2358`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-bdcb9d01fecb.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f49dfff2358.STACK.193686058b.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f49dfff2358.STACK.193686058b.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5f49dfff2358.STACK.193686058b.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`

### 217. cpython-313-c13c7159787d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e25be5f20`
- Honggfuzz stack hash: `e25be5f20`
- PC: `0x637562b1d956`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c13c7159787d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.637562b1d956.STACK.e25be5f20.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.637562b1d956.STACK.e25be5f20.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.637562b1d956.STACK.e25be5f20.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`

### 218. cpython-313-c22fd92c7386

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d3a97c074`
- Honggfuzz stack hash: `d3a97c074`
- PC: `0x63022278848c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c22fd92c7386.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63022278848c.STACK.d3a97c074.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63022278848c.STACK.d3a97c074.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.63022278848c.STACK.d3a97c074.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 219. cpython-313-c6824574b733

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a6a9dc6b7`
- Honggfuzz stack hash: `1a6a9dc6b7`
- PC: `0x55ab1fa5b360`
- Fault address: `0x12`
- Instruction: `mov____0x8(%r14),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c6824574b733.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ab1fa5b360.STACK.1a6a9dc6b7.CODE.1.ADDR.12.INSTR.mov____0x8(%r14),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ab1fa5b360.STACK.1a6a9dc6b7.CODE.1.ADDR.12.INSTR.mov____0x8(%r14),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.55ab1fa5b360.STACK.1a6a9dc6b7.CODE.1.ADDR.12.INSTR.mov____0x8(%r14),%r12.pyc`

### 220. cpython-313-c742ca9a3456

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a3d71e12d`
- Honggfuzz stack hash: `1a3d71e12d`
- PC: `0x64ab919bd48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-c742ca9a3456.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64ab919bd48c.STACK.1a3d71e12d.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64ab919bd48c.STACK.1a3d71e12d.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.64ab919bd48c.STACK.1a3d71e12d.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 221. cpython-313-cafe6ae93fa3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1af09af43d`
- Honggfuzz stack hash: `1af09af43d`
- PC: `0x606063604d82`
- Fault address: `0x0`
- Instruction: `movaps_%xmm0,-0x50(%rbp)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-cafe6ae93fa3.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.606063604d82.STACK.1af09af43d.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.606063604d82.STACK.1af09af43d.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.606063604d82.STACK.1af09af43d.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x50(%rbp).pyc`

### 222. cpython-313-cf78275abec0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:efd6ccbae`
- Honggfuzz stack hash: `efd6ccbae`
- PC: `0x5c44e542b837`
- Fault address: `0x0`
- Instruction: `call___*%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-cf78275abec0.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c44e542b837.STACK.efd6ccbae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c44e542b837.STACK.efd6ccbae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c44e542b837.STACK.efd6ccbae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`

### 223. cpython-313-d20f553d753b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f846191ff`
- Honggfuzz stack hash: `f846191ff`
- PC: `0x5d0caee4ac43`
- Fault address: `0xc8`
- Instruction: `mov____0xc8(%rax),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d20f553d753b.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d0caee4ac43.STACK.f846191ff.CODE.1.ADDR.c8.INSTR.mov____0xc8(%rax),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d0caee4ac43.STACK.f846191ff.CODE.1.ADDR.c8.INSTR.mov____0xc8(%rax),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5d0caee4ac43.STACK.f846191ff.CODE.1.ADDR.c8.INSTR.mov____0xc8(%rax),%rbx.pyc`

### 224. cpython-313-d44d31fd8e01

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b6bc06d5b`
- Honggfuzz stack hash: `1b6bc06d5b`
- PC: `0x5fa6ad9dc84e`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d44d31fd8e01.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ad9dc84e.STACK.1b6bc06d5b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ad9dc84e.STACK.1b6bc06d5b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa6ad9dc84e.STACK.1b6bc06d5b.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r15.pyc`

### 225. cpython-313-d7d5dae9430a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e7283b042`
- Honggfuzz stack hash: `e7283b042`
- PC: `0x5cd9a8e0867d`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d7d5dae9430a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cd9a8e0867d.STACK.e7283b042.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cd9a8e0867d.STACK.e7283b042.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5cd9a8e0867d.STACK.e7283b042.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`

### 226. cpython-313-d8cdf2d84bea

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1837a9f40d`
- Honggfuzz stack hash: `1837a9f40d`
- PC: `0x6244a5bc398f`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d8cdf2d84bea.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6244a5bc398f.STACK.1837a9f40d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6244a5bc398f.STACK.1837a9f40d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6244a5bc398f.STACK.1837a9f40d.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r15.pyc`

### 227. cpython-313-d8f04a0eb6a9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cb1941bfa`
- Honggfuzz stack hash: `cb1941bfa`
- PC: `0x5c6677e5c48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-d8f04a0eb6a9.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c6677e5c48c.STACK.cb1941bfa.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c6677e5c48c.STACK.cb1941bfa.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5c6677e5c48c.STACK.cb1941bfa.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 228. cpython-313-db1a9a6dd542

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:188f5e91cc`
- Honggfuzz stack hash: `188f5e91cc`
- PC: `0x7ee2550b4449`
- Fault address: `0x5f930c000000`
- Instruction: `mov____(%rax),%rdi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-db1a9a6dd542.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7ee2550b4449.STACK.188f5e91cc.CODE.1.ADDR.5f930c000000.INSTR.mov____(%rax),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7ee2550b4449.STACK.188f5e91cc.CODE.1.ADDR.5f930c000000.INSTR.mov____(%rax),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.7ee2550b4449.STACK.188f5e91cc.CODE.1.ADDR.5f930c000000.INSTR.mov____(%rax),%rdi.pyc`

### 229. cpython-313-dba8946399ae

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18560d7060`
- Honggfuzz stack hash: `18560d7060`
- PC: `0x649af8a91dc4`
- Fault address: `0x0`
- Instruction: `mov____0x0(%r13),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-dba8946399ae.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.649af8a91dc4.STACK.18560d7060.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.649af8a91dc4.STACK.18560d7060.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.649af8a91dc4.STACK.18560d7060.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`

### 230. cpython-313-dc8f177debc5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19747bc269`
- Honggfuzz stack hash: `19747bc269`
- PC: `0x61a4a4726e96`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-dc8f177debc5.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61a4a4726e96.STACK.19747bc269.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61a4a4726e96.STACK.19747bc269.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.61a4a4726e96.STACK.19747bc269.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%r14.pyc`

### 231. cpython-313-e2599cb48269

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18ac11003a`
- Honggfuzz stack hash: `18ac11003a`
- PC: `0x60beb873c48c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e2599cb48269.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60beb873c48c.STACK.18ac11003a.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60beb873c48c.STACK.18ac11003a.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.60beb873c48c.STACK.18ac11003a.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 232. cpython-313-e85dd244c180

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d37b6dbc2`
- Honggfuzz stack hash: `d37b6dbc2`
- PC: `0x6341d884248c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e85dd244c180.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6341d884248c.STACK.d37b6dbc2.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6341d884248c.STACK.d37b6dbc2.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6341d884248c.STACK.d37b6dbc2.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 233. cpython-313-e89fa661692d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:eba65bb64`
- Honggfuzz stack hash: `eba65bb64`
- PC: `0x5ae6d365648c`
- Fault address: `0x18`
- Instruction: `mov____0x18(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e89fa661692d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6d365648c.STACK.eba65bb64.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6d365648c.STACK.eba65bb64.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5ae6d365648c.STACK.eba65bb64.CODE.1.ADDR.18.INSTR.mov____0x18(%r14),%r15.pyc`

### 234. cpython-313-e9d90a7ab49d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d3f4454db`
- Honggfuzz stack hash: `d3f4454db`
- PC: `0x5fa4e20d0906`
- Fault address: `0x3`
- Instruction: `mov____(%rbx),%r15d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-e9d90a7ab49d.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa4e20d0906.STACK.d3f4454db.CODE.1.ADDR.3.INSTR.mov____(%rbx),%r15d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa4e20d0906.STACK.d3f4454db.CODE.1.ADDR.3.INSTR.mov____(%rbx),%r15d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fa4e20d0906.STACK.d3f4454db.CODE.1.ADDR.3.INSTR.mov____(%rbx),%r15d.pyc`

### 235. cpython-313-eb1719996647

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c7c927513`
- Honggfuzz stack hash: `c7c927513`
- PC: `0x5b6f20731634`
- Fault address: `0x9`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-eb1719996647.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b6f20731634.STACK.c7c927513.CODE.1.ADDR.9.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b6f20731634.STACK.c7c927513.CODE.1.ADDR.9.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5b6f20731634.STACK.c7c927513.CODE.1.ADDR.9.INSTR.mov____0x8(%r13),%rax.pyc`

### 236. cpython-313-ebb568efaaf7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3ea7eb90`
- Honggfuzz stack hash: `c3ea7eb90`
- PC: `0x6471362a3920`
- Fault address: `0x0`
- Instruction: `mov____0x158(%rbx),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ebb568efaaf7.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6471362a3920.STACK.c3ea7eb90.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6471362a3920.STACK.c3ea7eb90.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6471362a3920.STACK.c3ea7eb90.CODE.128.ADDR.0.INSTR.mov____0x158(%rbx),%r13.pyc`

### 237. cpython-313-ed39e1e545c6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b81756e54`
- Honggfuzz stack hash: `1b81756e54`
- PC: `0x578bd1cf068b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-ed39e1e545c6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578bd1cf068b.STACK.1b81756e54.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578bd1cf068b.STACK.1b81756e54.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.578bd1cf068b.STACK.1b81756e54.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`

### 238. cpython-313-f1b311911602

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a2860b3c8`
- Honggfuzz stack hash: `1a2860b3c8`
- PC: `0x5fdc1bcb584e`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f1b311911602.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdc1bcb584e.STACK.1a2860b3c8.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdc1bcb584e.STACK.1a2860b3c8.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5fdc1bcb584e.STACK.1a2860b3c8.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r15.pyc`

### 239. cpython-313-f57e68d7f7b6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:182cf10fde`
- Honggfuzz stack hash: `182cf10fde`
- PC: `0x6518e7dd46a4`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f57e68d7f7b6.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6518e7dd46a4.STACK.182cf10fde.CODE.1.ADDR.0.INSTR.mov____(%r15),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6518e7dd46a4.STACK.182cf10fde.CODE.1.ADDR.0.INSTR.mov____(%r15),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.6518e7dd46a4.STACK.182cf10fde.CODE.1.ADDR.0.INSTR.mov____(%r15),%r14.pyc`

### 240. cpython-313-f6cd2a182872

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c3f2e03b4`
- Honggfuzz stack hash: `c3f2e03b4`
- PC: `0x625c046598ea`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f6cd2a182872.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.625c046598ea.STACK.c3f2e03b4.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.625c046598ea.STACK.c3f2e03b4.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.625c046598ea.STACK.c3f2e03b4.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`

### 241. cpython-313-f6d7188e4462

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19bb054a13`
- Honggfuzz stack hash: `19bb054a13`
- PC: `0x573165c227ef`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f6d7188e4462.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.573165c227ef.STACK.19bb054a13.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.573165c227ef.STACK.19bb054a13.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.573165c227ef.STACK.19bb054a13.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 242. cpython-313-f73de278197a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf2794942`
- Honggfuzz stack hash: `cf2794942`
- PC: `0x584ebac0ca7a`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f73de278197a.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.584ebac0ca7a.STACK.cf2794942.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.584ebac0ca7a.STACK.cf2794942.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.584ebac0ca7a.STACK.cf2794942.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`

### 243. cpython-313-f77362b7d6b8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d79a59c1c`
- Honggfuzz stack hash: `d79a59c1c`
- PC: `0x58cea5fa9956`
- Fault address: `0x100000007`
- Instruction: `mov____0x8(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-f77362b7d6b8.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58cea5fa9956.STACK.d79a59c1c.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58cea5fa9956.STACK.d79a59c1c.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.58cea5fa9956.STACK.d79a59c1c.CODE.1.ADDR.100000007.INSTR.mov____0x8(%rbx),%r14.pyc`

### 244. cpython-313-fa3aa0ecb10f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18c7a47459`
- Honggfuzz stack hash: `18c7a47459`
- PC: `0x5766735d2687`
- Fault address: `0x90`
- Instruction: `mov____0x90(%r12),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.13/unique_bug_pyc/cpython-313-fa3aa0ecb10f.pyc`
- Representative original: `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5766735d2687.STACK.18c7a47459.CODE.1.ADDR.90.INSTR.mov____0x90(%r12),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.13/source/cpython-* PYTHONPATH=data/rq3/cpython-3.13/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.13/instrumented/python data/rq3/harness.py data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5766735d2687.STACK.18c7a47459.CODE.1.ADDR.90.INSTR.mov____0x90(%r12),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `Traceback (most recent call last):`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/site.py", line 73, in <module>`
  - `import os`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.13/source/cpython-3.13.13/Lib/os.py", line 1173, in <module>`
  - `if _exists('sched_getaffinity') and sys._get_cpu_count_config() < 0:`
  - `AttributeError: module 'sys' has no attribute '_get_cpu_count_config'`
- Example finding inputs:
  - `data/rq3/cpython-3.13/fuzz/crashes/SIGSEGV.PC.5766735d2687.STACK.18c7a47459.CODE.1.ADDR.90.INSTR.mov____0x90(%r12),%rbx.pyc`
