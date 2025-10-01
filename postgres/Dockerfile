FROM postgres:15

# --- Environment Variables ---
ENV POSTGRES_USER=nodered_user
ENV POSTGRES_PASSWORD=mysecretpassword
# POSTGRES_DB akan otomatis dibuat dan diinisialisasi
ENV POSTGRES_DB=nodered_db 

# --- Inisialisasi Database ---
# Kunci: Salin file SQL dan skrip ke direktori initdb.d
# File dengan ekstensi .sql akan otomatis dimuat ke database yang dibuat
#COPY schema.db /docker-entrypoint-initdb.d/
COPY create-db.sh /docker-entrypoint-initdb.d/

# Pastikan skrip memiliki izin eksekusi
RUN chmod +x /docker-entrypoint-initdb.d/create-db.sh

# Tidak perlu perintah RUN tambahan, semua akan dieksekusi saat container START (RUN)


