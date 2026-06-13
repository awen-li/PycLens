# RQ3 Unique Bug Report: cpython-3.14

## Summary

- Crash findings: 2088
- Unique bugs: 182
- Representative pyc artifacts: 182

## Unique Bugs

### 1. cpython-314-cb9b8bf7bf2b

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19f4e08fda`
- Honggfuzz stack hash: `19f4e08fda`
- PC: `0x7010a38439fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 616
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cb9b8bf7bf2b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7010a38439fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7010a38439fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a0525b9f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7010a38439fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7017380759fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.701aabe8e9fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.701c1ad6e9fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.702dc33f49fc.STACK.19f4e08fda.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 611 more

### 2. cpython-314-70ab44cae8f7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1830ed1c67`
- Honggfuzz stack hash: `1830ed1c67`
- PC: `0x1e70`
- Fault address: `0x1e70`
- Instruction: `[NOT_MMAPED]`
- Findings: 415
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-70ab44cae8f7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1e70.STACK.1830ed1c67.CODE.1.ADDR.1e70.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1e70.STACK.1830ed1c67.CODE.1.ADDR.1e70.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078e13d4c4180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1e70.STACK.1830ed1c67.CODE.1.ADDR.1e70.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5587461ec439.STACK.1830ed1c67.CODE.1.ADDR.8.INSTR.mov____0x8(%rdi),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558842677fad.STACK.1830ed1c67.CODE.1.ADDR.0.INSTR.mov____(%rbx),%r12d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5589aa96b790.STACK.1830ed1c67.CODE.1.ADDR.10234.INSTR.addl___$0x1,(%rbx).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5592e61d9637.STACK.1830ed1c67.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - ... 410 more

### 3. cpython-314-5a36b8a8d44c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cb2d75777`
- Honggfuzz stack hash: `cb2d75777`
- PC: `0x55ad07257d8c`
- Fault address: `0x38`
- Instruction: `mov____0x8(%r14,%rbx,8),%r14`
- Findings: 173
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5a36b8a8d44c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ad07257d8c.STACK.cb2d75777.CODE.1.ADDR.38.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ad07257d8c.STACK.cb2d75777.CODE.1.ADDR.38.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bab8ad2c180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ad07257d8c.STACK.cb2d75777.CODE.1.ADDR.38.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55bc8953dd8c.STACK.cb2d75777.CODE.1.ADDR.18.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c60cc83d8c.STACK.cb2d75777.CODE.1.ADDR.28.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ca4ffd2dc4.STACK.cb2d75777.CODE.1.ADDR.60.INSTR.mov____0x60(%rax),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ed9c470d8c.STACK.cb2d75777.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - ... 168 more

### 4. cpython-314-a0900c285088

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183c056d12`
- Honggfuzz stack hash: `183c056d12`
- PC: `0x55b3a3556fca`
- Fault address: `0x55b300000000`
- Instruction: `mov____(%rbx),%r13d`
- Findings: 112
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a0900c285088.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b3a3556fca.STACK.183c056d12.CODE.1.ADDR.55b300000000.INSTR.mov____(%rbx),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b3a3556fca.STACK.183c056d12.CODE.1.ADDR.55b300000000.INSTR.mov____(%rbx),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000076c9640a0180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b3a3556fca.STACK.183c056d12.CODE.1.ADDR.55b300000000.INSTR.mov____(%rbx),%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55bc60b9234a.STACK.183c056d12.CODE.1.ADDR.1d8.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5621823af0ed.STACK.183c056d12.CODE.1.ADDR.562100000000.INSTR.mov____(%rbx),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d3d616cf8b.STACK.183c056d12.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e64b08cc4a.STACK.183c056d12.CODE.1.ADDR.56e600000008.INSTR.mov____0x8(%rax),%rcx.pyc`
  - ... 107 more

### 5. cpython-314-1dafb3e699b2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fca120653`
- Honggfuzz stack hash: `fca120653`
- PC: `0x562607519d8c`
- Fault address: `0x800`
- Instruction: `mov____0x8(%r14,%rbx,8),%r14`
- Findings: 43
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-1dafb3e699b2.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562607519d8c.STACK.fca120653.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562607519d8c.STACK.fca120653.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000778e46a42180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562607519d8c.STACK.fca120653.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56db7539dd8c.STACK.fca120653.CODE.1.ADDR.8.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e248850d8c.STACK.fca120653.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573877e8cd8c.STACK.fca120653.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.579d3406bd8c.STACK.fca120653.CODE.1.ADDR.8.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - ... 38 more

### 6. cpython-314-d6b7808901a3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d675198e3`
- Honggfuzz stack hash: `d675198e3`
- PC: `0x56527340f750`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%r12`
- Findings: 39
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d6b7808901a3.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56527340f750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56527340f750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ce189444180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56527340f750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57433e22d7c3.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5748e5915750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57554eaed750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.575592815750.STACK.d675198e3.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - ... 34 more

### 7. cpython-314-021348427247

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a94a7b8f`
- Honggfuzz stack hash: `18a94a7b8f`
- PC: `0x5597ce1b92e9`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%rdi`
- Findings: 34
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-021348427247.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5597ce1b92e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5597ce1b92e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000793c761e2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5597ce1b92e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55aead2402e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55fe96f2e2e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ff744012e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56760bfa22e9.STACK.18a94a7b8f.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%rdi.pyc`
  - ... 29 more

### 8. cpython-314-2c626ff5f2f7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19ea13f994`
- Honggfuzz stack hash: `19ea13f994`
- PC: `0x5881fb20271c`
- Fault address: `0x88`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 31
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2c626ff5f2f7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5881fb20271c.STACK.19ea13f994.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5881fb20271c.STACK.19ea13f994.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a0e94004180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5881fb20271c.STACK.19ea13f994.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5896a559d71c.STACK.19ea13f994.CODE.1.ADDR.c8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.591d398c171c.STACK.19ea13f994.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.592a6bdca71c.STACK.19ea13f994.CODE.1.ADDR.100000007.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59488290871c.STACK.19ea13f994.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
  - ... 26 more

### 9. cpython-314-62b65abc800f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:da0955783`
- Honggfuzz stack hash: `da0955783`
- PC: `0x556f74949540`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 26
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-62b65abc800f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556f74949540.STACK.da0955783.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556f74949540.STACK.da0955783.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000072db593c7180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556f74949540.STACK.da0955783.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.559b569ae540.STACK.da0955783.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.577430bac544.STACK.da0955783.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58101c2c9544.STACK.da0955783.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5837a93f0544.STACK.da0955783.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rbx.pyc`
  - ... 21 more

### 10. cpython-314-e254c107830c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cbc1a57ef`
- Honggfuzz stack hash: `cbc1a57ef`
- PC: `0x56a28271e6bd`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 24
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e254c107830c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a28271e6bd.STACK.cbc1a57ef.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a28271e6bd.STACK.cbc1a57ef.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000712193210180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a28271e6bd.STACK.cbc1a57ef.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5749008336bd.STACK.cbc1a57ef.CODE.1.ADDR.41.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57b5cf1e36f4.STACK.cbc1a57ef.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57ded84a66bd.STACK.cbc1a57ef.CODE.1.ADDR.51.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a13793396bd.STACK.cbc1a57ef.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - ... 19 more

### 11. cpython-314-0a1f9a74a35c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19e360113b`
- Honggfuzz stack hash: `19e360113b`
- PC: `0x55d3f3cd645f`
- Fault address: `0xa`
- Instruction: `mov____(%r12),%ebx`
- Findings: 22
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0a1f9a74a35c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55d3f3cd645f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55d3f3cd645f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007377e2965180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55d3f3cd645f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5797c937745f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.580c638c83f9.STACK.19e360113b.CODE.1.ADDR.41.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59969063245f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59b555f7945f.STACK.19e360113b.CODE.1.ADDR.a.INSTR.mov____(%r12),%ebx.pyc`
  - ... 17 more

### 12. cpython-314-9cc783dcf87e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de2e60a79`
- Honggfuzz stack hash: `de2e60a79`
- PC: `0x556c17475a6a`
- Fault address: `0xc9`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 22
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9cc783dcf87e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556c17475a6a.STACK.de2e60a79.CODE.1.ADDR.c9.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556c17475a6a.STACK.de2e60a79.CODE.1.ADDR.c9.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000070c637413180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.556c17475a6a.STACK.de2e60a79.CODE.1.ADDR.c9.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d5b784ba6a.STACK.de2e60a79.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58c196694a6a.STACK.de2e60a79.CODE.1.ADDR.58c1c1af7.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.594410aaaa6a.STACK.de2e60a79.CODE.1.ADDR.12.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59d74f0c0a6a.STACK.de2e60a79.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`
  - ... 17 more

### 13. cpython-314-bf3ca2c6657d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c762a59c0`
- Honggfuzz stack hash: `c762a59c0`
- PC: `0x56153eb812e9`
- Fault address: `0x561500000008`
- Instruction: `mov____0x8(%r14),%rdi`
- Findings: 18
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-bf3ca2c6657d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56153eb812e9.STACK.c762a59c0.CODE.1.ADDR.561500000008.INSTR.mov____0x8(%r14),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56153eb812e9.STACK.c762a59c0.CODE.1.ADDR.561500000008.INSTR.mov____0x8(%r14),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007797020e4180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56153eb812e9.STACK.c762a59c0.CODE.1.ADDR.561500000008.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566b1e8de2e9.STACK.c762a59c0.CODE.1.ADDR.566b00000008.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a12341bd2e9.STACK.c762a59c0.CODE.1.ADDR.5a1200000008.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a371016c2e9.STACK.c762a59c0.CODE.1.ADDR.5a3700000008.INSTR.mov____0x8(%r14),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aa73f9c82e9.STACK.c762a59c0.CODE.1.ADDR.5aa700000008.INSTR.mov____0x8(%r14),%rdi.pyc`
  - ... 13 more

### 14. cpython-314-1a04034a2c9c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d67c036e6`
- Honggfuzz stack hash: `d67c036e6`
- PC: `0x1`
- Fault address: `0x1`
- Instruction: `[NOT_MMAPED]`
- Findings: 17
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-1a04034a2c9c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.d67c036e6.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.d67c036e6.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d0aef1cf180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.d67c036e6.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55723e0d3081.STACK.d67c036e6.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59dc5bb72081.STACK.d67c036e6.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c4997f53085.STACK.d67c036e6.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c9ae0525085.STACK.d67c036e6.CODE.1.ADDR.39.INSTR.mov____0x8(%r13),%r12.pyc`
  - ... 12 more

### 15. cpython-314-c18ecb5602a5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c761b814b`
- Honggfuzz stack hash: `c761b814b`
- PC: `0x55a3c4dbdbaf`
- Fault address: `0x55a400000008`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 17
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c18ecb5602a5.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a3c4dbdbaf.STACK.c761b814b.CODE.1.ADDR.55a400000008.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a3c4dbdbaf.STACK.c761b814b.CODE.1.ADDR.55a400000008.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077bb3779a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a3c4dbdbaf.STACK.c761b814b.CODE.1.ADDR.55a400000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.563aba652bb3.STACK.c761b814b.CODE.1.ADDR.a9.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b14ff07baf.STACK.c761b814b.CODE.1.ADDR.56b100000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d0e49fabaf.STACK.c761b814b.CODE.1.ADDR.56d100000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e2e5aa6baf.STACK.c761b814b.CODE.1.ADDR.56e300000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - ... 12 more

### 16. cpython-314-a56336a9e61a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b7e88bde9`
- Honggfuzz stack hash: `1b7e88bde9`
- PC: `0x55798a115a83`
- Fault address: `0x557900000008`
- Instruction: `mov____0x8(%r13),%rsi`
- Findings: 16
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a56336a9e61a.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55798a115a83.STACK.1b7e88bde9.CODE.1.ADDR.557900000008.INSTR.mov____0x8(%r13),%rsi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55798a115a83.STACK.1b7e88bde9.CODE.1.ADDR.557900000008.INSTR.mov____0x8(%r13),%rsi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071a766e45180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55798a115a83.STACK.1b7e88bde9.CODE.1.ADDR.557900000008.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cb018cea83.STACK.1b7e88bde9.CODE.1.ADDR.57cb00000008.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cf0dcb8a83.STACK.1b7e88bde9.CODE.1.ADDR.57cf00000008.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.594404794a83.STACK.1b7e88bde9.CODE.1.ADDR.594400000008.INSTR.mov____0x8(%r13),%rsi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a2887bada83.STACK.1b7e88bde9.CODE.1.ADDR.5a2800000008.INSTR.mov____0x8(%r13),%rsi.pyc`
  - ... 11 more

### 17. cpython-314-2583e654d40c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c76eee4db`
- Honggfuzz stack hash: `c76eee4db`
- PC: `0x1`
- Fault address: `0x1`
- Instruction: `[NOT_MMAPED]`
- Findings: 13
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2583e654d40c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.c76eee4db.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.c76eee4db.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007f07f827e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.1.STACK.c76eee4db.CODE.1.ADDR.1.INSTR.[NOT_MMAPED].pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55896abfdc4f.STACK.c76eee4db.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5611d91d23d0.STACK.c76eee4db.CODE.2.ADDR.5611d91d23d0.INSTR.add____(%rax),%eax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5663a0d10af0.STACK.c76eee4db.CODE.2.ADDR.5663a0d10af0.INSTR.add____(%rax),%eax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59c249b927b0.STACK.c76eee4db.CODE.2.ADDR.59c249b927b0.INSTR.add____(%rax),%eax.pyc`
  - ... 8 more

### 18. cpython-314-bcb1e238816f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18c96151a0`
- Honggfuzz stack hash: `18c96151a0`
- PC: `0x57f82eeaa6f4`
- Fault address: `0x57f800000000`
- Instruction: `mov____(%r14),%ebx`
- Findings: 12
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-bcb1e238816f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f82eeaa6f4.STACK.18c96151a0.CODE.1.ADDR.57f800000000.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f82eeaa6f4.STACK.18c96151a0.CODE.1.ADDR.57f800000000.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000079c1c7397180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f82eeaa6f4.STACK.18c96151a0.CODE.1.ADDR.57f800000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5890e73846bd.STACK.18c96151a0.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bfb356fc6f4.STACK.18c96151a0.CODE.1.ADDR.5bfb00000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f899a64e6bd.STACK.18c96151a0.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62d08c5646f4.STACK.18c96151a0.CODE.1.ADDR.62d000000000.INSTR.mov____(%r14),%ebx.pyc`
  - ... 7 more

### 19. cpython-314-facd5f93618d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19a250c8e3`
- Honggfuzz stack hash: `19a250c8e3`
- PC: `0x558705c695bd`
- Fault address: `0x558700000000`
- Instruction: `mov____0x0(%r13),%ebx`
- Findings: 12
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-facd5f93618d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558705c695bd.STACK.19a250c8e3.CODE.1.ADDR.558700000000.INSTR.mov____0x0(%r13),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558705c695bd.STACK.19a250c8e3.CODE.1.ADDR.558700000000.INSTR.mov____0x0(%r13),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007cf06053d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558705c695bd.STACK.19a250c8e3.CODE.1.ADDR.558700000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b3723175bd.STACK.19a250c8e3.CODE.1.ADDR.55b300000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b4c865a5bd.STACK.19a250c8e3.CODE.1.ADDR.56b500000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57fd2e8cd5bd.STACK.19a250c8e3.CODE.1.ADDR.57fd00000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59e6f169a5bd.STACK.19a250c8e3.CODE.1.ADDR.59e700000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - ... 7 more

