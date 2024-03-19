# za svakki film je poznat naziv,broj pozitivnih komentara za taj film i broj negatvnih komentara za taj film 
lista_filmova=  [{"naziv":"The Godfather", "br_pozitivni":1000,"br_negativni":10},
                  {"naziv":"The Pianist", "br_pozitivni":500,"br_negativni": 30}, 
                  {"naziv":"A Beautiful Mind","br_pozitivni":600,"br_negativni": 45}] 

max_film = ()
max_value = 0
for film in lista_filmova:
    if film["br_pozitivni"] > max_value:
        max_value = film['br_pozitivni']
        max_film = film
print(max_film)

for film in lista_filmova:
    if film["naziv"].startswith(term):
        print(film)
