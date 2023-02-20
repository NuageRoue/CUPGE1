from dict import *

def get_nom(dict, num):
    if num in dict:
        return dict[num]
    raise KeyError("pas de clé {}".format(num))

print(get_nom(dict_etudiants1, 204909))

def get_numero(dict, value):
    if value in dict.values():
        key = [i for i in dict if dict[i] == value]
        return key
    raise ValueError('pas de valeur {} dans le dictionnaire'.format(value))


print(get_numero(dict_etudiants1, 'BOUVIER'))

def ten_multiple(dict):
    return [dict[k] for k in dict if k % 10 == 0]

def Beginning(dict):
    return [key for key in dict if dict[key][0] == 'B']


def get_occurrence(txt):
    dict = dict()
    for letter in txt:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict

def freq_letter(txt):
    dict = get_occurrence(txt)
    tot = len(txt)

    for key in dict:
        dict[key] /= tot
    return dict

def to_morse(txt):
    morse_transcription = ""
    for letter in txt:
        if letter.upper() in dict_morse:
            morse_transcription += dict_morse[letter.upper()]
        morse_transcription += ' '
    return morse_transcription[:-1:]
print(to_morse('le mot'))

def to_text(morse):
    txt = ''
    for letter in morse.split(' '):
        if letter == '':
            txt += ' '
        else:
            txt += get_numero(dict_morse, letter)[0]
    return txt

print(to_text(to_morse('le mot')))