### 20. cpython-314-9d5d04ad998c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:182bc7a9bc`
- Honggfuzz stack hash: `182bc7a9bc`
- PC: `0x564981ca878a`
- Fault address: `0x0`
- Instruction: `mov____0x0(%r13),%r15d`
- Findings: 11
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9d5d04ad998c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564981ca878a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564981ca878a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007912b8e92180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564981ca878a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.571c424dc78a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f7692cf78a.STACK.182bc7a9bc.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.582e1427978a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5851669ee78a.STACK.182bc7a9bc.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - ... 6 more

### 21. cpython-314-411591a68f8e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de2ba6543`
- Honggfuzz stack hash: `de2ba6543`
- PC: `0x5694f8504587`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r12),%rdi`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-411591a68f8e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5694f8504587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5694f8504587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071ddbc5c7180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5694f8504587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57b3d0a72587.STACK.de2ba6543.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.587d57a2a587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b06341b9587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bb76cc31587.STACK.de2ba6543.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
  - ... 4 more

### 22. cpython-314-4556ae3870db

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fe10b3679`
- Honggfuzz stack hash: `fe10b3679`
- PC: `0x55a25b7b27b8`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-4556ae3870db.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a25b7b27b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a25b7b27b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d28a26df180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55a25b7b27b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5817cef027b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59adc37c47b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f49a5cae7b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60b0d92787b8.STACK.fe10b3679.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r15.pyc`
  - ... 4 more

### 23. cpython-314-5879d6216fe3

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19f4bce37f`
- Honggfuzz stack hash: `19f4bce37f`
- PC: `0x70cf2d9a49fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5879d6216fe3.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.70cf2d9a49fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.70cf2d9a49fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000076a932e23180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.70cf2d9a49fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.716070ad69fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.72f0ec6dd9fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7501da0dc9fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.760479eba9fc.STACK.19f4bce37f.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - ... 4 more

### 24. cpython-314-784d617d7c6c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19adef5eec`
- Honggfuzz stack hash: `19adef5eec`
- PC: `0x55b070b1da33`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-784d617d7c6c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b070b1da33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b070b1da33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007cbc6ce94180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55b070b1da33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55fffe8bba33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5813d6e74a33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58334ef9da33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58cabbb83a33.STACK.19adef5eec.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
  - ... 4 more

### 25. cpython-314-8fe411e495f5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:187120222c`
- Honggfuzz stack hash: `187120222c`
- PC: `0x5620a000896e`
- Fault address: `0x0`
- Instruction: `mov____0x78(%r15),%rbx`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8fe411e495f5.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5620a000896e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5620a000896e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b61b4d09180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5620a000896e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c6cbaabf96e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cb9ce15596e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d0b9525596e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e9d73ac996e.STACK.187120222c.CODE.128.ADDR.0.INSTR.mov____0x78(%r15),%rbx.pyc`
  - ... 4 more

### 26. cpython-314-9061ecffcd4e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1837cfd628`
- Honggfuzz stack hash: `1837cfd628`
- PC: `0x555c45cf5d8c`
- Fault address: `0x800`
- Instruction: `mov____0x8(%r14,%rbx,8),%r14`
- Findings: 9
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9061ecffcd4e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.555c45cf5d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.555c45cf5d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000072969cadf180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.555c45cf5d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55dc45938d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57c4d81b8d8c.STACK.1837cfd628.CODE.1.ADDR.8.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5af151808d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bdcab1d5d8c.STACK.1837cfd628.CODE.1.ADDR.800.INSTR.mov____0x8(%r14,%rbx,8),%r14.pyc`
  - ... 4 more

### 27. cpython-314-58bcd361e7e4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d26ccf048`
- Honggfuzz stack hash: `d26ccf048`
- PC: `0x560911d40938`
- Fault address: `0x0`
- Instruction: `mov____0x20(%rbx),%r12`
- Findings: 8
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-58bcd361e7e4.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560911d40938.STACK.d26ccf048.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560911d40938.STACK.d26ccf048.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074afdca63180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560911d40938.STACK.d26ccf048.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.563c602f6938.STACK.d26ccf048.CODE.1.ADDR.20.INSTR.mov____0x20(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.572412ae8938.STACK.d26ccf048.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aa4cbb97938.STACK.d26ccf048.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6178e235c938.STACK.d26ccf048.CODE.1.ADDR.20.INSTR.mov____0x20(%rbx),%r12.pyc`
  - ... 3 more

### 28. cpython-314-056f172652e8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197385c037`
- Honggfuzz stack hash: `197385c037`
- PC: `0x59ad872c236f`
- Fault address: `0x1ff0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-056f172652e8.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59ad872c236f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59ad872c236f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a07ed90e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59ad872c236f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dad1979436f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f7305def36f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f9787dd436f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61a954d8236f.STACK.197385c037.CODE.1.ADDR.1ff0.INSTR.mov____(%r14),%ebx.pyc`
  - ... 2 more

### 29. cpython-314-3968fb7a582b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a98ec694`
- Honggfuzz stack hash: `18a98ec694`
- PC: `0x5a1a502dcd85`
- Fault address: `0x5a1a00000008`
- Instruction: `cmpq___$0x0,0x8(%rax)`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-3968fb7a582b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a1a502dcd85.STACK.18a98ec694.CODE.1.ADDR.5a1a00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a1a502dcd85.STACK.18a98ec694.CODE.1.ADDR.5a1a00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b5dcbadd180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a1a502dcd85.STACK.18a98ec694.CODE.1.ADDR.5a1a00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0d66732d85.STACK.18a98ec694.CODE.1.ADDR.5f0d00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.602a2b577d85.STACK.18a98ec694.CODE.1.ADDR.602a00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6265b998fd85.STACK.18a98ec694.CODE.1.ADDR.626500000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.639cdab7ad85.STACK.18a98ec694.CODE.1.ADDR.639d00000008.INSTR.cmpq___$0x0,0x8(%rax).pyc`
  - ... 2 more

### 30. cpython-314-88afacdaf933

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c2262c35b`
- Honggfuzz stack hash: `c2262c35b`
- PC: `0x5ac8cc42a77d`
- Fault address: `0xa7`
- Instruction: `mov____0xa8(%rax),%rsi`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-88afacdaf933.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ac8cc42a77d.STACK.c2262c35b.CODE.1.ADDR.a7.INSTR.mov____0xa8(%rax),%rsi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ac8cc42a77d.STACK.c2262c35b.CODE.1.ADDR.a7.INSTR.mov____0xa8(%rax),%rsi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a282a2c9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ac8cc42a77d.STACK.c2262c35b.CODE.1.ADDR.a7.INSTR.mov____0xa8(%rax),%rsi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b249ba20717.STACK.c2262c35b.CODE.1.ADDR.0.INSTR.mov____(%r12),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b7580d9e717.STACK.c2262c35b.CODE.128.ADDR.0.INSTR.mov____(%r12),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f33e1a20778.STACK.c2262c35b.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f9a6b44e717.STACK.c2262c35b.CODE.128.ADDR.0.INSTR.mov____(%r12),%r14d.pyc`
  - ... 2 more

### 31. cpython-314-c5e9d30936f7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193dda470c`
- Honggfuzz stack hash: `193dda470c`
- PC: `0x5594dda62587`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r12),%rdi`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c5e9d30936f7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5594dda62587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5594dda62587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000787c21f13180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5594dda62587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57a432a2b587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.585c4fd73587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.597f4082d587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e106d180587.STACK.193dda470c.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rdi.pyc`
  - ... 2 more

### 32. cpython-314-d1985aa7dd2c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f451c7987`
- Honggfuzz stack hash: `f451c7987`
- PC: `0x566d0ac134df`
- Fault address: `0x99`
- Instruction: `cmpq___$0x0,0x58(%rbx)`
- Findings: 7
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d1985aa7dd2c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566d0ac134df.STACK.f451c7987.CODE.1.ADDR.99.INSTR.cmpq___$0x0,0x58(%rbx).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566d0ac134df.STACK.f451c7987.CODE.1.ADDR.99.INSTR.cmpq___$0x0,0x58(%rbx).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007792bd7a6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566d0ac134df.STACK.f451c7987.CODE.1.ADDR.99.INSTR.cmpq___$0x0,0x58(%rbx).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.590e21afd4da.STACK.f451c7987.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ce896a9c4da.STACK.f451c7987.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5daee6c0e4da.STACK.f451c7987.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e01ce46c4df.STACK.f451c7987.CODE.1.ADDR.5e01cec0ce.INSTR.cmpq___$0x0,0x58(%rbx).pyc`
  - ... 2 more

### 33. cpython-314-2a53f02d65fc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b6132c6d`
- Honggfuzz stack hash: `19b6132c6d`
- PC: `0x566e0a4323f9`
- Fault address: `0x0`
- Instruction: `mov____0x0(%r13),%ebx`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2a53f02d65fc.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566e0a4323f9.STACK.19b6132c6d.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566e0a4323f9.STACK.19b6132c6d.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007518fb1ee180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.566e0a4323f9.STACK.19b6132c6d.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.570f03db33f9.STACK.19b6132c6d.CODE.1.ADDR.291.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ae30dbf13f9.STACK.19b6132c6d.CODE.1.ADDR.2d200000000.INSTR.mov____0x0(%r13),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6306cda9345f.STACK.19b6132c6d.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63b57659d3f9.STACK.19b6132c6d.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%ebx.pyc`
  - ... 1 more

### 34. cpython-314-402123add590

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ce334132d`
- Honggfuzz stack hash: `ce334132d`
- PC: `0x5974e01eec4b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-402123add590.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5974e01eec4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5974e01eec4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071215f66b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5974e01eec4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a2f89899c4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf23c1cbc4b.STACK.ce334132d.CODE.1.ADDR.5bf200000008.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ca1c5216c4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.64d06821ec4b.STACK.ce334132d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - ... 1 more

### 35. cpython-314-813ed77c3a65

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d2c586105`
- Honggfuzz stack hash: `d2c586105`
- PC: `0x572cd361f230`
- Fault address: `0x0`
- Instruction: `mov____(%r12),%r15d`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-813ed77c3a65.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.572cd361f230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.572cd361f230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000721630fff180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.572cd361f230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a2711b4a230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c04754d4230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5eb208019230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0dd6f04230.STACK.d2c586105.CODE.128.ADDR.0.INSTR.mov____(%r12),%r15d.pyc`
  - ... 1 more

### 36. cpython-314-845a4be39973

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db31e0e1b`
- Honggfuzz stack hash: `db31e0e1b`
- PC: `0x6056a1bf4750`
- Fault address: `0x605600000008`
- Instruction: `mov____0x8(%r15),%r12`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-845a4be39973.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6056a1bf4750.STACK.db31e0e1b.CODE.1.ADDR.605600000008.INSTR.mov____0x8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6056a1bf4750.STACK.db31e0e1b.CODE.1.ADDR.605600000008.INSTR.mov____0x8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000075229f7d8180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6056a1bf4750.STACK.db31e0e1b.CODE.1.ADDR.605600000008.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.622f8aa75750.STACK.db31e0e1b.CODE.1.ADDR.622f00000008.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.633d28f1f750.STACK.db31e0e1b.CODE.1.ADDR.633d00000008.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6372da0c2750.STACK.db31e0e1b.CODE.1.ADDR.637300000008.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.64fe36f2d750.STACK.db31e0e1b.CODE.1.ADDR.64fe00000008.INSTR.mov____0x8(%r15),%r12.pyc`
  - ... 1 more

### 37. cpython-314-abde21376072

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a95a1b30`
- Honggfuzz stack hash: `18a95a1b30`
- PC: `0x57cff579681c`
- Fault address: `0x0`
- Instruction: `mov____(%r12),%ebx`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-abde21376072.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff579681c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff579681c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000757efaf50180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff579681c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dcf5159b7c3.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ede10f2981c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f770188781c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6468926b981c.STACK.18a95a1b30.CODE.1.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - ... 1 more

### 38. cpython-314-af093711f474

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f1dc4645e`
- Honggfuzz stack hash: `f1dc4645e`
- PC: `0x57f90afceca0`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 6
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-af093711f474.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f90afceca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f90afceca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b307e9d5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f90afceca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58ab4062fca0.STACK.f1dc4645e.CODE.1.ADDR.4018.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.598cfc5fdca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.601defa13ca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60e4090c8ca0.STACK.f1dc4645e.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - ... 1 more

### 39. cpython-314-2ca6b481bfea

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183f7c3bf1`
- Honggfuzz stack hash: `183f7c3bf1`
- PC: `0x5690bdd04c4b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2ca6b481bfea.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5690bdd04c4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5690bdd04c4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bda54fea180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5690bdd04c4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57def58ecc4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59dc8e98fc4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f43934b3c4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.624512846c4b.STACK.183f7c3bf1.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`

### 40. cpython-314-4c666ca029df

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de38df57c`
- Honggfuzz stack hash: `de38df57c`
- PC: `0x56d35796ffc2`
- Fault address: `0x0`
- Instruction: `cmp____%rax,0x20(%r15)`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-4c666ca029df.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d35796ffc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d35796ffc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007648f93b2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56d35796ffc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a24b7334fc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f009530dfc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60ea0913efc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.623a61987fc2.STACK.de38df57c.CODE.128.ADDR.0.INSTR.cmp____%rax,0x20(%r15).pyc`

