# cat

### Usage
Read/Write with text files.

### Options
```
cat [filename]
cat [option] [filename] [EOF]
```

- `-l`: Write file in one line.
- `-r`: Read file.
- `-w`: Write into file.
- `-a`: Append into file.
- `-c`: Create file.

### Examples
- **Example 1**: Text file here with `readme.txt` name:
```
Welcome to Pyabr
```
- **Example 2**: Read it
```
cat readme.txt
```
- output:
```
Welcome to Pyabr
```

- **Example 3**: Create it
```
cat -c readme.txt
```
- output:
```
```

- **Example 4**: Write into it with one line
```
cat -l readme.txt Hi
```
- output:
```
Hi
```

- **Example 5**: Write into it
```
cat -r readme.txt EOF
> Hi
> Welcome
> Goodbye
> EOF
```
- output:
```
Hi
Welcome
Goodbye
```

- **Example 6**: Append into it
```
cat -a readme.txt EOF
> Hi again
> EOF
```
- output:
```
Hi
Welcome
Goodbye
Hi again
```