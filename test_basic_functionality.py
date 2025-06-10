#!/usr/bin/env python3
"""
Basic functionality test for Python AI Music project
Tests syntax compatibility and basic operations without requiring external dependencies
"""

import os
import sys
import tempfile
import shutil

def test_python_version():
    """Test if Python version is in supported range"""
    print(f"Testing Python version: {sys.version}")
    major, minor = sys.version_info[:2]
    
    if major == 3 and 7 <= minor <= 10:
        print("✓ Python version is in optimal range (3.7-3.10)")
        return True
    elif major == 3 and minor > 10:
        print("⚠ Python version is newer than optimal (3.7-3.10), may have dependency issues")
        return True
    else:
        print("✗ Python version not supported")
        return False

def test_basic_imports():
    """Test imports that should always work"""
    try:
        import os
        import sys
        import glob
        import tempfile
        print("✓ Basic Python modules import successfully")
        return True
    except ImportError as e:
        print(f"✗ Basic imports failed: {e}")
        return False

def test_ai_py_syntax():
    """Test that AI.py has valid Python syntax"""
    try:
        with open('AI.py', 'r') as f:
            code = f.read()
        
        # Compile to check syntax
        compile(code, 'AI.py', 'exec')
        print("✓ AI.py has valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"✗ AI.py syntax error: {e}")
        return False
    except FileNotFoundError:
        print("✗ AI.py not found")
        return False

def test_roll_py_syntax():
    """Test that roll.py has valid Python syntax"""
    try:
        with open('roll.py', 'r') as f:
            code = f.read()
        
        # Compile to check syntax
        compile(code, 'roll.py', 'exec')
        print("✓ roll.py has valid Python syntax")
        return True
    except SyntaxError as e:
        print(f"✗ roll.py syntax error: {e}")
        return False
    except FileNotFoundError:
        print("✗ roll.py not found")
        return False

def test_directory_structure():
    """Test that required directories can be created"""
    test_dirs = ['test_CreatedMidi', 'test_CreatedWave', 'test_models']
    
    try:
        # Create test directories
        for dirname in test_dirs:
            os.makedirs(dirname, exist_ok=True)
            if not os.path.exists(dirname):
                raise Exception(f"Failed to create {dirname}")
        
        # Clean up
        for dirname in test_dirs:
            if os.path.exists(dirname):
                os.rmdir(dirname)
        
        print("✓ Directory creation/removal works")
        return True
    except Exception as e:
        print(f"✗ Directory operations failed: {e}")
        return False

def test_file_operations():
    """Test basic file operations used in the project"""
    try:
        # Test file creation and deletion
        test_file = 'test_file.txt'
        with open(test_file, 'w') as f:
            f.write('test content')
        
        if not os.path.exists(test_file):
            raise Exception("File creation failed")
        
        # Test file removal
        os.remove(test_file)
        
        if os.path.exists(test_file):
            raise Exception("File removal failed")
        
        print("✓ Basic file operations work")
        return True
    except Exception as e:
        print(f"✗ File operations failed: {e}")
        return False

def main():
    """Run all tests"""
    print("=== Python AI Music - Basic Functionality Test ===\n")
    
    tests = [
        test_python_version,
        test_basic_imports,
        test_ai_py_syntax,
        test_roll_py_syntax,
        test_directory_structure,
        test_file_operations
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"=== Results: {passed}/{total} tests passed ===")
    
    if passed == total:
        print("✓ All basic functionality tests passed!")
        print("Note: This doesn't test Magenta functionality which requires additional dependencies.")
        return True
    else:
        print("✗ Some tests failed. Check the output above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)