### 41. cpython-314-5adae8edfb1a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bc2a7e4fb`
- Honggfuzz stack hash: `1bc2a7e4fb`
- PC: `0x560c3f5a0572`
- Fault address: `0x560c00000008`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5adae8edfb1a.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560c3f5a0572.STACK.1bc2a7e4fb.CODE.1.ADDR.560c00000008.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560c3f5a0572.STACK.1bc2a7e4fb.CODE.1.ADDR.560c00000008.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000070184d567180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.560c3f5a0572.STACK.1bc2a7e4fb.CODE.1.ADDR.560c00000008.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a821fe13fe2.STACK.1bc2a7e4fb.CODE.1.ADDR.5a8200000008.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a98ff9be58d.STACK.1bc2a7e4fb.CODE.128.ADDR.0.INSTR.mov____(%rax),%r13.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c58ac584572.STACK.1bc2a7e4fb.CODE.1.ADDR.5c5800000008.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d91e0083572.STACK.1bc2a7e4fb.CODE.1.ADDR.5d9100000008.INSTR.mov____0x8(%r15),%rbx.pyc`

### 42. cpython-314-8dcba47075c4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ce01c19be`
- Honggfuzz stack hash: `ce01c19be`
- PC: `0x5d7072267c4b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8dcba47075c4.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d7072267c4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d7072267c4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000701b88849180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d7072267c4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f746ca3bc4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60db971bbc4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.628a99144c4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63e0fa0dec4b.STACK.ce01c19be.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%r14.pyc`

### 43. cpython-314-90438060db78

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dbd1d07b1`
- Honggfuzz stack hash: `dbd1d07b1`
- PC: `0x593a20a6b4ed`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-90438060db78.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.593a20a6b4ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.593a20a6b4ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078b402aa1180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.593a20a6b4ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59bbdf6434ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b7831b424ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bd8853f04ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d73491794ed.STACK.dbd1d07b1.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`

### 44. cpython-314-9b52a0daa1ec

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:182edd29c2`
- Honggfuzz stack hash: `182edd29c2`
- PC: `0x55ed8c4ef1bc`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9b52a0daa1ec.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ed8c4ef1bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ed8c4ef1bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071b27273f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ed8c4ef1bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c51cac981bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.604b8ad811bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.634563d231bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.654dbf3c01bc.STACK.182edd29c2.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`

### 45. cpython-314-ae94c10af9cf

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c062ff69a`
- Honggfuzz stack hash: `c062ff69a`
- PC: `0x56377ab346bd`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-ae94c10af9cf.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56377ab346bd.STACK.c062ff69a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56377ab346bd.STACK.c062ff69a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bd69b846180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56377ab346bd.STACK.c062ff69a.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.575e3d8396f4.STACK.c062ff69a.CODE.1.ADDR.575e00000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf5d2b906bd.STACK.c062ff69a.CODE.1.ADDR.41.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cd2ba5f46bd.STACK.c062ff69a.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60b84a0d66bd.STACK.c062ff69a.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 46. cpython-314-ccf893fa30a8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f99de572`
- Honggfuzz stack hash: `19f99de572`
- PC: `0x55c51c77de1b`
- Fault address: `0x55c500000008`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 5
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-ccf893fa30a8.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c51c77de1b.STACK.19f99de572.CODE.1.ADDR.55c500000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c51c77de1b.STACK.19f99de572.CODE.1.ADDR.55c500000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073acb848c180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c51c77de1b.STACK.19f99de572.CODE.1.ADDR.55c500000008.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dec081c2e1b.STACK.19f99de572.CODE.1.ADDR.5dec00000008.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df73e2cbe1b.STACK.19f99de572.CODE.1.ADDR.5df700000008.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63875727de1b.STACK.19f99de572.CODE.1.ADDR.638700000008.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.653aa9369e1b.STACK.19f99de572.CODE.1.ADDR.653a00000008.INSTR.mov____0x8(%r14),%r15.pyc`

### 47. cpython-314-0c8332b00d51

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf34bca28`
- Honggfuzz stack hash: `cf34bca28`
- PC: `0x5c09a3358d35`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0c8332b00d51.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c09a3358d35.STACK.cf34bca28.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c09a3358d35.STACK.cf34bca28.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e02fa3c1180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c09a3358d35.STACK.cf34bca28.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d5d9f0d9f67.STACK.cf34bca28.CODE.128.ADDR.0.INSTR.mov____%r15,(%r14,%rbx,1).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e92e3841fe5.STACK.cf34bca28.CODE.1.ADDR.10.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6193d15b8572.STACK.cf34bca28.CODE.1.ADDR.81.INSTR.mov____(%r15),%ebx.pyc`

### 48. cpython-314-225bd6d6a92d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f9acd207`
- Honggfuzz stack hash: `19f9acd207`
- PC: `0x557075eb08b4`
- Fault address: `0x557000000008`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-225bd6d6a92d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.557075eb08b4.STACK.19f9acd207.CODE.1.ADDR.557000000008.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.557075eb08b4.STACK.19f9acd207.CODE.1.ADDR.557000000008.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000076fb25a6d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.557075eb08b4.STACK.19f9acd207.CODE.1.ADDR.557000000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5679e8a178b4.STACK.19f9acd207.CODE.1.ADDR.567900000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58762684e8b4.STACK.19f9acd207.CODE.1.ADDR.587600000008.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d7642f85938.STACK.19f9acd207.CODE.128.ADDR.0.INSTR.mov____0x20(%rbx),%r12.pyc`

### 49. cpython-314-2c4d41c7c24c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a97ba304`
- Honggfuzz stack hash: `18a97ba304`
- PC: `0x573dee55dbaf`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2c4d41c7c24c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573dee55dbaf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573dee55dbaf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b2cef0e6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573dee55dbaf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58312ded9baf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b478072cbaf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ede7c87fbaf.STACK.18a97ba304.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rax.pyc`

### 50. cpython-314-577e3c4ccb19

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ca101bcc6`
- Honggfuzz stack hash: `ca101bcc6`
- PC: `0x558b0cb0b040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-577e3c4ccb19.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558b0cb0b040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558b0cb0b040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071014d79e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.558b0cb0b040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a69b7a79040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60a0bcfce040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62dd8dd7e040.STACK.ca101bcc6.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 51. cpython-314-57bf00f7a7f2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18bc13dc4a`
- Honggfuzz stack hash: `18bc13dc4a`
- PC: `0x56ff7ebf8514`
- Fault address: `0x0`
- Instruction: `mov____0x8(%rax),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-57bf00f7a7f2.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56ff7ebf8514.STACK.18bc13dc4a.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56ff7ebf8514.STACK.18bc13dc4a.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000075ec601dd180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56ff7ebf8514.STACK.18bc13dc4a.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.595fe7e1d514.STACK.18bc13dc4a.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a3b4d96f673.STACK.18bc13dc4a.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ff01c10a514.STACK.18bc13dc4a.CODE.1.ADDR.103340e64.INSTR.mov____0x8(%rax),%rax.pyc`

### 52. cpython-314-5806ac523007

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d906e575f`
- Honggfuzz stack hash: `d906e575f`
- PC: `0x564db09851bc`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5806ac523007.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564db09851bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564db09851bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000711dc540e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.564db09851bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e5e8fef81bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ef426a371bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60a5d8f271bc.STACK.d906e575f.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`

### 53. cpython-314-723985b4fbf7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f1dc7c6b4`
- Honggfuzz stack hash: `f1dc7c6b4`
- PC: `0x56861a895572`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-723985b4fbf7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56861a895572.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56861a895572.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000070b222efe180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56861a895572.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5962d5c5d572.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62525991cfe2.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62ef33413572.STACK.f1dc7c6b4.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rbx.pyc`

### 54. cpython-314-7bfff901f543

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193eda05a5`
- Honggfuzz stack hash: `193eda05a5`
- PC: `0x56b2cf0178b0`
- Fault address: `0x56b2cf0178b0`
- Instruction: `add____(%rax),%al`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-7bfff901f543.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b2cf0178b0.STACK.193eda05a5.CODE.2.ADDR.56b2cf0178b0.INSTR.add____(%rax),%al.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b2cf0178b0.STACK.193eda05a5.CODE.2.ADDR.56b2cf0178b0.INSTR.add____(%rax),%al.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ebe563dd180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b2cf0178b0.STACK.193eda05a5.CODE.2.ADDR.56b2cf0178b0.INSTR.add____(%rax),%al.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59250702a620.STACK.193eda05a5.CODE.2.ADDR.59250702a620.INSTR.add____(%rax),%al.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.619f1372e190.STACK.193eda05a5.CODE.2.ADDR.619f1372e190.INSTR.add____(%rax),%al.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.638ea00e1670.STACK.193eda05a5.CODE.2.ADDR.638ea00e1670.INSTR.add____(%rax),%al.pyc`

### 55. cpython-314-9e8374ff344c

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:cf8abaffd`
- Honggfuzz stack hash: `cf8abaffd`
- PC: `0x711e5abd99fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9e8374ff344c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.711e5abd99fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.711e5abd99fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074f3af2b9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.711e5abd99fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.724db347c9fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7a638147b9fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7a70f1a579fc.STACK.cf8abaffd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 56. cpython-314-c3dd1b67c44a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183c543162`
- Honggfuzz stack hash: `183c543162`
- PC: `0x57f5089dac4f`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c3dd1b67c44a.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f5089dac4f.STACK.183c543162.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f5089dac4f.STACK.183c543162.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e667db8b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57f5089dac4f.STACK.183c543162.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a1b5e62fc4f.STACK.183c543162.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc3b3c34c4b.STACK.183c543162.CODE.1.ADDR.5bc300000008.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6224c337d0c0.STACK.183c543162.CODE.2.ADDR.6224c337d0c0.INSTR.(bad)__.pyc`

### 57. cpython-314-d71d7dfce592

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1830fcfecd`
- Honggfuzz stack hash: `1830fcfecd`
- PC: `0x5fb29e3f4152`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d71d7dfce592.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb29e3f4152.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb29e3f4152.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000738ec12f2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb29e3f4152.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.616d188ce19f.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61f88180f152.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.641b2271d152.STACK.1830fcfecd.CODE.1.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 58. cpython-314-db203af4d089

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18637a75a0`
- Honggfuzz stack hash: `18637a75a0`
- PC: `0x567ac283f6f4`
- Fault address: `0x567a00000000`
- Instruction: `mov____(%r14),%ebx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-db203af4d089.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.567ac283f6f4.STACK.18637a75a0.CODE.1.ADDR.567a00000000.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.567ac283f6f4.STACK.18637a75a0.CODE.1.ADDR.567a00000000.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b44f46b6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.567ac283f6f4.STACK.18637a75a0.CODE.1.ADDR.567a00000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56f926e886f4.STACK.18637a75a0.CODE.1.ADDR.56f900000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc5730606f4.STACK.18637a75a0.CODE.1.ADDR.5bc500000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c9feaef16f4.STACK.18637a75a0.CODE.1.ADDR.5ca000000000.INSTR.mov____(%r14),%ebx.pyc`

### 59. cpython-314-e5e6ebcceab8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db66a3df8`
- Honggfuzz stack hash: `db66a3df8`
- PC: `0x57ed0126d98e`
- Fault address: `0x0`
- Instruction: `call___*%rbx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e5e6ebcceab8.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57ed0126d98e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57ed0126d98e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d06457bc180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57ed0126d98e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5894117a498e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60eda71ea98e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63fc2bd8a98e.STACK.db66a3df8.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`

### 60. cpython-314-eab2971674c1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:187bae1494`
- Honggfuzz stack hash: `187bae1494`
- PC: `0x56cb8c6ef1c0`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%rax),%rbx`
- Findings: 4
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-eab2971674c1.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56cb8c6ef1c0.STACK.187bae1494.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56cb8c6ef1c0.STACK.187bae1494.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000072558fdc5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56cb8c6ef1c0.STACK.187bae1494.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58f668e181bc.STACK.187bae1494.CODE.1.ADDR.58f600000008.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a9802c6c1bc.STACK.187bae1494.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b3463f3c1bc.STACK.187bae1494.CODE.1.ADDR.5b3400000008.INSTR.mov____0x8(%r14),%rax.pyc`

