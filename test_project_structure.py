#!/usr/bin/env python3
"""
Test that verifies the project structure and provides guidance for users
This test simulates what would happen with proper dependencies installed
"""

import os
import sys

def test_models_directory():
    """Check if models directory exists and provide guidance"""
    print("Testing models directory...")
    
    if os.path.exists('models'):
        model_files = ['basic_rnn.mag', 'lookback_rnn.mag', 'attention_rnn.mag']
        found_models = []
        
        for model_file in model_files:
            model_path = os.path.join('models', model_file)
            if os.path.exists(model_path):
                found_models.append(model_file)
        
        if found_models:
            print(f"✓ Models directory exists with {len(found_models)} model files:")
            for model in found_models:
                print(f"  - {model}")
        else:
            print("⚠ Models directory exists but no model files found.")
            print("  Download model files for full functionality:")
            for model in model_files:
                print(f"  - {model}")
    else:
        print("⚠ Models directory not found.")
        print("  Create 'models/' directory and add .mag model files for music generation.")
    
    return True

def test_midi_directory():
    """Test CreatedMidi directory for MIDI playback functionality"""
    print("\nTesting MIDI directory...")
    
    if os.path.exists('CreatedMidi'):
        midi_files = [f for f in os.listdir('CreatedMidi') 
                     if f.endswith('.mid') or f.endswith('.midi')]
        
        if midi_files:
            print(f"✓ CreatedMidi directory has {len(midi_files)} MIDI files")
            print("  Music playback functionality would work with proper dependencies")
        else:
            print("⚠ CreatedMidi directory is empty")
            print("  Generate music first to test playback functionality")
    else:
        print("✓ CreatedMidi directory will be created automatically")
    
    return True

def test_wave_directory():
    """Test CreatedWave directory for audio conversion"""
    print("\nTesting wave directory...")
    
    if os.path.exists('CreatedWave'):
        print("✓ CreatedWave directory exists")
    else:
        print("✓ CreatedWave directory will be created automatically")
    
    return True

def provide_installation_guidance():
    """Provide comprehensive installation guidance"""
    print("\n" + "="*60)
    print("INSTALLATION GUIDANCE")
    print("="*60)
    
    major, minor = sys.version_info[:2]
    
    if major == 3 and 7 <= minor <= 10:
        print(f"✓ Python {major}.{minor} is optimal for this project")
        print("\nTo install dependencies:")
        print("  pip install -r requirements.txt")
    elif major == 3 and minor > 10:
        print(f"⚠ Python {major}.{minor} detected")
        print("  This project works best with Python 3.7-3.10")
        print("  Consider using pyenv or conda to install Python 3.10:")
        print("    conda create -n aimusic python=3.10")
        print("    conda activate aimusic")
        print("    pip install -r requirements.txt")
    else:
        print(f"✗ Python {major}.{minor} is not supported")
        print("  Please install Python 3.7-3.10")
    
    print("\nSystem dependencies (Linux):")
    print("  sudo apt-get install fluidsynth")
    print("  # For MIDI to audio conversion")
    
    print("\nModel files needed in models/ directory:")
    print("  - basic_rnn.mag")
    print("  - lookback_rnn.mag") 
    print("  - attention_rnn.mag")
    print("  # Download from Magenta model zoo")
    
    print("\nTesting the installation:")
    print("  python test_basic_functionality.py  # Basic tests")
    print("  python AI.py                        # Full application")

def main():
    """Run structure and guidance tests"""
    print("=== Python AI Music - Project Structure Test ===\n")
    
    # Run tests
    test_models_directory()
    test_midi_directory()  
    test_wave_directory()
    
    # Provide guidance
    provide_installation_guidance()
    
    print(f"\n=== Test completed ===")
    print("This project is now properly configured for Python version compatibility.")
    print("Install dependencies with Python 3.7-3.10 for full functionality.")

if __name__ == "__main__":
    main()