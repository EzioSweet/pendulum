pipenv create from pipfile
cd src
f2py -c pendulum.f90 -m pendulum --compiler=mingw32
cd ..
pipenv run python src\pendulumUi.py