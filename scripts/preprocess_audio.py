# %%
import os
import torch
import torchaudio
import librosa
import numpy as np
from tqdm import tqdm


txtpath = './data/train_phon.txt'
wav_path = 'G:/data/arabic-speech-corpus/wav'
wav_new_path = 'G:/data/arabic-speech-corpus/wav_new'

# txtpath='./data/test_phon.txt'
# wav_path='G:/data/arabic-speech-corpus/test set/wav'
# wav_new_path='G:/data/arabic-speech-corpus/test set/wav_new/'

# %%

# silence_audio_size = 256 * 3

# resampler = torchaudio.transforms.Resample(48_000, 22_050,
#                                            lowpass_filter_width=1024)

# lines = open(txtpath).readlines()

# for line in tqdm(lines):

#     fname = line.split('" "')[0][:-1]

#     fpath = os.path.join(wav_path, fname)
#     wave, _ = torchaudio.load(fpath)

#     wave = resampler(wave)

#     wave_ = wave[0].numpy()
#     wave_ = wave_ / np.abs(wave_).max() * 0.999
#     wave_ = librosa.effects.trim(
#         wave_, top_db=23, frame_length=1024, hop_length=256)[0]
#     wave_ = np.append(wave_, [0.]*silence_audio_size)

#     torchaudio.save(f'{wav_new_path}/{fname}',
#                     torch.Tensor(wave_).unsqueeze(0), 22_050)
    

def process_audio(phonetics_file_path , wav_path , audio_sampling_rate , target_sampling_rate):
    silence_audio_size = 256 * 3
    
    wav_new_path = wav_path + '_new'

    os.makedirs(wav_new_path , exist_ok=True)
    
    resampler = torchaudio.transforms.Resample(audio_sampling_rate, target_sampling_rate,
                                            lowpass_filter_width=1024)

    lines = open(phonetics_file_path).readlines()

    for line in tqdm(lines):

        fname = line.split('" "')[0]
        fname=fname.strip('\"')

        fpath = os.path.join(wav_path, fname)
        wave, _ = torchaudio.load(fpath)

        wave = resampler(wave)

        wave_ = wave[0].numpy()
        wave_ = wave_ / np.abs(wave_).max() * 0.999
        wave_ = librosa.effects.trim(
            wave_, top_db=23, frame_length=1024, hop_length=256)[0]
        wave_ = np.append(wave_, [0.]*silence_audio_size)

        torchaudio.save(f'{wav_new_path}/{fname}',
                        torch.Tensor(wave_).unsqueeze(0), target_sampling_rate)
        
        
    return " successfully resample audios "    
    
