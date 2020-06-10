```bash
# Create project (This creates a whole folder)
poetry new kd_slug
# Or you could just create the toml file instead with `poetry init`

cd kd_slug
python3 -m venv env && . env/bin/activate

# Add dependencies
poetry add sphinx
poetry add git+https://github.com/crossnox/m2r@dev

# Create Sphinx project
mkdir docs/
cd docs/
sphinx-quickstart
  # Separate source and build directories (y/n) [n]: no
  # Project name: kd_slug
  # Author name(s): deepio
  # Project release []: 0.0.1
  # Project language [en]: en

# Edit docs/conf.py to add mr2 and docstring extensions
# extensions = ['m2r', 'sphinx.ext.autodoc']
# autosectionlabel_prefix_document = True
# source_suffix = ['.rst', '.md']

# Change index.rst to index.md and now you have a super markdown file.

# Add `.. mdinclude:: ../README.md` to the top of index.md

# Install your new custom library so it's accessible in python (e.g., from kd_slug import app)
poetry install
```

This way you can create a markdown file with `.. automodule::` to automatically grab your docstrings to document your code. Then add the `.readthedocs.yml` and add the build to your Read The Docs account.

Once everything is set and done, just update your docstrings whenever you change your code, and your documentation will reflect the changes.