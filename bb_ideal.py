def hitung_berat_ideal(tinggi, jenis_kelamin, unit_tinggi='cm'):
    if unit_tinggi.lower() == 'inch':
        tinggi = tinggi * 2.54  # Konversi tinggi dari inch ke cm jika diberikan dalam inch

    if jenis_kelamin.lower() == "pria":
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 10 / 100)
    elif jenis_kelamin.lower() == "wanita":
        berat_ideal = (tinggi - 100) - ((tinggi - 100) * 15 / 100)
    else:
        berat_ideal = None
    return berat_ideal

def pesan_kesehatan(berat_badan):
    if berat_badan is not None:
        if berat_badan < 18.5:
            return "Anda berisiko kekurangan berat badan. Penting untuk memastikan asupan nutrisi yang cukup."
        elif 18.5 <= berat_badan < 25:
            return "Berat badan Anda dalam kisaran normal. Pertahankan gaya hidup sehat!"
        else:
            return "Anda berisiko kelebihan berat badan. Pertimbangkan untuk memperbaiki pola makan dan beraktivitas fisik."
    return "Tidak dapat memberikan pesan kesehatan karena jenis kelamin tidak valid."

def main():
    try:
        tinggi_input = float(input("Masukkan tinggi: "))
        unit_tinggi_input = input("Masukkan unit tinggi (cm/inch): ").lower()
        jenis_kelamin_input = input("Masukkan jenis kelamin (Pria/Wanita): ")

        if unit_tinggi_input not in ['cm', 'inch']:
            print("Unit tinggi yang dimasukkan tidak valid. Masukkan 'cm' atau 'inch'.")
            return

        berat_ideal = hitung_berat_ideal(tinggi_input, jenis_kelamin_input, unit_tinggi_input)

        if berat_ideal is not None:
            print(f"Berat badan ideal Anda adalah {berat_ideal:.2f} kg.")
            print(pesan_kesehatan(berat_ideal))
        else:
            print("Jenis kelamin yang dimasukkan tidak valid. Masukkan 'Pria' atau 'Wanita'.")
    except ValueError:
        print("Masukkan tinggi dengan format bilangan.")

if __name__ == "__main__":
    main()
