@echo off
setlocal

REM Set the number of times to run the program
set iterations=800

REM Replace "python_program.py" with the name of your Python program
REM Replace "python.exe" with the path to your Python interpreter if necessary
for /l %%i in (1,1,%iterations%) do (
    python src/flappy.py --train noui --episode 10
)

endlocal