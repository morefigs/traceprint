# Check version in setup.cfg first

pipenv install --dev --skip-lock
pipenv run python -m build
pipenv run python -m twine upload dist/*
