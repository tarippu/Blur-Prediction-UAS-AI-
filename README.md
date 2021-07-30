# Blur-Prediction_UAS-AI
Pada proyek 3 kemarin, permasalahan yang yang ada yaitu pada ojek online dalam perbandingan tarif perjalanan pada aplikasi gojek dan grab. Dan pada UAS ini permasalahan yang ada yaitu grab dan gojek memiliki fitur gofood dan grab food. Saat ini juga startup atau e-commerce shopee sudah memiliki fitur baru yaitu shopee food. Saat melakukan pemesanan pada fitur tersebut pada setiap aplikasi user atau driver dapat menggunakan fitur camera untuk mengirim gambar, sering terjadi pada saat pengambilan gambar tersebut driver atau user tidak menyesuaikan dengan baik saat mengambil gambar sehingga gambar tersebut terlihat buram. Untuk gambar yang buram tidak kualitasnya tidak akan bagus untuk dilihat.

Pada video ini saya akan memperlihatkan cara menghitung jumlah keburaman pada gambar menggunakan OpenCV, Python, dan operator Laplacian.

# Cara Penggunaan
Pastikan python dan pip diinstal. Kemudian, instal imutils dan cv2.
# instal opencv-python
pip instal cv2
# instal imutils 
pip instal imutils

# Keywoard menajalankan
python main.py --images images

# Cara kerja nya 
Yang pertama yaitu siapkan data set gambar  Ada yang kabur, ada yang tidak. Tujuannya adalah melakukan deteksi blur dengan OpenCV dan menandai gambar seperti itu. Metode laplacian, merupakan metode sederhana, mudah dan emiliki penalaran yang masuk akal. Dan dapat diimplementasikan hanya dalam satu baris kode.
Jika varians turun di bawah ambang batas yang telah ditentukan, maka gambar dianggap buram ; jika tidak, gambar tidak buram Laplacian sering digunakan untuk deteksi tepi. Asumsinya di sini adalah bahwa jika sebuah gambar mengandung varians yang tinggi, maka ada respon yang tersebar luas, baik seperti tepi dan tidak seperti tepi, mewakili gambar normal dalam fokus. Tetapi jika ada varians yang sangat rendah , maka ada sebaran respons yang kecil, yang menunjukkan bahwa sangat sedikit tepi pada gambar. Seperti yang diketahui, semakin banyak gambar yang diburamkan, semakin sedikit tepi yang ada. Ambang batas yang terlalu rendah dan Anda akan salah menandai gambar sebagai buram padahal sebenarnya tidak. Ambang batas yang terlalu tinggi maka gambar yang sebenarnya buram tidak akan ditandai sebagai buram.