### 61. cpython-314-302b0956a5f7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a39b1cf4f`
- Honggfuzz stack hash: `1a39b1cf4f`
- PC: `0x588de76c3f5c`
- Fault address: `0x0`
- Instruction: `mov____0x10(%r13),%r12`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-302b0956a5f7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.588de76c3f5c.STACK.1a39b1cf4f.CODE.128.ADDR.0.INSTR.mov____0x10(%r13),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.588de76c3f5c.STACK.1a39b1cf4f.CODE.128.ADDR.0.INSTR.mov____0x10(%r13),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ddcc247a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.588de76c3f5c.STACK.1a39b1cf4f.CODE.128.ADDR.0.INSTR.mov____0x10(%r13),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5913db02cf5c.STACK.1a39b1cf4f.CODE.128.ADDR.0.INSTR.mov____0x10(%r13),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e6464fdef5c.STACK.1a39b1cf4f.CODE.128.ADDR.0.INSTR.mov____0x10(%r13),%r12.pyc`

### 62. cpython-314-46573aed81ca

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197ff575cc`
- Honggfuzz stack hash: `197ff575cc`
- PC: `0x5b3a92bcd540`
- Fault address: `0x5b3a00000008`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-46573aed81ca.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b3a92bcd540.STACK.197ff575cc.CODE.1.ADDR.5b3a00000008.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b3a92bcd540.STACK.197ff575cc.CODE.1.ADDR.5b3a00000008.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ac2880a9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b3a92bcd540.STACK.197ff575cc.CODE.1.ADDR.5b3a00000008.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.602858f3f540.STACK.197ff575cc.CODE.1.ADDR.602800000008.INSTR.mov____0x8(%rbx),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.649533249540.STACK.197ff575cc.CODE.1.ADDR.649500000008.INSTR.mov____0x8(%rbx),%r12.pyc`

### 63. cpython-314-5e1240bec101

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a9ffbf99`
- Honggfuzz stack hash: `18a9ffbf99`
- PC: `0x57cff1bee319`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5e1240bec101.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff1bee319.STACK.18a9ffbf99.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff1bee319.STACK.18a9ffbf99.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e7215975180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57cff1bee319.STACK.18a9ffbf99.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d3cfd36f319.STACK.18a9ffbf99.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.630deb264319.STACK.18a9ffbf99.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%rax.pyc`

### 64. cpython-314-64285b41369c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f8bd4476a`
- Honggfuzz stack hash: `f8bd4476a`
- PC: `0x575f625be4da`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r12),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-64285b41369c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.575f625be4da.STACK.f8bd4476a.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.575f625be4da.STACK.f8bd4476a.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077d48b8ed180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.575f625be4da.STACK.f8bd4476a.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cecccb224da.STACK.f8bd4476a.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f498f5ae4da.STACK.f8bd4476a.CODE.128.ADDR.0.INSTR.mov____0x8(%r12),%rbx.pyc`

### 65. cpython-314-655479a89ec3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bb96a8871`
- Honggfuzz stack hash: `1bb96a8871`
- PC: `0x5aad9cd0478f`
- Fault address: `0x5f5f746369`
- Instruction: `mov____(%r14),%ebx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-655479a89ec3.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aad9cd0478f.STACK.1bb96a8871.CODE.1.ADDR.5f5f746369.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aad9cd0478f.STACK.1bb96a8871.CODE.1.ADDR.5f5f746369.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000072ad2627e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aad9cd0478f.STACK.1bb96a8871.CODE.1.ADDR.5f5f746369.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b95a674878f.STACK.1bb96a8871.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c004609f78f.STACK.1bb96a8871.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 66. cpython-314-720f0462382f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf4a78bf3`
- Honggfuzz stack hash: `cf4a78bf3`
- PC: `0x57574484978a`
- Fault address: `0x0`
- Instruction: `mov____0x0(%r13),%r15d`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-720f0462382f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57574484978a.STACK.cf4a78bf3.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57574484978a.STACK.cf4a78bf3.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007add3becd180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57574484978a.STACK.cf4a78bf3.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6345d73d378a.STACK.cf4a78bf3.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.645adb91678a.STACK.cf4a78bf3.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r15d.pyc`

### 67. cpython-314-74d4bd038b92

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bc2a44611`
- Honggfuzz stack hash: `1bc2a44611`
- PC: `0x568b8f895ca0`
- Fault address: `0x568b00000008`
- Instruction: `mov____0x8(%rbx),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-74d4bd038b92.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.568b8f895ca0.STACK.1bc2a44611.CODE.1.ADDR.568b00000008.INSTR.mov____0x8(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.568b8f895ca0.STACK.1bc2a44611.CODE.1.ADDR.568b00000008.INSTR.mov____0x8(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000799c61f31180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.568b8f895ca0.STACK.1bc2a44611.CODE.1.ADDR.568b00000008.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a047f966ca0.STACK.1bc2a44611.CODE.1.ADDR.5a0400000008.INSTR.mov____0x8(%rbx),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63e4d100aca0.STACK.1bc2a44611.CODE.1.ADDR.63e400000008.INSTR.mov____0x8(%rbx),%rax.pyc`

### 68. cpython-314-9c659a964321

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d269cc9e9`
- Honggfuzz stack hash: `d269cc9e9`
- PC: `0x5bf70e5941a7`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r12d`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9c659a964321.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf70e5941a7.STACK.d269cc9e9.CODE.1.ADDR.0.INSTR.mov____(%r14),%r12d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf70e5941a7.STACK.d269cc9e9.CODE.1.ADDR.0.INSTR.mov____(%r14),%r12d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078866a8bc180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf70e5941a7.STACK.d269cc9e9.CODE.1.ADDR.0.INSTR.mov____(%r14),%r12d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c019b6ea962.STACK.d269cc9e9.CODE.1.ADDR.5c01e4d41000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df20a902962.STACK.d269cc9e9.CODE.1.ADDR.5df252a6f000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`

### 69. cpython-314-9f463573ffca

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:194220b127`
- Honggfuzz stack hash: `194220b127`
- PC: `0x5817244bfda2`
- Fault address: `0x0`
- Instruction: `mov____0x0(%r13),%r14d`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9f463573ffca.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5817244bfda2.STACK.194220b127.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5817244bfda2.STACK.194220b127.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073a2e7dd0180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5817244bfda2.STACK.194220b127.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a09c9acada2.STACK.194220b127.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d13c590eda2.STACK.194220b127.CODE.128.ADDR.0.INSTR.mov____0x0(%r13),%r14d.pyc`

### 70. cpython-314-a50542192284

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db2dd9610`
- Honggfuzz stack hash: `db2dd9610`
- PC: `0x55e21d649fc7`
- Fault address: `0x0`
- Instruction: `mov____0x9(%r14),%cl`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a50542192284.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55e21d649fc7.STACK.db2dd9610.CODE.128.ADDR.0.INSTR.mov____0x9(%r14),%cl.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55e21d649fc7.STACK.db2dd9610.CODE.128.ADDR.0.INSTR.mov____0x9(%r14),%cl.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007dfac4567180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55e21d649fc7.STACK.db2dd9610.CODE.128.ADDR.0.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ed5f131fc7.STACK.db2dd9610.CODE.128.ADDR.0.INSTR.mov____0x9(%r14),%cl.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56103faa5fc7.STACK.db2dd9610.CODE.128.ADDR.0.INSTR.mov____0x9(%r14),%cl.pyc`

### 71. cpython-314-a61213c31a3f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b3e6b1436`
- Honggfuzz stack hash: `1b3e6b1436`
- PC: `0x55c98afb37b8`
- Fault address: `0x55c900000008`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a61213c31a3f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c98afb37b8.STACK.1b3e6b1436.CODE.1.ADDR.55c900000008.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c98afb37b8.STACK.1b3e6b1436.CODE.1.ADDR.55c900000008.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071b6cc05d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55c98afb37b8.STACK.1b3e6b1436.CODE.1.ADDR.55c900000008.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5de9dad4c7b8.STACK.1b3e6b1436.CODE.1.ADDR.5dea00000008.INSTR.mov____0x8(%rbx),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60522ab967b8.STACK.1b3e6b1436.CODE.1.ADDR.605200000008.INSTR.mov____0x8(%rbx),%r15.pyc`

### 72. cpython-314-ab31a0422514

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:182fff3968`
- Honggfuzz stack hash: `182fff3968`
- PC: `0x582f589b996e`
- Fault address: `0x78`
- Instruction: `mov____0x78(%r15),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-ab31a0422514.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.582f589b996e.STACK.182fff3968.CODE.1.ADDR.78.INSTR.mov____0x78(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.582f589b996e.STACK.182fff3968.CODE.1.ADDR.78.INSTR.mov____0x78(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b8abfec7180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.582f589b996e.STACK.182fff3968.CODE.1.ADDR.78.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bd3bd07196e.STACK.182fff3968.CODE.1.ADDR.99.INSTR.mov____0x78(%r15),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.ffffffffffffffff.STACK.182fff3968.CODE.1.ADDR.ffffffffffffffff.INSTR.[NOT_MMAPED].pyc`

### 73. cpython-314-bcc32edb6e38

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c6373fe05`
- Honggfuzz stack hash: `c6373fe05`
- PC: `0x5b0fa51ec514`
- Fault address: `0x58`
- Instruction: `mov____0x8(%rax),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-bcc32edb6e38.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b0fa51ec514.STACK.c6373fe05.CODE.1.ADDR.58.INSTR.mov____0x8(%rax),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b0fa51ec514.STACK.c6373fe05.CODE.1.ADDR.58.INSTR.mov____0x8(%rax),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074cd2a110180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5b0fa51ec514.STACK.c6373fe05.CODE.1.ADDR.58.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61e7e07ae514.STACK.c6373fe05.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62175d53b514.STACK.c6373fe05.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rax.pyc`

### 74. cpython-314-bdaf6533e43a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193e8f0df6`
- Honggfuzz stack hash: `193e8f0df6`
- PC: `0x5a0755f79cd2`
- Fault address: `0x180070`
- Instruction: `mov____0x70(%r15),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-bdaf6533e43a.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0755f79cd2.STACK.193e8f0df6.CODE.1.ADDR.180070.INSTR.mov____0x70(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0755f79cd2.STACK.193e8f0df6.CODE.1.ADDR.180070.INSTR.mov____0x70(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000735a778d3180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0755f79cd2.STACK.193e8f0df6.CODE.1.ADDR.180070.INSTR.mov____0x70(%r15),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d82f4223cd2.STACK.193e8f0df6.CODE.1.ADDR.71.INSTR.mov____0x70(%r15),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6313894e7cdb.STACK.193e8f0df6.CODE.128.ADDR.0.INSTR.mov____0x8(%rax),%rbx.pyc`

### 75. cpython-314-cb6e1c510afa

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c769f9dd6`
- Honggfuzz stack hash: `c769f9dd6`
- PC: `0x5ebe30c36256`
- Fault address: `0x5ebe00000008`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cb6e1c510afa.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ebe30c36256.STACK.c769f9dd6.CODE.1.ADDR.5ebe00000008.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ebe30c36256.STACK.c769f9dd6.CODE.1.ADDR.5ebe00000008.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073a47e022180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ebe30c36256.STACK.c769f9dd6.CODE.1.ADDR.5ebe00000008.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60ed93bd0256.STACK.c769f9dd6.CODE.1.ADDR.60ed00000008.INSTR.mov____0x8(%r13),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.624cc2252256.STACK.c769f9dd6.CODE.1.ADDR.624c00000008.INSTR.mov____0x8(%r13),%r14.pyc`

### 76. cpython-314-d96c489927c6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d725c4540`
- Honggfuzz stack hash: `d725c4540`
- PC: `0x5db7a720f26b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d96c489927c6.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5db7a720f26b.STACK.d725c4540.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5db7a720f26b.STACK.d725c4540.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000784b13d75180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5db7a720f26b.STACK.d725c4540.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6446fe91b26b.STACK.d725c4540.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.650ae7fd926b.STACK.d725c4540.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`

### 77. cpython-314-e88942f907f1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dc51d6a09`
- Honggfuzz stack hash: `dc51d6a09`
- PC: `0x5903b219d1bc`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e88942f907f1.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5903b219d1bc.STACK.dc51d6a09.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5903b219d1bc.STACK.dc51d6a09.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b0bcd872180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5903b219d1bc.STACK.dc51d6a09.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59408c4c11c0.STACK.dc51d6a09.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e8873dc31bc.STACK.dc51d6a09.CODE.1.ADDR.5e8800000008.INSTR.mov____0x8(%r14),%rax.pyc`

### 78. cpython-314-eecb6adb9aec

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d26fdc73d`
- Honggfuzz stack hash: `d26fdc73d`
- PC: `0x59e7a3b97e1b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 3
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-eecb6adb9aec.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59e7a3b97e1b.STACK.d26fdc73d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59e7a3b97e1b.STACK.d26fdc73d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007f4774c86180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59e7a3b97e1b.STACK.d26fdc73d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d0e07772e1b.STACK.d26fdc73d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fd2fa849e1b.STACK.d26fdc73d.CODE.1.ADDR.8.INSTR.mov____0x8(%r14),%r15.pyc`

### 79. cpython-314-0511409be235

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bd11ee1f9`
- Honggfuzz stack hash: `1bd11ee1f9`
- PC: `0x5d770b70b040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0511409be235.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d770b70b040.STACK.1bd11ee1f9.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d770b70b040.STACK.1bd11ee1f9.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074536c180180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d770b70b040.STACK.1bd11ee1f9.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.629af33d2040.STACK.1bd11ee1f9.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 80. cpython-314-09da4ed02f1e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d7c498582`
- Honggfuzz stack hash: `d7c498582`
- PC: `0x5671e95b8351`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-09da4ed02f1e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5671e95b8351.STACK.d7c498582.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5671e95b8351.STACK.d7c498582.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000721c3b2d5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5671e95b8351.STACK.d7c498582.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c8ba6c75351.STACK.d7c498582.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rax.pyc`

### 81. cpython-314-0cf9e155f83f

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19f4ddd5cb`
- Honggfuzz stack hash: `19f4ddd5cb`
- PC: `0x703c94bc39fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0cf9e155f83f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.703c94bc39fc.STACK.19f4ddd5cb.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.703c94bc39fc.STACK.19f4ddd5cb.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007df259190180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.703c94bc39fc.STACK.19f4ddd5cb.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.754a1cfd49fc.STACK.19f4ddd5cb.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 82. cpython-314-12a72b9a43c4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e095be506`
- Honggfuzz stack hash: `e095be506`
- PC: `0x590dfa356040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-12a72b9a43c4.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.590dfa356040.STACK.e095be506.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.590dfa356040.STACK.e095be506.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b166c421180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.590dfa356040.STACK.e095be506.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f935a99a040.STACK.e095be506.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 83. cpython-314-1ecbc28d2f88

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de11a6550`
- Honggfuzz stack hash: `de11a6550`
- PC: `0x5d72c205148a`
- Fault address: `0x2d`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-1ecbc28d2f88.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d72c205148a.STACK.de11a6550.CODE.1.ADDR.2d.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d72c205148a.STACK.de11a6550.CODE.1.ADDR.2d.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007994057be180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d72c205148a.STACK.de11a6550.CODE.1.ADDR.2d.INSTR.mov____0x8(%r15),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6347cd8f348a.STACK.de11a6550.CODE.1.ADDR.49.INSTR.mov____0x8(%r15),%rax.pyc`

### 84. cpython-314-30f0a9a47546

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de1ef2fb9`
- Honggfuzz stack hash: `de1ef2fb9`
- PC: `0x56e2dd1dacce`
- Fault address: `0x56e300000008`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-30f0a9a47546.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e2dd1dacce.STACK.de1ef2fb9.CODE.1.ADDR.56e300000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e2dd1dacce.STACK.de1ef2fb9.CODE.1.ADDR.56e300000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000075a722c4b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e2dd1dacce.STACK.de1ef2fb9.CODE.1.ADDR.56e300000008.INSTR.mov____0x8(%r14),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a49f6389cd2.STACK.de1ef2fb9.CODE.1.ADDR.70.INSTR.mov____0x70(%r15),%rax.pyc`

