```bash
# Create project
poetry new kd_slug
cd kd_slug
python3 -m venv env && . env/bin/activate

# Add dependencies
poetry add sphinx m2r

# Create Sphinx project
sphinx-quickstart
Separate source and build directories (y/n) [n]: yes
Project name: kd_slug
Author name(s): deepio
Project release []: 0.0.1
Project language [en]: en
```
