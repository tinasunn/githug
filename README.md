#Gitwrap

Gitwrap is a lighweight Python CLI tool I built that wraps Git commands with additional functionality tool to make Git workflows safer and more user-friendly. I noticed a common pain point: developers risk accidentally deleting files or spending time on repetitive Git commands. GitWrap wraps commands like ```git clean``` & ```git status``` with safety prompts, YAML-formatted outputs, and  ```--dry-run```  previews, allowing users to see exactly what actions will be taken before executing them. This project was a fun opportunity to combine my technical skills with product thinking: identifying a pain point, designing a solution, testing it, and refining it based on user experience from friends and family to ultimately solve a real user problem and improve workflow efficiency.


Installation
Unzip gitwrap and from root run:

pip install .
Verify installation:

gitwrap --help
#Usage

Prompt before deleting untracked files:

gitwrap clean
Skip confirmation with --yes:

gitwrap clean --yes
Dry run to preview what would be deleted:

gitwrap --dry-run clean 
Status:

gitwrap status
With dry run:

gitwrap --dry-run status
