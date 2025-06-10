import os
import midi2audio
from midi2audio import FluidSynth
import pygame
from pygame import mixer
from roll import *
import magenta
import tensorflow


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
    try:
        FluidSynth().midi_to_audio('CreatedMidi/' + song,'CreatedWave/audio.wav')
        pygame.mixer.init()
        pygame.mixer.music.load('CreatedWave/audio.wav')
        pygame.mixer.music.play()

        #Draws midi visualization
        midi = MidiFile('CreatedMidi/' + song)
        roll = midi.get_roll()
        midi.draw_roll()
        os.system('clear')
    except Exception as e:
        print(f"Error playing music file '{song}': {e}")
        print("Make sure the file exists and all dependencies are installed.")



# Main program
def ensure_directories():
    """Ensure required directories exist"""
    dirs = ['CreatedMidi', 'CreatedWave', 'models']
    for dir_name in dirs:
        os.makedirs(dir_name, exist_ok=True)

# Initialize
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
