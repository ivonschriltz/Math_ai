import operator
import speech_recognition as s_r
import Grams.py
from Grams.py import *

#Prints version
print("Your speech_recognition version is : "+s_r.__version__)

#Recognizer
r = s_r.Recognizer()
my_mic_device = s_r.Microphone() #sr.Microphone.list_microphone_names()

with my_mic_device as source:
    print("Is this Math?")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
my_string=r.recognize_google(audio)

def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        'x' : operator.mul,
        'divided' :operator.__truediv__,
        'Mod' : operator.mod,
        'mod' : operator.mod,
        '^' : operator.xor,
        }[op]
def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    return get_operator_fn(oper)(op1, op2)

while True:
    print(my_string)
    if my_string is lowm_names
print(eval_binary_expr(*(my_string.split())))
