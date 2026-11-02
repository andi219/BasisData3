import mysql.connector
import random
import time

# Konfigurasi Database (Sesuaikan dengan setup kamu)
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",          # Isi password MySQL kamu jika ada
    "database": "uts"        # Nama database kamu
}

TOTAL_DATA = 100_000
BATCH_SIZE = 10_000

# Rentang ID pemain dan item yang ada di database kamu
TOTAL_PEMAIN = 20  # pemain_id 1 s/d 20
TOTAL_ITEM = 10    # item_id 1 s/d 10

print("Mulai memasukkan 100.000 data ke tabel penyimpanan...")
start_time = time.time()

with mysql.connector.connect(**db_config) as db:
    with db.cursor() as cursor:
        sql = "INSERT INTO penyimpanan (pemain_id, item_id) VALUES (%s, %s)"
        
        data_batch = []
        for i in range(1, TOTAL_DATA + 1):
            # Generate ID acak
            pemain_id = random.randint(1, TOTAL_PEMAIN)
            item_id = random.randint(1, TOTAL_ITEM)
            
            data_batch.append((pemain_id, item_id))
            
            # Kirim per porsi 10.000 data biar super cepat
            if len(data_batch) == BATCH_SIZE:
                cursor.executemany(sql, data_batch)
                db.commit()
                print(f"Progress: {i} / {TOTAL_DATA} data terisi...")
                data_batch.clear()

end_time = time.time()
durasi = round(end_time - start_time, 2)

print(f"\nSelesai! 100.000 data berhasil masuk dalam waktu {durasi} detik!")