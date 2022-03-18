# chmod

### Usage
Change directory/file permission.

### Options

> digit-1: used for owner

> digit-2: used for other users

> digit-3: used for guest user 

> permission number starts with 000 and ends with 777 (x > 8)

- `0`:                    Permission denied
- `1`:                    Execute only
- `2`:                    Write only
- `3`:                    Write and Execute
- `4`:                    Read only
- `5`:                    Read and Execute
- `6`:                    Read and Write
- `7`:                    Have all permissions

### Examples

- **Example 1**: Change permission to read only for others/guest users:
```
chmod 744 /foo.bar
```

- **Example 2**: Access for all users with all no condition:
```
chmod 777 /foo.bar
```

- **Example 3**: Remove all access for guest users:
```
chmod 770 /foo.bar
```

- **Example 4**: Remove all access:
```
chmod 000 /foo.bar
```