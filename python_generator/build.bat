@echo off
REM Build and compile script for LoliCode Generator (Windows)

echo ================================================================
echo   LoliCode Generator - Build ^& Compile Script
echo ================================================================
echo.

REM Get the directory of this script
cd /d %~dp0

echo Working directory: %CD%
echo.

REM Clean previous builds
echo Cleaning previous builds...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.egg-info rmdir /s /q *.egg-info
for /r %%i in (__pycache__) do @if exist "%%i" rmdir /s /q "%%i"
for /r %%i in (*.pyc) do @if exist "%%i" del /q "%%i"
for /r %%i in (*.pyo) do @if exist "%%i" del /q "%%i"
echo    Done
echo.

REM Compile Python files (syntax check)
echo Compiling Python files...
python -m py_compile gui_app.py
python -m py_compile src/generator/__init__.py
python -m py_compile src/generator/lolicode_generator.py
python -m py_compile src/generator/types.py
python -m py_compile src/generator/builders/__init__.py
python -m py_compile src/generator/validators/__init__.py
if errorlevel 1 (
    echo    Failed to compile Python files!
    pause
    exit /b 1
)
echo    All Python files compiled successfully
echo.

REM Run tests
echo Running tests...
python -m pytest tests/ -v --tb=short
if errorlevel 1 (
    echo    Tests failed!
    pause
    exit /b 1
)
echo    All tests passed
echo.

REM Build source distribution
echo Building source distribution...
python setup.py sdist
if errorlevel 1 (
    echo    Failed to build source distribution!
    pause
    exit /b 1
)
echo    Source distribution created
echo.

REM Build wheel distribution
echo Building wheel distribution...
python setup.py bdist_wheel
if errorlevel 1 (
    echo Installing wheel package...
    python -m pip install wheel
    python setup.py bdist_wheel
)
echo    Wheel distribution created
echo.

REM List built files
echo Built files:
dir /b dist
echo.

REM Installation instructions
echo ================================================================
echo   Build Complete!
echo ================================================================
echo.
echo To install the package:
echo   pip install dist\lolicode_generator-1.0.0-py3-none-any.whl
echo.
echo To run the GUI after installation:
echo   lolicode-gui
echo.
echo Or run directly:
echo   python gui_app.py
echo.
pause
