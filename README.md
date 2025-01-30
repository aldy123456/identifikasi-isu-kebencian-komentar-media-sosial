# identifikasi isu kebencian komentar media sosial

Komentar ujaran kebencian di media sosial, yang mengandung bahasa kasar dan menghina, dapat merusak kesehatan mental serta menciptakan lingkungan digital yang tidak sehat. Oleh karena itu, deteksi otomatis terhadap ujaran kebencian menjadi penting untuk mengurangi dampak negatifnya.

Hate Speech (1): Komentar yang mengandung ujaran kebencian dan diskriminasi.
Offensive Language (2): Komentar yang mengandung bahasa kasar tetapi tidak termasuk ujaran kebencian.
Neither (0): Komentar yang tidak mengandung ujaran kebencian maupun bahasa kasar.
Metodologi:
  1. Menggunakan dataset yang telah diberi label untuk klasifikasi ujaran kebencian.
  2. Melakukan pemrosesan teks, termasuk pembersihan data, tokenisasi, dan stemming.
  3. Ekstraksi fitur menggunakan metode TF-IDF untuk merepresentasikan teks dalam bentuk numerik.
  4. Melatih model LightGBM, yang dikenal efisien dalam menangani dataset dengan jumlah fitur yang besar.
  5. Evaluasi model menggunakan metrik akurasi, dengan hasil mencapai 88%.
Tujuan Proyek:
✅ Membangun sistem klasifikasi otomatis untuk mendeteksi ujaran kebencian di media sosial.
✅ Mengurangi penyebaran komentar negatif dengan memberikan insight kepada moderator platform.
✅ Menggunakan teknik machine learning untuk meningkatkan akurasi deteksi dibandingkan metode rule-based.

Manfaat Proyek:
🔹 Membantu platform media sosial dalam menyaring komentar yang berpotensi merugikan pengguna.
🔹 Mendukung penelitian dalam bidang NLP dan machine learning terkait deteksi ujaran kebencian.
🔹 Dapat dikembangkan lebih lanjut dengan model yang lebih kompleks seperti transformer-based models (BERT, RoBERTa, dll.) untuk meningkatkan performa klasifikasi.

Kode sumber proyek ini dapat ditemukan di repositori GitHub berikut: [GitHub Repository Link] (tambahkan link repositori GitHub Anda). 🚀
