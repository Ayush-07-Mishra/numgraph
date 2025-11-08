# Publishing numgraph to PyPI

This guide will help you publish numgraph to the Python Package Index (PyPI) so others can install it with `pip install numgraph`.

## Prerequisites

1. **Create PyPI Account**
   - Sign up at https://pypi.org/account/register/
   - Verify your email

2. **Create API Token**
   - Go to https://pypi.org/manage/account/token/
   - Create a new API token
   - Save it securely (you'll only see it once!)

3. **Install Build Tools**
   ```bash
   pip install build twine
   ```

## Publishing Steps

### 1. Update Version Number

Edit `setup.py` and `pyproject.toml` to increment the version:
```python
version="0.1.0"  # Change to your new version
```

### 2. Update CHANGELOG.md

Document what changed in this version.

### 3. Build the Distribution

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build the package
python -m build
```

This creates two files in `dist/`:
- `numgraph-0.1.0.tar.gz` (source distribution)
- `numgraph-0.1.0-py3-none-any.whl` (wheel distribution)

### 4. Test Upload to TestPyPI (Recommended)

First test on TestPyPI:

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Test installation
pip install --index-url https://test.pypi.org/simple/ numgraph
```

### 5. Upload to PyPI

Once tested, upload to the real PyPI:

```bash
python -m twine upload dist/*
```

Enter your PyPI username (`__token__`) and your API token as the password.

### 6. Verify Installation

```bash
pip install numgraph
```

## Using GitHub Actions (Automated)

The project includes GitHub Actions workflows:

1. **Set up PyPI token in GitHub:**
   - Go to your GitHub repository
   - Settings → Secrets and variables → Actions
   - Add new secret: `PYPI_API_TOKEN`

2. **Create a release:**
   - Go to Releases → Create a new release
   - Create a new tag (e.g., `v0.1.0`)
   - Publish release

GitHub Actions will automatically build and publish to PyPI!

## Version Numbering

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR** version (1.0.0): Breaking changes
- **MINOR** version (0.1.0): New features, backward compatible
- **PATCH** version (0.0.1): Bug fixes

## Checklist Before Publishing

- [ ] All tests pass: `pytest tests/ -v`
- [ ] Version number updated
- [ ] CHANGELOG.md updated
- [ ] README.md accurate
- [ ] `.gitignore` configured
- [ ] Built and tested locally
- [ ] Tested on TestPyPI

## After Publishing

1. **Create a Git tag:**
   ```bash
   git tag -a v0.1.0 -m "Release version 0.1.0"
   git push origin v0.1.0
   ```

2. **Create GitHub release** with changelog

3. **Announce on social media/forums**

## Troubleshooting

**"File already exists"**
- You can't upload the same version twice
- Increment version number and rebuild

**"Invalid credentials"**
- Make sure username is `__token__`
- Check your API token is correct

**Import errors after installation**
- Check `MANIFEST.in` includes all necessary files
- Rebuild and re-upload

## Resources

- PyPI: https://pypi.org
- TestPyPI: https://test.pypi.org
- Packaging Guide: https://packaging.python.org
- Twine Docs: https://twine.readthedocs.io
