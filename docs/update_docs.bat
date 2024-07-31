echo Working on it...
cd "E:/Coding/Wordle"
sphinx-apidoc -o ./docs src
sphinx-build -b html docs/ docs/_build
echo DONE!
pause