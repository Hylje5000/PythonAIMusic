import os
import sys

# Check for optional dependencies and provide helpful error messages
try:
    import midi2audio
    from midi2audio import FluidSynth
    MIDI2AUDIO_AVAILABLE = True
except ImportError:
    MIDI2AUDIO_AVAILABLE = False
    print("Warning: midi2audio not available. Audio playback will not work.")

try:
    import pygame
    from pygame import mixer
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False
    print("Warning: pygame not available. Audio playback will not work.")

try:
    from roll import MidiFile
    ROLL_AVAILABLE = True
except ImportError:
    ROLL_AVAILABLE = False
    print("Warning: roll.py not available. Visualization will not work.")
    print("This likely means mido, numpy, or matplotlib are not installed.")

try:
    import magenta
    import tensorflow
    MAGENTA_AVAILABLE = True
except ImportError:
    MAGENTA_AVAILABLE = False
    print("Warning: Magenta not available. Music generation will not work.")
    print("Install with: pip install -r requirements.txt")


# Defining parts of the main program
def titlebar():
    os.system('clear')
    print("**********************************************")
    print("  AI music creator - built with Magenta  ")
    print("**********************************************")

def getchoice():
    print('1 Create new melodies')
    print('2 Listen to created melodies')
    print('0 Exit')
    print('q Quit')
    return input().strip().lower()

def createMusic():
    if not MAGENTA_AVAILABLE:
        print("Error: Magenta is not available. Cannot create music.")
        print("Please install dependencies with: pip install -r requirements.txt")
        print("Note: This project requires Python 3.7-3.10 for best compatibility.")
        return
    
    # Get model choice
    print('1 Basic model')
    print('2 Lookback model')
    print('3 Attention model')
    model = input("Choose model to use: ").strip()
    
    if model == '1':
        modelfile = "basic_rnn.mag"
        modelname = 'basic_rnn'
    elif model == '2':
        modelfile = "lookback_rnn.mag"
        modelname = 'lookback_rnn'
    elif model == '3':
        modelfile = "attention_rnn.mag"
        modelname = 'attention_rnn'
    else:
        print("Invalid model choice. Please select 1, 2, or 3.")
        return

    # Getting current working directory
    pwd = os.getcwd()
    
    # Check if model file exists
    model_path = os.path.join(pwd, 'models', modelfile)
    if not os.path.exists(model_path):
        print(f"Model file not found: {model_path}")
        print("Please ensure the model files are in the models/ directory.")
        return
    
    # Clear CreatedMidi/ folder (safer approach)
    try:
        import glob
        midi_files = glob.glob(os.path.join(pwd, 'CreatedMidi', '*'))
        for f in midi_files:
            if os.path.isfile(f):
                os.remove(f)
    except Exception as e:
        print(f"Warning: Could not clear CreatedMidi directory: {e}")
    
    # Creating .Midi files with Magenta
    cmd = f'melody_rnn_generate --config={modelname} --bundle_file={model_path} --output_dir={pwd}/CreatedMidi/ --num_outputs=5 --num_steps=128 --primer_melody="[60]"'
    print(f"Running: {cmd}")
    result = os.system(cmd)
    
    if result != 0:
        print("Error: Music generation failed. Make sure Magenta is properly installed.")
        print("You may need to install Magenta separately: pip install magenta")
    else:
        print("Music generation completed successfully!")


def selectMusic():
    #Listing CreatedMidi/ directory and getting choice
    fileList = os.listdir('CreatedMidi/')
    
    # Filter to only MIDI files
    fileList = [f for f in fileList if f.endswith('.mid') or f.endswith('.midi')]
    
    if not fileList:
        print("No MIDI files found in CreatedMidi/ directory!")
        return
    
    # Display available files with bounds checking
    print("Available MIDI files:")
    for i, file in enumerate(fileList[:5], 1):  # Show max 5 files
        print(f'{i} {file}')
    
    try:
        print("Input number of file to play: ")
        fileToPlay = input().strip()
        index = int(fileToPlay) - 1
        
        if 0 <= index < len(fileList):
            playMusic(fileList[index])
        else:
            print(f"Invalid choice. Please enter a number between 1 and {min(5, len(fileList))}")
    except ValueError:
        print("Invalid input. Please enter a number.")

def playMusic(song):
    #Converts midi to .wav and plays audio
    if not MIDI2AUDIO_AVAILABLE:
        print("Error: midi2audio not available. Cannot convert MIDI to audio.")
        print("Please install dependencies with: pip install -r requirements.txt")
        return
    
    if not PYGAME_AVAILABLE:
        print("Error: pygame not available. Cannot play audio.")
        print("Please install dependencies with: pip install -r requirements.txt")
        return
    
    try:
        FluidSynth().midi_to_audio('CreatedMidi/' + song,'CreatedWave/audio.wav')
        pygame.mixer.init()
        pygame.mixer.music.load('CreatedWave/audio.wav')
        pygame.mixer.music.play()

        #Draws midi visualization
        if ROLL_AVAILABLE:
            midi = MidiFile('CreatedMidi/' + song)
            roll = midi.get_roll()
            midi.draw_roll()
        else:
            print("Visualization not available (roll.py dependencies missing)")
        
        os.system('clear')
    except Exception as e:
        print(f"Error playing music file '{song}': {e}")
        print("Make sure the file exists and all dependencies are installed.")



# Main program
def check_python_version():
    """Check if Python version is in the supported range"""
    major, minor = sys.version_info[:2]
    if major == 3 and 7 <= minor <= 10:
        return True
    elif major == 3 and minor > 10:
        print(f"Warning: Python {major}.{minor} detected. This project works best with Python 3.7-3.10.")
        print("Magenta may have compatibility issues with newer Python versions.")
        return True
    else:
        print(f"Error: Python {major}.{minor} is not supported. Please use Python 3.7-3.10.")
        return False

def ensure_directories():
    """Ensure required directories exist"""
    dirs = ['CreatedMidi', 'CreatedWave', 'models']
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)

# Initialize
if not check_python_version():
    sys.exit(1)

ensure_directories()
answer = ''
titlebar()
while answer not in ['q', '0']:
    answer = getchoice()
    titlebar()
    if answer == '1':
        createMusic()
    elif answer == '2':
        selectMusic()
    elif answer in ['0', 'q']:
        print('Exiting app...')
        break
    else:
        print("Invalid choice. Please select 1, 2, 0, or q.")
