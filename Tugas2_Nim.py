#fungsi enkripsi ke deskripsi
#kunci 3 
#19102290 = "SATU SEMBILAN SATU NOL DUA DUA SEMBILAN NOL"
shift = 3 # menentukan jumlah shift

encrypted_text = "VDWX VHPELODQ VDWX QRO GXD GXD VHPELODQ QRO"

plain_text = ""

for c in encrypted_text:

    # periksa apakah karakter adalah huruf besar
    if c.isupper():

        # cari posisi di 0-25
        c_unicode = ord(c)

        c_index = ord(c) - ord("A")

        # melakukan pergeseran negatif
        new_index = (c_index - shift) % 26

        # ubah ke karakter baru
        new_unicode = new_index + ord("A")

        new_character = chr(new_unicode)

        # tambahkan ke string biasa
        plain_text = plain_text + new_character

    else:

        
        plain_text += c

print("Encrypted text:",encrypted_text)

print("Decrypted text:",plain_text)