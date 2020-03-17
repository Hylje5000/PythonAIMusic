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
    return input()

def createMusic():
    # Get model choice
    print('1 Basic model')
    print('2 Lookback model')
    print('3 Attention model')
    model = input("Choose model to use: ")
    if model == '1':
        modelfile = "basic_rnn.mag"
        modelname = 'basic_rnn'
    elif model == '2':
        modelfile = "lookback_rnn.mag"
        modelname = 'lookback_rnn'
    elif model == '3':
        modelfile = "attention_rnn.mag"
        modelname = 'attention_rnn'


    # Getting current working directory
    pwd = os.getcwd()
    # Clear CreatedMidi/ folder
    os.system('rm ' + pwd + '/CreatedMidi/*')
    # Creating .Midi files with Magenta
    os.system('melody_rnn_generate --config=' + modelname + ' --bundle_file=' + pwd + '/models/' + modelfile + ' --output_dir=' + pwd + '/CreatedMidi/ --num_outputs=5 --num_steps=128 --primer_melody="[60]"')


def selectMusic():
    #Listing CreatedMidi/ directory and getting choice
    fileList = os.listdir('CreatedMidi/')
    print('1 ' + fileList[0])
    print('2 ' + fileList[1])
    print('3 ' + fileList[2])
    print('4 ' + fileList[3])
    print('5 ' + fileList[4])
    print("Input number of file to play: ")
    fileToPlay = input()
    file = fileList[int(fileToPlay) - 1]
    playMusic(file)

def playMusic(song):
    #Converts midi to .wav and plays audio
    FluidSynth().midi_to_audio('CreatedMidi/' + song,'CreatedWave/audio.wav')
    pygame.mixer.init()
    pygame.mixer.music.load('CreatedWave/audio.wav')
    pygame.mixer.music.play()

    #Draws midi visualization
    midi = MidiFile('CreatedMidi/' + song)
    roll = midi.get_roll()
    midi.draw_roll()
    os.system('clear')



# Main program
answer = ''
titlebar()
while answer != 'q':
    answer = getchoice()
    titlebar()
    if answer == '1':
        createMusic()
    elif answer == '2':
        selectMusic()
    elif answer == '0':
        print('Exiting app...')
        quit()
