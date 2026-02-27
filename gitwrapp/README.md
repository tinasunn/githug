#Gitwrap 

A lighweight Python CLI tool that wraps Git commands with additional functionality like dry-run simulations, safer cleaning and structured output.

---
## Installation

Unzip gitwrap and from root run: 
```
pip install .
```

Verify installation:
```
gitwrap --help
```

#Usage

Prompt before deleting untracked files:
```
gitwrap clean
```

Skip confirmation with --yes:
```
gitwrap clean --yes
```

Dry run to preview what would be deleted:
```
gitwrap --dry-run clean 
```

Status: 
```
gitwrap status
```
With dry run:

```
gitwrap --dry-run status
```
