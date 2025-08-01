# Dokumen Persyaratan Produk (PRD) - MVP: Truth Consensus Engine

## 1. Ikhtisar Proyek

Truth Consensus Engine adalah sebuah alat yang dirancang untuk memerangi disinformasi dengan menganalisis informasi dari berbagai sumber mengenai topik tertentu. Tujuannya adalah untuk mengidentifikasi fakta konsensus dan menyoroti klaim yang bertentangan atau belum terverifikasi menggunakan Pemrosesan Bahasa Alami (NLP). Mesin ini akan memberikan pengguna cara yang andal untuk memahami konsensus faktual dan mengidentifikasi misinformasi.

## 2. Tujuan

*   Memberikan pemahaman yang jelas kepada pengguna mengenai konsensus faktual pada topik tertentu dengan mengumpulkan dan menganalisis informasi dari berbagai sumber.
*   Mengidentifikasi dan menandai klaim yang bertentangan atau belum terverifikasi yang ada dalam informasi yang dianalisis.
*   Berfungsi sebagai alat dasar untuk memerangi penyebaran misinformasi dengan menawarkan wawasan yang dapat diverifikasi.

## 3. Fitur (MVP)

*   **Input Topik**: Pengguna dapat memasukkan topik spesifik untuk dianalisis.
*   **Agregasi Sumber**: Sistem akan mengumpulkan informasi dari sekumpulan sumber berita dan jurnal ilmiah terkemuka yang telah ditentukan sebelumnya yang relevan dengan topik yang dimasukkan.
*   **Analisis Berbasis NLP**: Memproses informasi yang dikumpulkan untuk mengidentifikasi klaim utama dan membandingkannya di berbagai sumber.
*   **Identifikasi Fakta Konsensus**: Menyoroti klaim yang secara konsisten dilaporkan dan diverifikasi di berbagai sumber.
*   **Penyorotan Klaim Bertentangan/Belum Terverifikasi**: Menandai klaim yang diperdebatkan, kurang bukti pendukung, atau bertentangan dengan sumber lain.
*   **Tampilan Hasil**: Menyajikan temuan dalam format yang jelas dan mudah dipahami, menunjukkan fakta konsensus dan perbedaan yang disorot.

## 4. Kisah Pengguna

*   **Sebagai seorang jurnalis**, saya ingin memasukkan topik berita dan dengan cepat melihat apa konsensus pelaporan faktual di berbagai sumber, sehingga saya dapat memastikan keakuratan dalam artikel saya dan menghindari penyebaran misinformasi.
*   **Sebagai seorang peneliti**, saya ingin memasukkan topik ilmiah dan mengidentifikasi area konsensus dan ketidaksepakatan di antara studi yang diterbitkan, sehingga saya dapat fokus pada pertanyaan yang belum terselesaikan atau memverifikasi temuan yang ada.
*   **Sebagai warga negara yang peduli**, saya ingin memasukkan topik yang menjadi kepentingan publik dan memahami fakta yang terverifikasi versus klaim yang diperdebatkan, sehingga saya dapat membuat keputusan yang terinformasi dan membedakan kebenaran dari kepalsuan.

## 5. Kriteria Penerimaan

*   Sistem berhasil menerima topik yang disediakan pengguna.
*   Sistem mengambil informasi dari setidaknya 10 sumber berbeda yang telah ditentukan untuk topik tertentu.
*   Analisis NLP secara akurat mengidentifikasi setidaknya 70% klaim utama dalam informasi yang diagregasi.
*   Sistem secara akurat menyoroti setidaknya 80% klaim yang jelas bertentangan yang ditemukan di berbagai sumber.
*   Sistem secara akurat mengidentifikasi dan menyajikan setidaknya 70% klaim yang tampaknya merupakan fakta konsensus (yaitu, dilaporkan serupa oleh banyak sumber).
*   Output dengan jelas membedakan antara fakta konsensus dan perbedaan/klaim yang belum terverifikasi yang disorot.
*   Antarmuka pengguna intuitif dan memungkinkan input topik yang mudah serta tampilan hasil yang jelas.

## 6. Rencana Masa Depan

*   Memperluas jumlah dan variasi sumber data, termasuk media sosial dan outlet berita alternatif, dengan bobot yang sesuai untuk keandalan.
*   Mengimplementasikan teknik NLP lanjutan untuk analisis sentimen dan deteksi bias dalam sumber.
*   Mengembangkan mekanisme umpan balik pengguna untuk meningkatkan keandalan sumber dan verifikasi klaim.
*   Berintegrasi dengan database organisasi pemeriksa fakta.
*   Membuat API publik untuk pengembang mengintegrasikan Truth Consensus Engine ke dalam aplikasi lain.
*   Mengembangkan ekstensi peramban untuk analisis konten web secara real-time.
