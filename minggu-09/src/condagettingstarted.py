#Verifikasi bahwa conda diinstal dan berjalan di sistem
conda --version

#Update conda
conda update conda

#ketik yuntuk memperbarui:
Proceed ([y]/n)? y

#Buat environment baru dan instal paket di dalamnya.
conda create --name snowflakes biopython

#Untuk melihat daftar semua environment
conda info --envs

#Daftar environment muncul, mirip dengan berikut ini:
conda environments:

    base           /home/username/Anaconda3
    snowflakes   * /home/username/Anaconda3/envs/snowflakes

#Buat environment baru bernama "snakes" yang berisi Python 3.9:
conda create --name snakes python=3.9

#Aktifkan environment baru:
conda activate snakes

#Verifikasi bahwa environment snakes telah ditambahkan dan aktif:
conda info --envs

# conda environments:
#
base                     /home/username/anaconda3
snakes                *  /home/username/anaconda3/envs/snakes
snowflakes               /home/username/anaconda3/envs/snowflakes

#Verifikasi versi Python mana yang ada di environment
python --version

#Nonaktifkan environment snakes dan kembali ke environment dasar:
conda activate