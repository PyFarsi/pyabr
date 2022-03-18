# cc

### Usage
Compile collection
- Compile Python codes as bytecodes
- Compile C/C++ codes as Linux executable
- Compile Hascal codes as Linux executable

### Options
```
cc [src]
cc [src] [dest]
```

### Examples
- **Example 1**: Compile `foo.py` file:
```
cc foo.py
```
- **Example 2**: Compile `foo.py` as `bar.pyc`:
```
cc foo.py bar.pyc
```
- **Example 3**: Compile `foo.c`:
```
cc foo.c
```
- **Example 4**: Compile `foo.c` as `bar`:
```
cc foo.c bar
```
- **Example 5**: Compile `foo.cpp`:
```
cc foo.cpp
```
- **Example 6**: Compile `foo.cpp` as `bar`:
```
cc foo.cpp bar
```
- **Example 8**: Compile `foo.has`:
```
cc foo.has
```
- **Example 8**: Compile `foo.has` as `bar`:
```
cc foo.has bar
```