#!/usr/bin/python2.7
# coding: utf-8

# testowanie wrazliwosci minimapa na mutacje oraz wplywu parametrow
# nie do konca rozumialam dlaczego np minimap nie umie zmapowac odczytu na jego samego
# (mimo 100% identycznosci)
# chcialam sprawdzic na ile manipulujac parametrami mozna to zmienic
# zasadniczo to zapis sesji ipythona, wiec troche balaganiarski, ale zapisuje na wszelki wypadek

import random
import mappy

def mutuj(read, liczba_mutacji):
    read = list(read)
    gdzie_mutacje = random.sample(range(len(read)), liczba_mutacji)
    nukleotydy = ['A','T','C','G']
    for i in gdzie_mutacje:
        tmp_nukleotydy = [nuk for nuk in nukleotydy if nuk != read[i]]
        read[i] = random.choice(tmp_nukleotydy)
    return ''.join(read)

l_mutacji = 6

aligner_fq = mappy.Aligner("GXB01031_20180705_FAJ01742_GA40000_sequencing_run_23377_read_10049_ch_350_strand.fastq", preset="map-ont")
long_read = aligner_fq.seq("Read_10049", 2, 100)

success = 0
fail = 0
for i in range(1000):
    try:
        next(aligner_fq.map(mutuj(long_read, l_mutacji)))
        success += 1
    except:
        fail += 1

print("default parameters")
print("mapped: %d" % success)
print("not mapped: %d" % fail)
        
aligner_fq_w100 = mappy.Aligner("GXB01031_20180705_FAJ01742_GA40000_sequencing_run_23377_read_10049_ch_350_strand.fastq", preset="map-ont", w=100)
success_w100 = 0
fail_w100 = 0
        
for i in range(1000):
    try:
        next(aligner_fq_w100.map(mutuj(long_read, l_mutacji)))
        success_w100 += 1
    except:
        fail_w100 += 1
 

print("w = 100")
print("mapped: %d" % success_w100)
print("not mapped: %d" % fail_w100)
        
       
        
aligner_fq_w10 = mappy.Aligner("GXB01031_20180705_FAJ01742_GA40000_sequencing_run_23377_read_10049_ch_350_strand.fastq", preset="map-ont", w=10)
fail_w10 = 0
success_w10 = 0
for i in range(1000):
    try:
        next(aligner_fq_w10.map(mutuj(long_read, l_mutacji)))
        success_w10 += 1
    except:
        fail_w10 += 1

print("w = 10")
print("mapped: %d" % success_w10)
print("not mapped: %d" % fail_w10)
        
        
aligner_fq_w10_k5 = mappy.Aligner("GXB01031_20180705_FAJ01742_GA40000_sequencing_run_23377_read_10049_ch_350_strand.fastq", preset="map-ont", w=10, k=5)
fail_w10_k5 = 0
success_w10_k5 = 0
for i in range(1000):
    try:
        next(aligner_fq_w10_k5.map(mutuj(long_read, l_mutacji)))
        success_w10_k5 += 1
    except:
        fail_w10_k5 += 1

print("w = 10, k = 5")
print("mapped: %d" % success_w10_k5)
print("not mapped: %d" % fail_w10_k5)
