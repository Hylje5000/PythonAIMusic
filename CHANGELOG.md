# CHANGELOG - Python Version Modernization

## Changes Made to Support Modern Python Versions (3.8+)

### Dependencies Updated (requirements.txt)
- Updated all package versions to use minimum version constraints instead of exact versions
- Changed from exact pins (==) to minimum versions (>=) for better compatibility
- Updated target versions:
  - numpy: 1.21.0 -> >=1.24.0
  - matplotlib: 3.2.0 -> >=3.7.0  
  - pygame: 1.9.6 -> >=2.5.0
  - mido: 1.2.6 -> >=1.3.0
  - magenta: 1.2.2 -> >=2.1.4
  - tensorflow: 2.9.3 -> >=2.15.0

### Code Improvements (AI.py)

#### Enhanced Error Handling
- Added bounds checking in `selectMusic()` to prevent crashes when there are fewer than 5 MIDI files
- Added file filtering to only show .mid and .midi files
- Added try-catch blocks in `playMusic()` with informative error messages
- Added input validation in `createMusic()` with better user feedback

#### Improved User Experience  
- Added 'q' option to quit in addition to '0'
- Fixed main loop logic to properly handle exit conditions
- Added directory initialization to ensure required folders exist
- Better error messages for invalid inputs

#### Safer File Operations
- Replaced unsafe `os.system('rm ...')` with safer Python file operations using `glob` and `os.remove()`
- Added existence checks for model files before attempting to use them
- Better path handling with `os.path.join()`

### Code Fixes (roll.py)

#### Bug Fixes
- Fixed indexing bug in `get_roll()` method where `note_register[idx]` should be `note_register[key]`
- Updated deprecated `matplotlib.colors.colorConverter` to modern `matplotlib.colors.to_rgba`

#### Compatibility Improvements
- Updated import statements for modern matplotlib versions
- Maintained backward compatibility where possible

### Documentation Updates (readme.md)
- Updated Python version requirements from "Python 3.7 only" to "Python 3.8+ supported"
- Added note about modern Python compatibility
- Maintained original Finnish documentation

### Testing
- All code compiles successfully on Python 3.12
- Basic functionality tests pass
- Syntax is compatible with Python 3.8-3.12

## Backward Compatibility
- Changes maintain compatibility with the original API
- No breaking changes to the user interface
- Original functionality preserved while adding improvements

## Next Steps for Full Functionality
To use the application fully, users need to:
1. Install dependencies: `pip install -r requirements.txt`
2. Ensure model files are present in the `models/` directory
3. Install FluidSynth system dependency for MIDI to audio conversion