### 85. cpython-314-373d8637d748

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a71de6e2a`
- Honggfuzz stack hash: `1a71de6e2a`
- PC: `0x6115d69ef73c`
- Fault address: `0x0`
- Instruction: `movzbl_(%rax,%rbx,1),%r13d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-373d8637d748.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6115d69ef73c.STACK.1a71de6e2a.CODE.1.ADDR.0.INSTR.movzbl_(%rax,%rbx,1),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6115d69ef73c.STACK.1a71de6e2a.CODE.1.ADDR.0.INSTR.movzbl_(%rax,%rbx,1),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071aac3161180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6115d69ef73c.STACK.1a71de6e2a.CODE.1.ADDR.0.INSTR.movzbl_(%rax,%rbx,1),%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61504884f73c.STACK.1a71de6e2a.CODE.1.ADDR.0.INSTR.movzbl_(%rax,%rbx,1),%r13d.pyc`

### 86. cpython-314-44114397e1f2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18637b5dc6`
- Honggfuzz stack hash: `18637b5dc6`
- PC: `0x62626c0bd8b4`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-44114397e1f2.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62626c0bd8b4.STACK.18637b5dc6.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62626c0bd8b4.STACK.18637b5dc6.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073c468aea180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62626c0bd8b4.STACK.18637b5dc6.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.628a79a598b4.STACK.18637b5dc6.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rax.pyc`

### 87. cpython-314-54b9383c41c2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cf18cb179`
- Honggfuzz stack hash: `cf18cb179`
- PC: `0x56b4a769b441`
- Fault address: `0x56b400000008`
- Instruction: `mov____0x8(%rax),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-54b9383c41c2.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b4a769b441.STACK.cf18cb179.CODE.1.ADDR.56b400000008.INSTR.mov____0x8(%rax),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b4a769b441.STACK.cf18cb179.CODE.1.ADDR.56b400000008.INSTR.mov____0x8(%rax),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b13c24e2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56b4a769b441.STACK.cf18cb179.CODE.1.ADDR.56b400000008.INSTR.mov____0x8(%rax),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.62ff40a614ab.STACK.cf18cb179.CODE.1.ADDR.62ff00000008.INSTR.mov____0x8(%rax),%rax.pyc`

### 88. cpython-314-578d0de35ad6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de2b1348e`
- Honggfuzz stack hash: `de2b1348e`
- PC: `0x59fa86b0e4c0`
- Fault address: `0x59fa87419e`
- Instruction: `mov____0xa8(%rax),%r14`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-578d0de35ad6.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59fa86b0e4c0.STACK.de2b1348e.CODE.1.ADDR.59fa87419e.INSTR.mov____0xa8(%rax),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59fa86b0e4c0.STACK.de2b1348e.CODE.1.ADDR.59fa87419e.INSTR.mov____0xa8(%rax),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007078aabaf180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59fa86b0e4c0.STACK.de2b1348e.CODE.1.ADDR.59fa87419e.INSTR.mov____0xa8(%rax),%r14.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f65b73814c0.STACK.de2b1348e.CODE.1.ADDR.5f65b7c8ce.INSTR.mov____0xa8(%rax),%r14.pyc`

### 89. cpython-314-5e23ec4841ac

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:18bf63e665`
- Honggfuzz stack hash: `18bf63e665`
- PC: `0x7644964de9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5e23ec4841ac.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7644964de9fc.STACK.18bf63e665.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7644964de9fc.STACK.18bf63e665.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bd2b04c2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7644964de9fc.STACK.18bf63e665.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7ef6b0df89fc.STACK.18bf63e665.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 90. cpython-314-5f874a277b47

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cef9cdc82`
- Honggfuzz stack hash: `cef9cdc82`
- PC: `0x61cd9bed019f`
- Fault address: `0x61cd00000000`
- Instruction: `mov____(%r14),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5f874a277b47.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61cd9bed019f.STACK.cef9cdc82.CODE.1.ADDR.61cd00000000.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61cd9bed019f.STACK.cef9cdc82.CODE.1.ADDR.61cd00000000.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000718af478b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61cd9bed019f.STACK.cef9cdc82.CODE.1.ADDR.61cd00000000.INSTR.mov____(%r14),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.632c36a30152.STACK.cef9cdc82.CODE.1.ADDR.632c00000000.INSTR.mov____(%r15),%ebx.pyc`

### 91. cpython-314-6e4a25e03b51

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b9a223086`
- Honggfuzz stack hash: `1b9a223086`
- PC: `0x573d7a1416df`
- Fault address: `0xa7`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-6e4a25e03b51.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573d7a1416df.STACK.1b9a223086.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573d7a1416df.STACK.1b9a223086.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000076cb88242180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.573d7a1416df.STACK.1b9a223086.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59df3a1016df.STACK.1b9a223086.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`

### 92. cpython-314-706fbfce0a17

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a4b11b095`
- Honggfuzz stack hash: `1a4b11b095`
- PC: `0x562fb1e5f442`
- Fault address: `0x1`
- Instruction: `mov____(%r15),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-706fbfce0a17.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562fb1e5f442.STACK.1a4b11b095.CODE.1.ADDR.1.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562fb1e5f442.STACK.1a4b11b095.CODE.1.ADDR.1.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000079bdefff2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.562fb1e5f442.STACK.1a4b11b095.CODE.1.ADDR.1.INSTR.mov____(%r15),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a1828109442.STACK.1a4b11b095.CODE.1.ADDR.1.INSTR.mov____(%r15),%ebx.pyc`

### 93. cpython-314-79690c504734

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d64f2b78d`
- Honggfuzz stack hash: `d64f2b78d`
- PC: `0x5d2bf96e6397`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-79690c504734.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2bf96e6397.STACK.d64f2b78d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2bf96e6397.STACK.d64f2b78d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007384d9ca4180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2bf96e6397.STACK.d64f2b78d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f32ab28e397.STACK.d64f2b78d.CODE.1.ADDR.8.INSTR.mov____0x8(%r13),%rbx.pyc`

### 94. cpython-314-89e10f2c9b87

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d2c03e653`
- Honggfuzz stack hash: `d2c03e653`
- PC: `0x58627c2c1435`
- Fault address: `0x10`
- Instruction: `mov____0x10(%rax),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-89e10f2c9b87.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58627c2c1435.STACK.d2c03e653.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58627c2c1435.STACK.d2c03e653.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077649681d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58627c2c1435.STACK.d2c03e653.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.589cee990572.STACK.d2c03e653.CODE.1.ADDR.41.INSTR.mov____(%r15),%ebx.pyc`

### 95. cpython-314-8a32c3ca8618

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c763a397f`
- Honggfuzz stack hash: `c763a397f`
- PC: `0x607a1d9a17c3`
- Fault address: `0x607a00000000`
- Instruction: `mov____0x0(%r13),%r14d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8a32c3ca8618.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.607a1d9a17c3.STACK.c763a397f.CODE.1.ADDR.607a00000000.INSTR.mov____0x0(%r13),%r14d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.607a1d9a17c3.STACK.c763a397f.CODE.1.ADDR.607a00000000.INSTR.mov____0x0(%r13),%r14d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000079c74dd0b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.607a1d9a17c3.STACK.c763a397f.CODE.1.ADDR.607a00000000.INSTR.mov____0x0(%r13),%r14d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.64c8733c47c3.STACK.c763a397f.CODE.1.ADDR.64c800000000.INSTR.mov____0x0(%r13),%r14d.pyc`

### 96. cpython-314-8cd89f80ff40

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d7a4b265b`
- Honggfuzz stack hash: `d7a4b265b`
- PC: `0x598656d9d1cd`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8cd89f80ff40.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.598656d9d1cd.STACK.d7a4b265b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.598656d9d1cd.STACK.d7a4b265b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000791c7d55e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.598656d9d1cd.STACK.d7a4b265b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e12e5ea41cd.STACK.d7a4b265b.CODE.128.ADDR.0.INSTR.mov____0xa8(%r14),%rbx.pyc`

### 97. cpython-314-90be3ee878fb

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:cb8234a76`
- Honggfuzz stack hash: `cb8234a76`
- PC: `0x789d3a9839fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-90be3ee878fb.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.789d3a9839fc.STACK.cb8234a76.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.789d3a9839fc.STACK.cb8234a76.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007cd0ab405180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.789d3a9839fc.STACK.cb8234a76.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7e11ff53b9fc.STACK.cb8234a76.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 98. cpython-314-a0782edc41c4

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fdf0ec89d`
- Honggfuzz stack hash: `fdf0ec89d`
- PC: `0x5a18ce383fca`
- Fault address: `0x5a1800000008`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a0782edc41c4.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a18ce383fca.STACK.fdf0ec89d.CODE.1.ADDR.5a1800000008.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a18ce383fca.STACK.fdf0ec89d.CODE.1.ADDR.5a1800000008.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b2487154180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a18ce383fca.STACK.fdf0ec89d.CODE.1.ADDR.5a1800000008.INSTR.mov____0x8(%r13),%r15.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.613c6b41dfd3.STACK.fdf0ec89d.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%rsi.pyc`

### 99. cpython-314-b036fdf2d7b1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de66d334d`
- Honggfuzz stack hash: `de66d334d`
- PC: `0x56f2ab133750`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%r12`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b036fdf2d7b1.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56f2ab133750.STACK.de66d334d.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56f2ab133750.STACK.de66d334d.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074f686370180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56f2ab133750.STACK.de66d334d.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.638d0d65d750.STACK.de66d334d.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r12.pyc`

### 100. cpython-314-b8b61310a397

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193d39e786`
- Honggfuzz stack hash: `193d39e786`
- PC: `0x56e9eb7167b0`
- Fault address: `0x56e9eb7167b0`
- Instruction: `add____(%rax),%eax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b8b61310a397.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e9eb7167b0.STACK.193d39e786.CODE.2.ADDR.56e9eb7167b0.INSTR.add____(%rax),%eax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e9eb7167b0.STACK.193d39e786.CODE.2.ADDR.56e9eb7167b0.INSTR.add____(%rax),%eax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007dd2ebd07180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56e9eb7167b0.STACK.193d39e786.CODE.2.ADDR.56e9eb7167b0.INSTR.add____(%rax),%eax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.584d4b529af0.STACK.193d39e786.CODE.2.ADDR.584d4b529af0.INSTR.add____(%rax),%eax.pyc`

### 101. cpython-314-b95ad5268920

- Status: crash
- Signal: SIGBUS
- Stack source: honggfuzz-filename
- Stack signature: `SIGBUS:19f6b967ca`
- Honggfuzz stack hash: `19f6b967ca`
- PC: `0x5b9334297962`
- Fault address: `0x745133e57000`
- Instruction: `mov____0x50(%rax,%r13,8),%r13`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b95ad5268920.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGBUS.PC.5b9334297962.STACK.19f6b967ca.CODE.2.ADDR.745133e57000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGBUS.PC.5b9334297962.STACK.19f6b967ca.CODE.2.ADDR.745133e57000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078b605894180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGBUS.PC.5b9334297962.STACK.19f6b967ca.CODE.2.ADDR.745133e57000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGBUS.PC.5c9dbd984962.STACK.19f6b967ca.CODE.2.ADDR.7a2c887b3000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`

### 102. cpython-314-c02472ad3abb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a0197786`
- Honggfuzz stack hash: `18a0197786`
- PC: `0x565741fb41cd`
- Fault address: `0xa9`
- Instruction: `mov____0xa8(%r14),%rbx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c02472ad3abb.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.565741fb41cd.STACK.18a0197786.CODE.1.ADDR.a9.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.565741fb41cd.STACK.18a0197786.CODE.1.ADDR.a9.INSTR.mov____0xa8(%r14),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073d36a469180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.565741fb41cd.STACK.18a0197786.CODE.1.ADDR.a9.INSTR.mov____0xa8(%r14),%rbx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61113665d241.STACK.18a0197786.CODE.128.ADDR.0.INSTR.mov____0x2c010(%r15,%r12,1),%rax.pyc`

### 103. cpython-314-d26f831ad8d6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cbc1b7f89`
- Honggfuzz stack hash: `cbc1b7f89`
- PC: `0x5e0f65d4d8b4`
- Fault address: `0x1003c`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d26f831ad8d6.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e0f65d4d8b4.STACK.cbc1b7f89.CODE.1.ADDR.1003c.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e0f65d4d8b4.STACK.cbc1b7f89.CODE.1.ADDR.1003c.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007327c3acc180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e0f65d4d8b4.STACK.cbc1b7f89.CODE.1.ADDR.1003c.INSTR.mov____0x8(%r13),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.64f9be5d68b4.STACK.cbc1b7f89.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rax.pyc`

### 104. cpython-314-d4a9146aced1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db6fec82a`
- Honggfuzz stack hash: `db6fec82a`
- PC: `0x56416619ffc2`
- Fault address: `0x20`
- Instruction: `cmp____%rax,0x20(%r15)`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d4a9146aced1.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56416619ffc2.STACK.db6fec82a.CODE.1.ADDR.20.INSTR.cmp____%rax,0x20(%r15).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56416619ffc2.STACK.db6fec82a.CODE.1.ADDR.20.INSTR.cmp____%rax,0x20(%r15).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007739f8735180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56416619ffc2.STACK.db6fec82a.CODE.1.ADDR.20.INSTR.cmp____%rax,0x20(%r15).pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e2a3ceb8f57.STACK.db6fec82a.CODE.1.ADDR.5e2a00000008.INSTR.mov____0x8(%r14),%rax.pyc`

### 105. cpython-314-f540efbe3d55

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:193e3aa15c`
- Honggfuzz stack hash: `193e3aa15c`
- PC: `0x5eabba559f36`
- Fault address: `0x0`
- Instruction: `mov____0x14(%rax,%r15,4),%ebx`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-f540efbe3d55.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5eabba559f36.STACK.193e3aa15c.CODE.128.ADDR.0.INSTR.mov____0x14(%rax,%r15,4),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5eabba559f36.STACK.193e3aa15c.CODE.128.ADDR.0.INSTR.mov____0x14(%rax,%r15,4),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007c8d3b2cc180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5eabba559f36.STACK.193e3aa15c.CODE.128.ADDR.0.INSTR.mov____0x14(%rax,%r15,4),%ebx.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fad8ce4ff36.STACK.193e3aa15c.CODE.128.ADDR.0.INSTR.mov____0x14(%rax,%r15,4),%ebx.pyc`

### 106. cpython-314-fcc743e6df3e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:dec3baf1a`
- Honggfuzz stack hash: `dec3baf1a`
- PC: `0x59f14aa71351`
- Fault address: `0x59f100000008`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 2
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-fcc743e6df3e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59f14aa71351.STACK.dec3baf1a.CODE.1.ADDR.59f100000008.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59f14aa71351.STACK.dec3baf1a.CODE.1.ADDR.59f100000008.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e9e28765180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59f14aa71351.STACK.dec3baf1a.CODE.1.ADDR.59f100000008.INSTR.mov____0x8(%r12),%rax.pyc`
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f5b1d36b351.STACK.dec3baf1a.CODE.1.ADDR.5f5b00000008.INSTR.mov____0x8(%r12),%rax.pyc`

