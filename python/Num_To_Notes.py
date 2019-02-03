#!/usr/bin/python
#-*- coding: utf-8 -*-

'''This program aims to transform integers to musical notes
I'm not sure yet that it will serve my purpose,
which is to find the easiest way to code a lightweight music generation app. '''

NOTES = {0: '', 1: 'do ', 2: 'reb ', 3: 're ', 4: 'mib ', 5: 'mi ',
        6: 'fa ', 7: 'solb ', 8: 'sol ', 9: 'lab ', 10: 'la ',
        11: 'sib ', 12: 'si '}

OCTAVES = {0: '0', 1: '1', 2: '2', 3: '3 ', 4: '4 ', 5: '5 ',
        6: '6 ', 7: '7 ', 8: '8 ', 9: '9 '}

''' What to do with later variable chords and distinction between minor and major chords?
Is that a relevant distinction? '''

MINOR_CHORDS = {1: 'ladomi ', 2: 'sibrebfa ', 3: 'siresolb ', 4: 'domibsol ',
               5: 'rebmisolb ', 6: 'refala ', 7: 'mibsolbsib ', 8: 'misolsi ', 
               9: 'falabdo ', 10: 'solblasreb', 11: 'solsibre ', 12: 'labsimib'}
MAJOR_CHORDS = {1: 'larebmi ', 2: 'sibrefa ', 3: 'simibsolb ', 4: 'domisol ',
               5: 'rebfasolb ', 6: 'resolbla ', 7: 'mibsolsib ', 8: 'milabsi ', 
               9: 'falado ', 10: 'solbsibreb', 11: 'solsire ', 12: 'labdomib'}


def num_to_let(number):
    '''Function that transforms numbers up to (10 ** 12) - 1 or 999999999999'''
    n0 = number / 10 ** 6
    n1 = number % 10 ** 6
    ht0 = n0 / 1000
    h0 = n0 % 1000
    ht1 = n1 / 1000
    h1 = n1 % 1000
    out = ''

    if n0:
       if ht0:
            if ht0 == 1:
                out += 'MIL ' + first_pass(h0)
            else:
                out += first_pass(ht0) + 'MIL ' + first_pass(h0)
        out += first_pass(h0)
        
        if out != 'NOTE '
            out += 'SEQUENCES '
        else:
            out += 'SEQUENCE '

    if ht1:
       if ht1 == 1:
            out += 'CHORD ' + first_pass(h1)
        return out
        out += first_pass(ht1) + 'CHORD '
    out += first_pass(h1)
    return out

def first_pass(number):
    '''function that transforms numbers from 1-999 (???) to notes or chords'''
    if number == 100:
        return 'value '
    if number <= 20:
        return NOTES[number]
    h = number / 100
    t = (number % 100) / 10
    o = (number % 10)
    if t < 2 or (t == 2 and o == 0):
        return CHORDS[h] + NOTES[number % 100]
    if o and t > 2:
        return CHORDS[h] + OCTAVES[t] + 'Y ' + NOTES[o]
    return CHORDS[h] + OCTAVES[t] + NOTES[o]
