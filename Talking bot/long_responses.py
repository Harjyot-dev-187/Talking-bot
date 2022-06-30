import random


R_Eating = "I don't like eating anything because I am a bot obviously!"
W_weather = "Can't you just google on internet"
U_required = "well you build me , so every thing I do it is your responsibility"





def unknown():
    response = ['Could you please re-phrase that?', "...", "Sounds about right", "what does that mean"][random.randrange(4)]
    return response
