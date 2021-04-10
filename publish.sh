# Check version in setup.cfg first

rm -rf build
rm -rf dist
rm -rf printstack.egg-info

pipenv install --dev --skip-lock
pipenv run python -m build
pipenv run python -m twine upload dist/*
