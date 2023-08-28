# LXM3-Deploy

Simple LXM3-based workflow to deploy HPC jobs

## Project Structure

## Project Structure

`lxm3-deploy` assumes the following structure. 

```bash
<PYTHON_PACKAGE>
├── <PACKAGE_NAME>
│   └── __init.py__
│   └── main.py
├── requirements 
│   └── base.txt
├── pyproject.toml
├── cluster # We will write the .sif file here
```