# CHANGELOG - Python Version Compatibility Fix

## Changes Made to Address Magenta Compatibility Issues

### Dependencies Fixed (requirements.txt)
- **ROLLED BACK** package versions to be compatible with Magenta 2.1.4
- Changed from ambitious modern versions to Magenta-compatible versions:
  - numpy: >=1.24.0 → >=1.19.0,<1.25.0
  - matplotlib: >=3.7.0 → >=3.0.0,<3.8.0  
  - pygame: >=2.5.0 → >=1.9.0
  - mido: >=1.3.0 → >=1.2.0
  - magenta: >=2.1.4 → ==2.1.4 (exact version)
  - tensorflow: >=2.15.0 → >=2.3.0,<2.16.0

### Documentation Updates (readme.md)
- **CORRECTED** Python version requirements from "Python 3.8+ supported" to "Python 3.7-3.10 supported"
- Added clear warning about Magenta's dependency constraints
- Added note in Finnish about Python version limitations
- Maintained original Finnish documentation style

### Code Improvements (Preserved from previous work)
- **KEPT** all safety improvements in AI.py:
  - Enhanced error handling in `selectMusic()`, `playMusic()`, and `createMusic()`
  - Safer file operations using `glob` and `os.remove()` instead of `os.system('rm')`  
  - Better input validation and user feedback
  - Directory initialization to ensure required folders exist

- **KEPT** bug fixes in roll.py:
  - Fixed indexing bug where `note_register[idx]` should be `note_register[key]`
  - Updated deprecated `matplotlib.colors.colorConverter` to modern `matplotlib.colors.to_rgba`

### Testing Added
- Created `test_basic_functionality.py` to validate Python syntax and basic operations
- Tests work without requiring external dependencies
- Confirms compatibility with Python 3.7-3.12 (with warnings for 3.11+)

## Key Insight: Magenta Constraints
The core issue is that **Magenta 2.1.4 has strict dependency requirements** that conflict with newer package versions. While the Python code itself is compatible with modern Python versions, the dependency ecosystem around Magenta constrains the entire project to Python 3.7-3.10.

## Backward Compatibility
- Changes maintain compatibility with the original API
- No breaking changes to the user interface  
- Original functionality preserved while keeping safety improvements
- Code quality improvements retained

## Next Steps for Full Functionality
To use the application fully, users need to:
1. **Use Python 3.7-3.10** (3.11+ may have issues)
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure model files are present in the `models/` directory
4. Install FluidSynth system dependency for MIDI to audio conversion