from editdistpy import damerau_osa

ORDINAL_BG_TO_INT = {
    "ПЪРВ": 1,
    "ВТОР": 2,
    "ТРЕТ": 3,
    "ЧЕТВЪРТ": 4,
    "ПЕТ": 5,
    "ШЕСТ": 6,
    "СЕДМ": 7,
    "ОСМ": 8,
    "ДЕВЕТ": 9,
    "ДЕСЕТ": 10,
    "ДВАДЕСЕТ": 20,
    "ТРИДЕСЕТ": 30,
    "ЧЕТИРИДЕСЕТ": 40,
    "ПЕТДЕСЕТ": 50,
    "ШЕСТДЕСЕТ": 60,
    "СЕДЕМДЕСЕТ": 70,
    "ОСЕМДЕСЕТ": 80,
    "ДЕВЕТДЕСЕТ": 90,
    "СТО": 100,
    "ДВЕСТА": 200,
    "ТРИСТА": 300,
    "ЧЕТИРИСТОТИН": 400,
    "ПЕТСТОТИН": 500,
    "ШЕСТОТИН": 600,
    "СЕДЕМСТОТИН": 700,
    "ОСЕМСТОТИН": 800,
    "ДЕВЕТСТОТИН": 900
}

def cyrillic_int_decoder(word_to_decode):

    #Load a dict with mapped ordinal bg
    numbers_mapped = ORDINAL_BG_TO_INT
    word_to_decode_upper = word_to_decode.upper()

    #Threshold to max distance when comparing words
    lex_sim_distance = 2

    #Setting up an initial distance, which will be minimized
    distance = 10
    decoded_number = 0

    for number in numbers_mapped:

        levenshtein_damerau_distance = damerau_osa.distance(word_to_decode_upper, number, lex_sim_distance)

        if levenshtein_damerau_distance > -1 and levenshtein_damerau_distance < distance:
                distance = levenshtein_damerau_distance
                decoded_number = numbers_mapped[number]

    return decoded_number

def string_list_decoder (assembly_name):

    assembly_list = assembly_name.split(' ')

    total = 0

    for assembly_word in assembly_list:

        total += cyrillic_int_decoder(assembly_word)

    return total
