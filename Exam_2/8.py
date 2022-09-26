# 8. Есть словарь песен группы Depeche Mode
# violator songsdict = { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30,
# 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен. Создайте список песен, время звучаниях которых больше 5 минут
# Создайте новый словарь тех песен,
# в название которых состоит из одного слова

songsdict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 5.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68
}

total_sound_time = 0
list_long_songs = []
dict_shortname_songs = {}
for songs in songsdict :
    total_sound_time += songsdict[songs]
    if songsdict[songs] > 5.0 :
        list_long_songs.append(songs)
    if " " not in songs :
        dict_shortname_songs[songs] = songsdict[songs]
print(total_sound_time,"\n",list_long_songs,"\n",dict_shortname_songs)
