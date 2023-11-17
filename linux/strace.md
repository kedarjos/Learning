# strace

- Used to trace system calls and signals of a process.
- Can attach to a running process.
- Records signals received by a process and also records signals called by a process
- Name of the syscall, its return value etc. are printed on standard error or file pointed by -o
- It is a very useful diganostic, instructional and debugging tool.
- A great deal can be learned about a system and its system calls by tracing even ordinary programs.

## The perfect strace commands:

````
strace -f -s 512 -o /tmp/straceout -v -tt -T -C -yy -q <command>
strace -f -s 512 -o /tmp/straceout -v -tt -T -C -yy -q -p <pid>
````

    -f => follow children
    -s => strsize (increase default size)
    -o => output file
    -t / -tt / -ttt => Prefix each line with time
    -T => show time spent inside systemcall
    -y => print file descriptor associated
    -v => verbose mode
    -C => Using "-c" shows summary only, use -C for summary plus regular output

## Some important system calls:

- fork:
    - Creates a new process by duplicating calling process
    - Parent will get the PID of the child
    - Child process gets a 0 as the return value

- clone:
    - Creates a new thread
    - Much more flexible
    - Can be used as fork with some changes input parameters

- wait:
    - Wait for state changes in a child of the calling processes and obtain info when the child has state change
    - Child process with send a SIGCHLD to parent when done
    - Without wait, the child will become a zombie process
    - After wait, the parent will clean the corresponding process table entry

- execve:
    - Executes a program pointed by filename
    - Executes in a new memory space


## More notes:
- File descriptor 1 is for stdout. For example: `write(1, "test test test\n", 15)        = 15`
- For -y, the numbers for file descriptor will be replaced with actual name
  For example: `close(3)` will change to `close(3</tmp/testfile>)`
- `pstree` is another useful command to get idea about all the process tree and children of a process
