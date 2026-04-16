# Environment Configuration Files

This folder contains environment-specific variables used during test execution.

## Overview

You can create multiple `.env` files for different environments. Examples:
- `dev.env`
- `test.env`
- `prod.env`
- `lab1.env`
- `ROLAB.env`
- `PTLAB1.env`
- etc.

## Usage

### Defining Variables

- Define variables in `KEY=VALUE` format
- Variables defined here will be available during test runs as environment variables
- Lines starting with `#` are comments and will be ignored
- Empty lines are ignored

### Examples

```
BASE_URL=https://example.com
DEVICE_ID=PT00001GSC01
```

## Setting Environment for Test Runs

The environment that a test-run will run under can be set from:

- **AquaLab GUI** - Environment popup (for TestRuns)
- **AquaCLI** - `aqua run -e test` (for DevRuns)

## Accessing Variables in Python

In the `environment.py` or in any other `*.py` file, these variables can be accessed in two ways:

1. **Classic Python environment variable access:**
   ```python
   os.getenv("BASE_URL")
   os.getenv("BASE_URL", "http://example.com")
   ```

2. **AquaLab context object (recommended):**
   ```python
   context.env.get("BASE_URL")
   context.env.get("BASE_URL", "http://example.com")
   ```
   
   AquaLab automatically extracts these environment variables and makes them available in the `context.env` object.

## Editing Environment Files

These env files can be created/edited from both:
- **Filesystem** - directly editing the `.env` files in this folder
- **AquaLab GUI** - using the Environment Variables Editor
