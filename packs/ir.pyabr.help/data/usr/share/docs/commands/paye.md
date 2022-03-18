# paye

### Usage
Pyabr default Package Manager.

### Options
- Clean the package manager cache:
```
sudo paye cl
```

- Build a project as a package with `.pa` format:
```
sudo paye pak [project-directory]
```

- Install packages from `.pa` file:
```
sudo paye upak [package-name].pa
```

- Install/Upgrade packages from repo:
```
sudo paye in [package]
```

- Uninstall packages:
```
sudo paye rm [package]
```

- Download package without installing:
```
sudo paye get [package]
```

- Show informations of packages:
```
sudo paye info [package]
```

- Show list of packages:
```
sudo paye ls
```

- Add a repo:
```
sudo paye add [repo]
```

- Remove a repo:
```
sudo paye del [repo]
```

- Create a project:
```
sudo paye crt [project-type] [project-name]
```

#### Project Types
- C Console Project:
```
sudo paye crt c-console [project-name]
```

- C++ Console Project:
```
sudo paye crt cpp-console [project-name]
```

- Hascal Console Project:
```
sudo paye crt hascal-console [project-name]
```

- Pashmak Console Project:
```
sudo paye crt pashmak-console [project-name]
```

- Python Console Project:
```
sudo paye crt python-console [project-name]
```

- Python Qt Project:
```
sudo paye crt python-qt [project-name]
```

- Python Qt+QML Project:
```
sudo paye crt python-quick [project-name]
```
- Python WebApplication Project:
```
sudo paye crt python-webapp [project-name]
```
- Saye Console Project:
```
sudo paye crt saye-console [project-name]
```