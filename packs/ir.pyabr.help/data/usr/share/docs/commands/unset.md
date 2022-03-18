# unset

### Usage
Unset variables.

### Options
```
unset [variable] ...
```

### Example

- **Example 1**:
```
unset foo
```

- **Example 2**:
```
set a: 1
set b: 2
echo A is :a
unset a
echo B is :b
```
- output:
```
A is :a
B is 2
```