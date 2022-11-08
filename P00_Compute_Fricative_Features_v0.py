#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Cálculo de características acústicas em fricativas
Minha humilde contribuição para o trabalho de Wellington Araujo Mendes Junior.
---
Data: 03/08/2022
Autor: Adelino P. Silva
mail: adelinocpp@gmail.com, adelinocpp@gmail.com, adelino@ufmg.br
tel: +55 31 98801-3605

--- 
Rotina para a leitura de arquivos do tipo .TextgGrid (praat) e calculo de 
taxas espectrais como:
1 - HNR (de Signal_Analysis.features.signal)
2 - centro de gravidade espectral do tipo 1, 2 e 2/3, (vide link abaixo) e
3 - Low-frequency-to-total intensities ratio (LTF), vide GRADOVILLE (2021).

Centro de gravidade praat:
https://www.fon.hum.uva.nl/praat/manual/Spectrum__Get_centre_of_gravity___.html

GRADOVILLE, M. S., Validity in measurements of fricative voicing: Evidence from 
Argentine Spanish. In: Selected proceedings of the 5th Conference on Laboratory 
Approaches to Romance Phonology. Somerville, MA: Cascadilla Proceedings Project, 
2011. p. 59-74.
----
Contribuições basicas de funções:
textgrid_to_interval_matrix: decompõe o arquivo .Textgrid em uma matriz de intervalos
spectral_ratios: calcula os centros de gravidade e LTF
---
Livre para uso e modificações.
Em caso de dúvidas entre em contato.
"""
from utils.file_utils import list_contend, textgrid_to_interval_matrix, spectral_ratios
from scipy.io import wavfile
from Signal_Analysis.features.signal import get_HNR
import numpy as np
from pathlib import Path

import warnings
warnings.filterwarnings("ignore")
# -----------------------------------------------------------------------------

AUDIO_FOLDER = '../Audios/'
CSVFILE = './csvDataAudios.csv'
audiofiles = list_contend(folder=AUDIO_FOLDER, pattern=('.wav',))
textgridfiles = list_contend(folder=AUDIO_FOLDER, pattern=('.textgrid',))

if (len(audiofiles) != len(textgridfiles)):
    print("Erro: número de arquivos de áudio não corresponde ao numero de TextGrid")

# Tamanho do passo de tempo em segundos
valStep = 0.01

csvLines = []
strTitle = "Arquivo,Ordem,Etiqueta,Duracao,Vogal Presente,Simbilante,Forca,Idioma,Etapa,Contexto,HNR,GOG1,GOG2,GOG23,LTF\n"
csvLines.append(strTitle)
for idxtg, tgFile in enumerate(textgridfiles):
    value = textgrid_to_interval_matrix(tgFile,tierNumber=0)
    intervalMtx = value[0]
    sr, audio = wavfile.read(audiofiles[idxtg])
    nSamples, nChannel = audio.shape
    if (nChannel > 1):
        audio = np.mean(audio,axis = 1)
    audio = audio/np.max(np.abs(audio))
    for idxL, interval in enumerate(intervalMtx):
        nIni = int(interval[0]*sr)
        nFim = int(interval[1]*sr)
        duration = interval[1] - interval[0]
        selAudio = audio[nIni:nFim]
        vecHNR = get_HNR(selAudio,sr,time_step=valStep)
        COG_1, COG_2, COG_23, LTF = spectral_ratios(selAudio,sr,time_step=valStep)
        strVogal = "sem vogal epentética precedente"
        strSimbilante = "sibilante desvozeada"
        strForca = "oclusiva precedente regular"
        strIdioma = "Inglês"
        strEtapa = "nomeação de figuras"
        strContexto = "seguido de pausa"
        strData = "{:},{:},{:},{:},{:},{:},{:},{:},{:},{:},{:},{:},{:},{:},{:}\n".format(
                                              Path(audiofiles[idxtg]).stem,
                                              idxL,interval[2],duration,
                                              strVogal, strSimbilante, strForca,
                                              strIdioma,  strEtapa, strContexto,
                                              vecHNR,np.mean(COG_1),
                                              np.mean(COG_2),np.mean(COG_23),np.mean(LTF))
        csvLines.append(strData)
with open(CSVFILE, 'w') as file:
        file.writelines(csvLines)
