# say

### Usage
Print text on screen console with creating a new line.

### Options
```
say [text] ...
```

- `-a`: \a
- `-b`: \b
- `-f`: \f
- `-n`: \n
- `-r`: \r
- `-t`: \t
- `-v`: \v

### Examples

- **Example 1**:
```
say foo
say bar
```
- output:
```
foobar
```
- **Example 2**:
```
say What is your name?
read name
echo Welcome, :name in this program.
```
- output:
```
What is your name? Foo
Welcome, Foo in this program.
```