### 107. cpython-314-0299a4ae6301

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e9d3c76ca`
- Honggfuzz stack hash: `e9d3c76ca`
- PC: `0x5d4b8b79e040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0299a4ae6301.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d4b8b79e040.STACK.e9d3c76ca.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d4b8b79e040.STACK.e9d3c76ca.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ac708fe5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d4b8b79e040.STACK.e9d3c76ca.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 108. cpython-314-0b4ba925febf

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d732b17b3`
- Honggfuzz stack hash: `d732b17b3`
- PC: `0x56a0bc24dd9a`
- Fault address: `0x71`
- Instruction: `mov____0x70(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-0b4ba925febf.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a0bc24dd9a.STACK.d732b17b3.CODE.1.ADDR.71.INSTR.mov____0x70(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a0bc24dd9a.STACK.d732b17b3.CODE.1.ADDR.71.INSTR.mov____0x70(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e8a56f8a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56a0bc24dd9a.STACK.d732b17b3.CODE.1.ADDR.71.INSTR.mov____0x70(%r14),%rax.pyc`

### 109. cpython-314-14f485a609ce

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d732a42c7`
- Honggfuzz stack hash: `d732a42c7`
- PC: `0x5cd331a2de61`
- Fault address: `0x5cd300000008`
- Instruction: `mov____0x8(%r15),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-14f485a609ce.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cd331a2de61.STACK.d732a42c7.CODE.1.ADDR.5cd300000008.INSTR.mov____0x8(%r15),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cd331a2de61.STACK.d732a42c7.CODE.1.ADDR.5cd300000008.INSTR.mov____0x8(%r15),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a05d1ca2180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cd331a2de61.STACK.d732a42c7.CODE.1.ADDR.5cd300000008.INSTR.mov____0x8(%r15),%r14.pyc`

### 110. cpython-314-1583be010a5d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d728f7ca3`
- Honggfuzz stack hash: `d728f7ca3`
- PC: `0x5c020fe99a33`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-1583be010a5d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c020fe99a33.STACK.d728f7ca3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c020fe99a33.STACK.d728f7ca3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000719d289aa180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c020fe99a33.STACK.d728f7ca3.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r14.pyc`

### 111. cpython-314-16b9391547df

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f0116c8df`
- Honggfuzz stack hash: `f0116c8df`
- PC: `0x55ea04794040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-16b9391547df.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ea04794040.STACK.f0116c8df.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ea04794040.STACK.f0116c8df.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000072782fc59180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.55ea04794040.STACK.f0116c8df.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 112. cpython-314-17b1fec79ec0

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fe51e6697`
- Honggfuzz stack hash: `fe51e6697`
- PC: `0x629d05074491`
- Fault address: `0x0`
- Instruction: `mov____0x140(%r13),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-17b1fec79ec0.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.629d05074491.STACK.fe51e6697.CODE.128.ADDR.0.INSTR.mov____0x140(%r13),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.629d05074491.STACK.fe51e6697.CODE.128.ADDR.0.INSTR.mov____0x140(%r13),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007ed610ce5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.629d05074491.STACK.fe51e6697.CODE.128.ADDR.0.INSTR.mov____0x140(%r13),%r14.pyc`

### 113. cpython-314-22471a4a805f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b1abf643`
- Honggfuzz stack hash: `18b1abf643`
- PC: `0x587b9cabce1b`
- Fault address: `0x587b00000008`
- Instruction: `mov____0x8(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-22471a4a805f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.587b9cabce1b.STACK.18b1abf643.CODE.1.ADDR.587b00000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.587b9cabce1b.STACK.18b1abf643.CODE.1.ADDR.587b00000008.INSTR.mov____0x8(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007f8fbfa37180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.587b9cabce1b.STACK.18b1abf643.CODE.1.ADDR.587b00000008.INSTR.mov____0x8(%r14),%r15.pyc`

### 114. cpython-314-23dbb2be8740

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d2683f029`
- Honggfuzz stack hash: `d2683f029`
- PC: `0x5bbfc232b51e`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-23dbb2be8740.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bbfc232b51e.STACK.d2683f029.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bbfc232b51e.STACK.d2683f029.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077725a355180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bbfc232b51e.STACK.d2683f029.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r13.pyc`

### 115. cpython-314-291a41234212

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cb58df2ae`
- Honggfuzz stack hash: `cb58df2ae`
- PC: `0x5c54bd91d871`
- Fault address: `0x0`
- Instruction: `call___*%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-291a41234212.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c54bd91d871.STACK.cb58df2ae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c54bd91d871.STACK.cb58df2ae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007086551e4180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c54bd91d871.STACK.cb58df2ae.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`

### 116. cpython-314-2c9b438d5abc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1af2abaf11`
- Honggfuzz stack hash: `1af2abaf11`
- PC: `0x58ab15940085`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2c9b438d5abc.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58ab15940085.STACK.1af2abaf11.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58ab15940085.STACK.1af2abaf11.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e2f5435d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58ab15940085.STACK.1af2abaf11.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%r12.pyc`

### 117. cpython-314-2cebbd95e78e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f9e3d266`
- Honggfuzz stack hash: `19f9e3d266`
- PC: `0x570a7c77051e`
- Fault address: `0x570a00000008`
- Instruction: `mov____0x8(%r15),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-2cebbd95e78e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.570a7c77051e.STACK.19f9e3d266.CODE.1.ADDR.570a00000008.INSTR.mov____0x8(%r15),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.570a7c77051e.STACK.19f9e3d266.CODE.1.ADDR.570a00000008.INSTR.mov____0x8(%r15),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000730907ea1180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.570a7c77051e.STACK.19f9e3d266.CODE.1.ADDR.570a00000008.INSTR.mov____0x8(%r15),%r13.pyc`

### 118. cpython-314-3d7d6b6b6b5c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fa21702d8`
- Honggfuzz stack hash: `fa21702d8`
- PC: `0x5f948d923f24`
- Fault address: `0x81`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-3d7d6b6b6b5c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f948d923f24.STACK.fa21702d8.CODE.1.ADDR.81.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f948d923f24.STACK.fa21702d8.CODE.1.ADDR.81.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074c50b147180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f948d923f24.STACK.fa21702d8.CODE.1.ADDR.81.INSTR.mov____0x8(%r13),%rax.pyc`

### 119. cpython-314-3f2d13ff3fc8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a9844ca8`
- Honggfuzz stack hash: `18a9844ca8`
- PC: `0x5f0e263f4043`
- Fault address: `0x0`
- Instruction: `mov____0x8(%rbx),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-3f2d13ff3fc8.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0e263f4043.STACK.18a9844ca8.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0e263f4043.STACK.18a9844ca8.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000758c52f23180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0e263f4043.STACK.18a9844ca8.CODE.128.ADDR.0.INSTR.mov____0x8(%rbx),%r15.pyc`

### 120. cpython-314-4140051f69a2

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1926f6fd61`
- Honggfuzz stack hash: `1926f6fd61`
- PC: `0x5deea33c736f`
- Fault address: `0x81`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-4140051f69a2.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5deea33c736f.STACK.1926f6fd61.CODE.1.ADDR.81.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5deea33c736f.STACK.1926f6fd61.CODE.1.ADDR.81.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000764aa15e5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5deea33c736f.STACK.1926f6fd61.CODE.1.ADDR.81.INSTR.mov____(%r14),%ebx.pyc`

### 121. cpython-314-42d0f3bd678e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18c8b0b3a6`
- Honggfuzz stack hash: `18c8b0b3a6`
- PC: `0x5bc81d38e70e`
- Fault address: `0x5bc800000008`
- Instruction: `mov____0x8(%rbx),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-42d0f3bd678e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc81d38e70e.STACK.18c8b0b3a6.CODE.1.ADDR.5bc800000008.INSTR.mov____0x8(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc81d38e70e.STACK.18c8b0b3a6.CODE.1.ADDR.5bc800000008.INSTR.mov____0x8(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007acb1022c180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc81d38e70e.STACK.18c8b0b3a6.CODE.1.ADDR.5bc800000008.INSTR.mov____0x8(%rbx),%r13.pyc`

### 122. cpython-314-4d055ea2240e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ee0656d5f`
- Honggfuzz stack hash: `ee0656d5f`
- PC: `0x5aeddfc3b048`
- Fault address: `0xa9`
- Instruction: `mov____0xa8(%rax),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-4d055ea2240e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aeddfc3b048.STACK.ee0656d5f.CODE.1.ADDR.a9.INSTR.mov____0xa8(%rax),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aeddfc3b048.STACK.ee0656d5f.CODE.1.ADDR.a9.INSTR.mov____0xa8(%rax),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077222f2a5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5aeddfc3b048.STACK.ee0656d5f.CODE.1.ADDR.a9.INSTR.mov____0xa8(%rax),%rbx.pyc`

### 123. cpython-314-4d8b873dfcbd

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:cfca3df47`
- Honggfuzz stack hash: `cfca3df47`
- PC: `0x5f0de9db2902`
- Fault address: `0x0`
- Instruction: `mov____(%r15),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-4d8b873dfcbd.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0de9db2902.STACK.cfca3df47.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0de9db2902.STACK.cfca3df47.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007fb876e50180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5f0de9db2902.STACK.cfca3df47.CODE.128.ADDR.0.INSTR.mov____(%r15),%ebx.pyc`

### 124. cpython-314-517baeecc3e7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197f91d28c`
- Honggfuzz stack hash: `197f91d28c`
- PC: `0x5c583d1bf26c`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-517baeecc3e7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c583d1bf26c.STACK.197f91d28c.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c583d1bf26c.STACK.197f91d28c.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077e2db67a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c583d1bf26c.STACK.197f91d28c.CODE.1.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 125. cpython-314-55fa1b03b080

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18278aac71`
- Honggfuzz stack hash: `18278aac71`
- PC: `0x5df224f936f1`
- Fault address: `0x0`
- Instruction: `call___*%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-55fa1b03b080.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df224f936f1.STACK.18278aac71.CODE.128.ADDR.0.INSTR.call___*%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df224f936f1.STACK.18278aac71.CODE.128.ADDR.0.INSTR.call___*%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000791f9e25a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df224f936f1.STACK.18278aac71.CODE.128.ADDR.0.INSTR.call___*%r12.pyc`

### 126. cpython-314-58ff52d0ee1b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a81335b65`
- Honggfuzz stack hash: `1a81335b65`
- PC: `0x6134586a6572`
- Fault address: `0x10008`
- Instruction: `mov____0x8(%r15),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-58ff52d0ee1b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6134586a6572.STACK.1a81335b65.CODE.1.ADDR.10008.INSTR.mov____0x8(%r15),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6134586a6572.STACK.1a81335b65.CODE.1.ADDR.10008.INSTR.mov____0x8(%r15),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007fe4b5755180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6134586a6572.STACK.1a81335b65.CODE.1.ADDR.10008.INSTR.mov____0x8(%r15),%rbx.pyc`

### 127. cpython-314-5fa4225d9e70

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1963f396f6`
- Honggfuzz stack hash: `1963f396f6`
- PC: `0x60c638b0f146`
- Fault address: `0x0`
- Instruction: `mov____0x10(%r14),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-5fa4225d9e70.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60c638b0f146.STACK.1963f396f6.CODE.128.ADDR.0.INSTR.mov____0x10(%r14),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60c638b0f146.STACK.1963f396f6.CODE.128.ADDR.0.INSTR.mov____0x10(%r14),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007aceb338e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60c638b0f146.STACK.1963f396f6.CODE.128.ADDR.0.INSTR.mov____0x10(%r14),%r15.pyc`

### 128. cpython-314-604acccb288f

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18fd0190d9`
- Honggfuzz stack hash: `18fd0190d9`
- PC: `0x61efb1167787`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-604acccb288f.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61efb1167787.STACK.18fd0190d9.CODE.128.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61efb1167787.STACK.18fd0190d9.CODE.128.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078e33578e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61efb1167787.STACK.18fd0190d9.CODE.128.ADDR.0.INSTR.mov____(%r14),%r13d.pyc`

### 129. cpython-314-640b78f7e796

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:df1c1aacc`
- Honggfuzz stack hash: `df1c1aacc`
- PC: `0x60362d529cd2`
- Fault address: `0x0`
- Instruction: `mov____0x70(%r15),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-640b78f7e796.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60362d529cd2.STACK.df1c1aacc.CODE.128.ADDR.0.INSTR.mov____0x70(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60362d529cd2.STACK.df1c1aacc.CODE.128.ADDR.0.INSTR.mov____0x70(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000786e4b8e9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60362d529cd2.STACK.df1c1aacc.CODE.128.ADDR.0.INSTR.mov____0x70(%r15),%rax.pyc`

### 130. cpython-314-6960e4378938

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:e043e6fa4`
- Honggfuzz stack hash: `e043e6fa4`
- PC: `0x5fae985c7e57`
- Fault address: `0x7`
- Instruction: `mov____0x8(%r15),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-6960e4378938.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fae985c7e57.STACK.e043e6fa4.CODE.1.ADDR.7.INSTR.mov____0x8(%r15),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fae985c7e57.STACK.e043e6fa4.CODE.1.ADDR.7.INSTR.mov____0x8(%r15),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078dc7b46f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fae985c7e57.STACK.e043e6fa4.CODE.1.ADDR.7.INSTR.mov____0x8(%r15),%rax.pyc`

### 131. cpython-314-6efc300625b7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1acee58681`
- Honggfuzz stack hash: `1acee58681`
- PC: `0x5e377c38978f`
- Fault address: `0x100000013`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-6efc300625b7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e377c38978f.STACK.1acee58681.CODE.1.ADDR.100000013.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e377c38978f.STACK.1acee58681.CODE.1.ADDR.100000013.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073f505d8f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5e377c38978f.STACK.1acee58681.CODE.1.ADDR.100000013.INSTR.mov____(%r14),%ebx.pyc`

### 132. cpython-314-763c401ee23b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c63b7a722`
- Honggfuzz stack hash: `c63b7a722`
- PC: `0x60a46b92c2b1`
- Fault address: `0x10`
- Instruction: `mov____0x10(%rbx),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-763c401ee23b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60a46b92c2b1.STACK.c63b7a722.CODE.1.ADDR.10.INSTR.mov____0x10(%rbx),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60a46b92c2b1.STACK.c63b7a722.CODE.1.ADDR.10.INSTR.mov____0x10(%rbx),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000767e5c665180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.60a46b92c2b1.STACK.c63b7a722.CODE.1.ADDR.10.INSTR.mov____0x10(%rbx),%r13.pyc`

### 133. cpython-314-77e5b6ba53d3

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d67405a90`
- Honggfuzz stack hash: `d67405a90`
- PC: `0x5915b8ca6c10`
- Fault address: `0x0`
- Instruction: `mov____(%r12),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-77e5b6ba53d3.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5915b8ca6c10.STACK.d67405a90.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5915b8ca6c10.STACK.d67405a90.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bc6497f5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5915b8ca6c10.STACK.d67405a90.CODE.128.ADDR.0.INSTR.mov____(%r12),%ebx.pyc`

### 134. cpython-314-797e2b50d8bc

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:db7d6ed62`
- Honggfuzz stack hash: `db7d6ed62`
- PC: `0x596cd49b5a8f`
- Fault address: `0x0`
- Instruction: `cmpq___$0x0,0x108(%rax)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-797e2b50d8bc.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.596cd49b5a8f.STACK.db7d6ed62.CODE.128.ADDR.0.INSTR.cmpq___$0x0,0x108(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.596cd49b5a8f.STACK.db7d6ed62.CODE.128.ADDR.0.INSTR.cmpq___$0x0,0x108(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000076fa3674b180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.596cd49b5a8f.STACK.db7d6ed62.CODE.128.ADDR.0.INSTR.cmpq___$0x0,0x108(%rax).pyc`

### 135. cpython-314-7a499c9b568a

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c1cb166bb`
- Honggfuzz stack hash: `c1cb166bb`
- PC: `0x57d82c4d9435`
- Fault address: `0x10`
- Instruction: `mov____0x10(%rax),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-7a499c9b568a.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57d82c4d9435.STACK.c1cb166bb.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57d82c4d9435.STACK.c1cb166bb.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e8875b49180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57d82c4d9435.STACK.c1cb166bb.CODE.1.ADDR.10.INSTR.mov____0x10(%rax),%r15.pyc`

### 136. cpython-314-7c743d916eff

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a7ecac47`
- Honggfuzz stack hash: `18a7ecac47`
- PC: `0x5df79cc22351`
- Fault address: `0x5df700000008`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-7c743d916eff.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df79cc22351.STACK.18a7ecac47.CODE.1.ADDR.5df700000008.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df79cc22351.STACK.18a7ecac47.CODE.1.ADDR.5df700000008.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078f5a0be1180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5df79cc22351.STACK.18a7ecac47.CODE.1.ADDR.5df700000008.INSTR.mov____0x8(%r12),%rax.pyc`

### 137. cpython-314-8069e66ba870

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fbcf3e3fd`
- Honggfuzz stack hash: `fbcf3e3fd`
- PC: `0x59cf7bc5fd35`
- Fault address: `0x0`
- Instruction: `movaps_%xmm0,-0x40(%rbp)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8069e66ba870.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59cf7bc5fd35.STACK.fbcf3e3fd.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59cf7bc5fd35.STACK.fbcf3e3fd.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007417bc37a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.59cf7bc5fd35.STACK.fbcf3e3fd.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`

### 138. cpython-314-8309fdc770c7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19651e4f34`
- Honggfuzz stack hash: `19651e4f34`
- PC: `0x5867c104a36f`
- Fault address: `0x51`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8309fdc770c7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5867c104a36f.STACK.19651e4f34.CODE.1.ADDR.51.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5867c104a36f.STACK.19651e4f34.CODE.1.ADDR.51.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e896c1c7180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5867c104a36f.STACK.19651e4f34.CODE.1.ADDR.51.INSTR.mov____(%r14),%ebx.pyc`

### 139. cpython-314-862ecb521c00

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:c31f1419b`
- Honggfuzz stack hash: `c31f1419b`
- PC: `0x7a31a2ff79fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-862ecb521c00.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7a31a2ff79fc.STACK.c31f1419b.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7a31a2ff79fc.STACK.c31f1419b.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e7d68b42180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7a31a2ff79fc.STACK.c31f1419b.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 140. cpython-314-879559ad2377

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b756bf6dc`
- Honggfuzz stack hash: `1b756bf6dc`
- PC: `0x5774feccf548`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%rax),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-879559ad2377.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5774feccf548.STACK.1b756bf6dc.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5774feccf548.STACK.1b756bf6dc.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007752ee174180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5774feccf548.STACK.1b756bf6dc.CODE.128.ADDR.0.INSTR.mov____0xa8(%rax),%r15.pyc`

### 141. cpython-314-8d6bd7b2ea1b

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19f6b967ca`
- Honggfuzz stack hash: `19f6b967ca`
- PC: `0x5d2395804962`
- Fault address: `0x5d23c95d1000`
- Instruction: `mov____0x50(%rax,%r13,8),%r13`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8d6bd7b2ea1b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2395804962.STACK.19f6b967ca.CODE.1.ADDR.5d23c95d1000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2395804962.STACK.19f6b967ca.CODE.1.ADDR.5d23c95d1000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007dba99731180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d2395804962.STACK.19f6b967ca.CODE.1.ADDR.5d23c95d1000.INSTR.mov____0x50(%rax,%r13,8),%r13.pyc`

### 142. cpython-314-8da6df976e77

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:caffa1428`
- Honggfuzz stack hash: `caffa1428`
- PC: `0x5cfe138d1cd9`
- Fault address: `0x60`
- Instruction: `mov____0x60(%rax),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8da6df976e77.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cfe138d1cd9.STACK.caffa1428.CODE.1.ADDR.60.INSTR.mov____0x60(%rax),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cfe138d1cd9.STACK.caffa1428.CODE.1.ADDR.60.INSTR.mov____0x60(%rax),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007873fcf4e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5cfe138d1cd9.STACK.caffa1428.CODE.1.ADDR.60.INSTR.mov____0x60(%rax),%r12.pyc`

### 143. cpython-314-8ff333c68540

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19ac4a6088`
- Honggfuzz stack hash: `19ac4a6088`
- PC: `0x5c1f28acbe61`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r15),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-8ff333c68540.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c1f28acbe61.STACK.19ac4a6088.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c1f28acbe61.STACK.19ac4a6088.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077ed3ad4e180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c1f28acbe61.STACK.19ac4a6088.CODE.1.ADDR.8.INSTR.mov____0x8(%r15),%r14.pyc`

### 144. cpython-314-90adcce54d14

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18a97ba713`
- Honggfuzz stack hash: `18a97ba713`
- PC: `0x6232e931660b`
- Fault address: `0x8`
- Instruction: `mov____0x8(%r12),%rdi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-90adcce54d14.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6232e931660b.STACK.18a97ba713.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6232e931660b.STACK.18a97ba713.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007528c69fc180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6232e931660b.STACK.18a97ba713.CODE.1.ADDR.8.INSTR.mov____0x8(%r12),%rdi.pyc`

### 145. cpython-314-91d259ef184c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19eaa664ea`
- Honggfuzz stack hash: `19eaa664ea`
- PC: `0x5a0e8d3e9ec8`
- Fault address: `0x30`
- Instruction: `mov____0x30(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-91d259ef184c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0e8d3e9ec8.STACK.19eaa664ea.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0e8d3e9ec8.STACK.19eaa664ea.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007fccc5a66180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a0e8d3e9ec8.STACK.19eaa664ea.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`

### 146. cpython-314-96ee8bd54ca7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:187e02ce9a`
- Honggfuzz stack hash: `187e02ce9a`
- PC: `0x63e088381fca`
- Fault address: `0x63e000000008`
- Instruction: `mov____0x8(%r13),%r15`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-96ee8bd54ca7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63e088381fca.STACK.187e02ce9a.CODE.1.ADDR.63e000000008.INSTR.mov____0x8(%r13),%r15.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63e088381fca.STACK.187e02ce9a.CODE.1.ADDR.63e000000008.INSTR.mov____0x8(%r13),%r15.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071fafa014180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.63e088381fca.STACK.187e02ce9a.CODE.1.ADDR.63e000000008.INSTR.mov____0x8(%r13),%r15.pyc`

### 147. cpython-314-96f3468a3b8c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:183c05b1bf`
- Honggfuzz stack hash: `183c05b1bf`
- PC: `0x5dac374ea36f`
- Fault address: `0x0`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-96f3468a3b8c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dac374ea36f.STACK.183c05b1bf.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dac374ea36f.STACK.183c05b1bf.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007399199d6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5dac374ea36f.STACK.183c05b1bf.CODE.128.ADDR.0.INSTR.mov____(%r14),%ebx.pyc`

### 148. cpython-314-99d0f371ddda

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19c3bd0d62`
- Honggfuzz stack hash: `19c3bd0d62`
- PC: `0x6111239596df`
- Fault address: `0xae`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-99d0f371ddda.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6111239596df.STACK.19c3bd0d62.CODE.1.ADDR.ae.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6111239596df.STACK.19c3bd0d62.CODE.1.ADDR.ae.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078c55a9e9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.6111239596df.STACK.19c3bd0d62.CODE.1.ADDR.ae.INSTR.mov____0xa8(%r15),%r12.pyc`

### 149. cpython-314-9dea711312e6

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ce36593f0`
- Honggfuzz stack hash: `ce36593f0`
- PC: `0x5a4729b7c36f`
- Fault address: `0x11`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-9dea711312e6.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a4729b7c36f.STACK.ce36593f0.CODE.1.ADDR.11.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a4729b7c36f.STACK.ce36593f0.CODE.1.ADDR.11.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000075d8350f6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a4729b7c36f.STACK.ce36593f0.CODE.1.ADDR.11.INSTR.mov____(%r14),%ebx.pyc`

### 150. cpython-314-a25f60823a1e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1bc7cdc998`
- Honggfuzz stack hash: `1bc7cdc998`
- PC: `0x56eeca3976df`
- Fault address: `0xa7`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a25f60823a1e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56eeca3976df.STACK.1bc7cdc998.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56eeca3976df.STACK.1bc7cdc998.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d6721292180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.56eeca3976df.STACK.1bc7cdc998.CODE.1.ADDR.a7.INSTR.mov____0xa8(%r15),%r12.pyc`

### 151. cpython-314-a29d47104c0d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1824900665`
- Honggfuzz stack hash: `1824900665`
- PC: `0x5c738209ff57`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a29d47104c0d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c738209ff57.STACK.1824900665.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c738209ff57.STACK.1824900665.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007db14fa4a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c738209ff57.STACK.1824900665.CODE.128.ADDR.0.INSTR.mov____0x8(%r14),%rax.pyc`

### 152. cpython-314-a4df2c1af78c

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1abbfc97f6`
- Honggfuzz stack hash: `1abbfc97f6`
- PC: `0x651d300e3540`
- Fault address: `0x8`
- Instruction: `mov____0x8(%rbx),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a4df2c1af78c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.651d300e3540.STACK.1abbfc97f6.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.651d300e3540.STACK.1abbfc97f6.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000704cd3b58180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.651d300e3540.STACK.1abbfc97f6.CODE.1.ADDR.8.INSTR.mov____0x8(%rbx),%r12.pyc`

### 153. cpython-314-a90b87d3bc73

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19b3a76c03`
- Honggfuzz stack hash: `19b3a76c03`
- PC: `0x785ef201e9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a90b87d3bc73.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.785ef201e9fc.STACK.19b3a76c03.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.785ef201e9fc.STACK.19b3a76c03.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000763fcb2ab180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.785ef201e9fc.STACK.19b3a76c03.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 154. cpython-314-a954e51f564e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b53e06e08`
- Honggfuzz stack hash: `1b53e06e08`
- PC: `0x5942be5e778f`
- Fault address: `0xc`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a954e51f564e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5942be5e778f.STACK.1b53e06e08.CODE.1.ADDR.c.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5942be5e778f.STACK.1b53e06e08.CODE.1.ADDR.c.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e2db70f5180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5942be5e778f.STACK.1b53e06e08.CODE.1.ADDR.c.INSTR.mov____(%r14),%ebx.pyc`

### 155. cpython-314-a98d39eeedf7

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:fd97845a4`
- Honggfuzz stack hash: `fd97845a4`
- PC: `0x5bfcb7221d35`
- Fault address: `0x0`
- Instruction: `movaps_%xmm0,-0x40(%rbp)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-a98d39eeedf7.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bfcb7221d35.STACK.fd97845a4.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bfcb7221d35.STACK.fd97845a4.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000077abe1f15180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bfcb7221d35.STACK.fd97845a4.CODE.128.ADDR.0.INSTR.movaps_%xmm0,-0x40(%rbp).pyc`

### 156. cpython-314-afab230f5062

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18bff2250a`
- Honggfuzz stack hash: `18bff2250a`
- PC: `0x61f74b1516df`
- Fault address: `0x0`
- Instruction: `mov____0xa8(%r15),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-afab230f5062.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61f74b1516df.STACK.18bff2250a.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61f74b1516df.STACK.18bff2250a.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073a87a803180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.61f74b1516df.STACK.18bff2250a.CODE.128.ADDR.0.INSTR.mov____0xa8(%r15),%r12.pyc`

### 157. cpython-314-b66161d39d74

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:deaba9cb7`
- Honggfuzz stack hash: `deaba9cb7`
- PC: `0x5932a2dfeec8`
- Fault address: `0x30`
- Instruction: `mov____0x30(%rbx),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b66161d39d74.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5932a2dfeec8.STACK.deaba9cb7.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5932a2dfeec8.STACK.deaba9cb7.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000723c84c0d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5932a2dfeec8.STACK.deaba9cb7.CODE.1.ADDR.30.INSTR.mov____0x30(%rbx),%rax.pyc`

### 158. cpython-314-b7c89ad6c93d

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de1fe7f16`
- Honggfuzz stack hash: `de1fe7f16`
- PC: `0x57e70c7e3a59`
- Fault address: `0x49`
- Instruction: `mov____0x8(%r14),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b7c89ad6c93d.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57e70c7e3a59.STACK.de1fe7f16.CODE.1.ADDR.49.INSTR.mov____0x8(%r14),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57e70c7e3a59.STACK.de1fe7f16.CODE.1.ADDR.49.INSTR.mov____0x8(%r14),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e39a92b6180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.57e70c7e3a59.STACK.de1fe7f16.CODE.1.ADDR.49.INSTR.mov____0x8(%r14),%rax.pyc`

### 159. cpython-314-b95f2c219a9c

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:18bc176076`
- Honggfuzz stack hash: `18bc176076`
- PC: `0x7045fc9499fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-b95f2c219a9c.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7045fc9499fc.STACK.18bc176076.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7045fc9499fc.STACK.18bc176076.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000764bb7c46180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7045fc9499fc.STACK.18bc176076.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 160. cpython-314-bff3439f1e0e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d600719f2`
- Honggfuzz stack hash: `d600719f2`
- PC: `0x581da4975fb0`
- Fault address: `0x0`
- Instruction: `mov____0x100(%rbx),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-bff3439f1e0e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.581da4975fb0.STACK.d600719f2.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.581da4975fb0.STACK.d600719f2.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007fbc73011180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.581da4975fb0.STACK.d600719f2.CODE.128.ADDR.0.INSTR.mov____0x100(%rbx),%rbx.pyc`

### 161. cpython-314-c0bf69ee7066

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de1ee7e05`
- Honggfuzz stack hash: `de1ee7e05`
- PC: `0x58b06bb27843`
- Fault address: `0x652`
- Instruction: `mov____(%r14),%r15d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c0bf69ee7066.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58b06bb27843.STACK.de1ee7e05.CODE.1.ADDR.652.INSTR.mov____(%r14),%r15d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58b06bb27843.STACK.de1ee7e05.CODE.1.ADDR.652.INSTR.mov____(%r14),%r15d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000726c6b455180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58b06bb27843.STACK.de1ee7e05.CODE.1.ADDR.652.INSTR.mov____(%r14),%r15d.pyc`

### 162. cpython-314-c13d00afb834

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:e448dac14`
- Honggfuzz stack hash: `e448dac14`
- PC: `0x73d8fd6199fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c13d00afb834.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.73d8fd6199fc.STACK.e448dac14.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.73d8fd6199fc.STACK.e448dac14.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007af045c3a180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.73d8fd6199fc.STACK.e448dac14.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 163. cpython-314-c4f171621deb

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b4440b5e1`
- Honggfuzz stack hash: `1b4440b5e1`
- PC: `0x58d1f9a30f3d`
- Fault address: `0x0`
- Instruction: `mov____%rbx,(%rax)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-c4f171621deb.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58d1f9a30f3d.STACK.1b4440b5e1.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58d1f9a30f3d.STACK.1b4440b5e1.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d798fb90180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.58d1f9a30f3d.STACK.1b4440b5e1.CODE.128.ADDR.0.INSTR.mov____%rbx,(%rax).pyc`

### 164. cpython-314-cd349d875815

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:19b82078df`
- Honggfuzz stack hash: `19b82078df`
- PC: `0x5d9905cc5c49`
- Fault address: `0x5d9900000000`
- Instruction: `mov____(%r14),%ebx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cd349d875815.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d9905cc5c49.STACK.19b82078df.CODE.1.ADDR.5d9900000000.INSTR.mov____(%r14),%ebx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d9905cc5c49.STACK.19b82078df.CODE.1.ADDR.5d9900000000.INSTR.mov____(%r14),%ebx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000727d9ea45180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5d9905cc5c49.STACK.19b82078df.CODE.1.ADDR.5d9900000000.INSTR.mov____(%r14),%ebx.pyc`

### 165. cpython-314-cebfa16a5d57

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:18b9a043e1`
- Honggfuzz stack hash: `18b9a043e1`
- PC: `0x621d0173cca2`
- Fault address: `0x0`
- Instruction: `call___*%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cebfa16a5d57.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.621d0173cca2.STACK.18b9a043e1.CODE.128.ADDR.0.INSTR.call___*%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.621d0173cca2.STACK.18b9a043e1.CODE.128.ADDR.0.INSTR.call___*%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007961630bb180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.621d0173cca2.STACK.18b9a043e1.CODE.128.ADDR.0.INSTR.call___*%r14.pyc`

### 166. cpython-314-cf39bebfd575

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a11f9ac25`
- Honggfuzz stack hash: `1a11f9ac25`
- PC: `0x7bcf6480e795`
- Fault address: `0xfffffffffffffff7`
- Instruction: `mov____-0x8(%rbp),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cf39bebfd575.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7bcf6480e795.STACK.1a11f9ac25.CODE.1.ADDR.fffffffffffffff7.INSTR.mov____-0x8(%rbp),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7bcf6480e795.STACK.1a11f9ac25.CODE.1.ADDR.fffffffffffffff7.INSTR.mov____-0x8(%rbp),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a9ecd7ef180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7bcf6480e795.STACK.1a11f9ac25.CODE.1.ADDR.fffffffffffffff7.INSTR.mov____-0x8(%rbp),%rax.pyc`

### 167. cpython-314-cf9eb79b3306

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:ca56aa2a7`
- Honggfuzz stack hash: `ca56aa2a7`
- PC: `0x5fb9506d32b8`
- Fault address: `0xa`
- Instruction: `movzbl_0xa(%r15),%r12d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-cf9eb79b3306.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb9506d32b8.STACK.ca56aa2a7.CODE.1.ADDR.a.INSTR.movzbl_0xa(%r15),%r12d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb9506d32b8.STACK.ca56aa2a7.CODE.1.ADDR.a.INSTR.movzbl_0xa(%r15),%r12d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007e2d1ee90180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fb9506d32b8.STACK.ca56aa2a7.CODE.1.ADDR.a.INSTR.movzbl_0xa(%r15),%r12d.pyc`

### 168. cpython-314-d0eb014d7819

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f5465f589`
- Honggfuzz stack hash: `f5465f589`
- PC: `0x626c29222040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d0eb014d7819.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.626c29222040.STACK.f5465f589.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.626c29222040.STACK.f5465f589.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007b15743cd180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.626c29222040.STACK.f5465f589.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 169. cpython-314-d27e3820a94b

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:c313ca348`
- Honggfuzz stack hash: `c313ca348`
- PC: `0x7c8eb33e49fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-d27e3820a94b.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7c8eb33e49fc.STACK.c313ca348.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7c8eb33e49fc.STACK.c313ca348.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073fc09237180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7c8eb33e49fc.STACK.c313ca348.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 170. cpython-314-df0f86991cb5

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d2863d22f`
- Honggfuzz stack hash: `d2863d22f`
- PC: `0x7b869681847c`
- Fault address: `0x0`
- Instruction: `call___*(%rax)`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-df0f86991cb5.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7b869681847c.STACK.d2863d22f.CODE.128.ADDR.0.INSTR.call___*(%rax).pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7b869681847c.STACK.d2863d22f.CODE.128.ADDR.0.INSTR.call___*(%rax).pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073abfd0a3180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.7b869681847c.STACK.d2863d22f.CODE.128.ADDR.0.INSTR.call___*(%rax).pyc`

### 171. cpython-314-df532cb10fc9

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1b846ddcaf`
- Honggfuzz stack hash: `1b846ddcaf`
- PC: `0x5bc17368b040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-df532cb10fc9.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc17368b040.STACK.1b846ddcaf.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc17368b040.STACK.1b846ddcaf.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007a2e12c49180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bc17368b040.STACK.1b846ddcaf.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 172. cpython-314-e00529dd6c74

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:eee366619`
- Honggfuzz stack hash: `eee366619`
- PC: `0x5fc762175727`
- Fault address: `0x0`
- Instruction: `call___*%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e00529dd6c74.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fc762175727.STACK.eee366619.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fc762175727.STACK.eee366619.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000071af63cf4180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5fc762175727.STACK.eee366619.CODE.128.ADDR.0.INSTR.call___*%rbx.pyc`

### 173. cpython-314-e416f1b1a257

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:197f26da72`
- Honggfuzz stack hash: `197f26da72`
- PC: `0x5ea8c73b5da3`
- Fault address: `0x0`
- Instruction: `mov____0x10(%rax),%r12`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e416f1b1a257.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ea8c73b5da3.STACK.197f26da72.CODE.128.ADDR.0.INSTR.mov____0x10(%rax),%r12.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ea8c73b5da3.STACK.197f26da72.CODE.128.ADDR.0.INSTR.mov____0x10(%rax),%r12.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000075399ec8f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5ea8c73b5da3.STACK.197f26da72.CODE.128.ADDR.0.INSTR.mov____0x10(%rax),%r12.pyc`

### 174. cpython-314-e50d4dcb0b28

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:c23796ede`
- Honggfuzz stack hash: `c23796ede`
- PC: `0x76bc692fc900`
- Fault address: `0x0`
- Instruction: `mov____-0x8(%rsi,%rdx,1),%rcx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e50d4dcb0b28.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.76bc692fc900.STACK.c23796ede.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.76bc692fc900.STACK.c23796ede.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000078385296f180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.76bc692fc900.STACK.c23796ede.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`

### 175. cpython-314-e5f4fd12aa75

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1a5667f536`
- Honggfuzz stack hash: `1a5667f536`
- PC: `0x5bf7fce79120`
- Fault address: `0x0`
- Instruction: `mov____0x8(%r13),%rbx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e5f4fd12aa75.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf7fce79120.STACK.1a5667f536.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf7fce79120.STACK.1a5667f536.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007d4a20a4d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5bf7fce79120.STACK.1a5667f536.CODE.128.ADDR.0.INSTR.mov____0x8(%r13),%rbx.pyc`

### 176. cpython-314-e80f347a4079

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:1935db5aa8`
- Honggfuzz stack hash: `1935db5aa8`
- PC: `0x645ef9fab356`
- Fault address: `0xa8`
- Instruction: `mov____0xa8(%rax),%rsi`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-e80f347a4079.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.645ef9fab356.STACK.1935db5aa8.CODE.1.ADDR.a8.INSTR.mov____0xa8(%rax),%rsi.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.645ef9fab356.STACK.1935db5aa8.CODE.1.ADDR.a8.INSTR.mov____0xa8(%rax),%rsi.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000074c3c9833180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.645ef9fab356.STACK.1935db5aa8.CODE.1.ADDR.a8.INSTR.mov____0xa8(%rax),%rsi.pyc`

### 177. cpython-314-ee998c2344c8

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:de15a8313`
- Honggfuzz stack hash: `de15a8313`
- PC: `0x5c010a9cde56`
- Fault address: `0xf2`
- Instruction: `mov____0x8(%r12),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-ee998c2344c8.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c010a9cde56.STACK.de15a8313.CODE.1.ADDR.f2.INSTR.mov____0x8(%r12),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c010a9cde56.STACK.de15a8313.CODE.1.ADDR.f2.INSTR.mov____0x8(%r12),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007bc835355180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5c010a9cde56.STACK.de15a8313.CODE.1.ADDR.f2.INSTR.mov____0x8(%r12),%rax.pyc`

### 178. cpython-314-f1d7079d88b1

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:f0886933f`
- Honggfuzz stack hash: `f0886933f`
- PC: `0x5efe5fe03040`
- Fault address: `0x18`
- Instruction: `mov____0x18(%rbx),%r14`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-f1d7079d88b1.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5efe5fe03040.STACK.f0886933f.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5efe5fe03040.STACK.f0886933f.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007f6410be0180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5efe5fe03040.STACK.f0886933f.CODE.1.ADDR.18.INSTR.mov____0x18(%rbx),%r14.pyc`

### 179. cpython-314-f43403f36d44

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:19f4b372cd`
- Honggfuzz stack hash: `19f4b372cd`
- PC: `0x7ef4ec5959fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-f43403f36d44.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7ef4ec5959fc.STACK.19f4b372cd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7ef4ec5959fc.STACK.19f4b372cd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x00007f62904ea180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.7ef4ec5959fc.STACK.19f4b372cd.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`

### 180. cpython-314-f785a84eb78e

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:d702e63f8`
- Honggfuzz stack hash: `d702e63f8`
- PC: `0x5a61ac6f071c`
- Fault address: `0x88`
- Instruction: `mov____0x8(%r13),%rax`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-f785a84eb78e.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a61ac6f071c.STACK.d702e63f8.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a61ac6f071c.STACK.d702e63f8.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x000073439dc3d180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.5a61ac6f071c.STACK.d702e63f8.CODE.1.ADDR.88.INSTR.mov____0x8(%r13),%rax.pyc`

### 181. cpython-314-fad26aecaf20

- Status: crash
- Signal: SIGSEGV
- Stack source: honggfuzz-filename
- Stack signature: `SIGSEGV:196b4d8fa0`
- Honggfuzz stack hash: `196b4d8fa0`
- PC: `0x775635428900`
- Fault address: `0x0`
- Instruction: `mov____-0x8(%rsi,%rdx,1),%rcx`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-fad26aecaf20.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.775635428900.STACK.196b4d8fa0.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.775635428900.STACK.196b4d8fa0.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000788b2d6c9180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGSEGV.PC.775635428900.STACK.196b4d8fa0.CODE.128.ADDR.0.INSTR.mov____-0x8(%rsi,%rdx,1),%rcx.pyc`

### 182. cpython-314-fb0d7ef5c673

- Status: crash
- Signal: SIGABRT
- Stack source: honggfuzz-filename
- Stack signature: `SIGABRT:c720497b9`
- Honggfuzz stack hash: `c720497b9`
- PC: `0x79b5720ac9fc`
- Fault address: `0x0`
- Instruction: `mov____%eax,%r13d`
- Findings: 1
- Representative pyc: `data/rq3/cpython-3.14/unique_bug_pyc/cpython-314-fb0d7ef5c673.pyc`
- Representative original: `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.79b5720ac9fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Reproduced stack frames: `not available; rerun did not produce a native backtrace`
- Manual gdb command: `PYTHONHOME=data/rq3/cpython-3.14/source/cpython-* PYTHONPATH=data/rq3/cpython-3.14/source/cpython-*/Lib gdb -q --args data/rq3/cpython-3.14/instrumented/python data/rq3/harness.py data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.79b5720ac9fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
- Rerun diagnostic excerpt:
  - `Fatal Python error: init_import_site: Failed to import the site module`
  - `Python runtime state: initialized`
  - `File "/root/PyBC-Sec/pybcSEC/data/rq3/cpython-3.14/source/cpython-3.14.5/Lib/site.py", line 582`
  - `except FileNotFoundError, PermissionError:`
  - `^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^`
  - `SyntaxError: multiple exception types must be parenthesized`
  - `Current thread 0x0000763cd1cee180 (most recent call first):`
  - `<no Python frame>`
- Example finding inputs:
  - `data/rq3/cpython-3.14/fuzz/crashes/SIGABRT.PC.79b5720ac9fc.STACK.c720497b9.CODE.-6.ADDR.0.INSTR.mov____%eax,%r13d.pyc`
