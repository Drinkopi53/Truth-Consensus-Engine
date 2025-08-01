Truth Consensus Engine
======================

Deskripsi
---------

Truth Consensus Engine adalah alat yang dirancang untuk memerangi disinformasi dengan menganalisis informasi dari berbagai sumber mengenai topik tertentu. Tujuannya adalah untuk mengidentifikasi fakta konsensus dan menyoroti klaim yang bertentangan atau belum terverifikasi menggunakan Pemrosesan Bahasa Alami (NLP). Mesin ini memberikan pengguna cara yang andal untuk memahami konsensus faktual dan mengidentifikasi misinformasi.

Proyek ini adalah implementasi dari Produk Minimum yang Layak (MVP) seperti yang dijelaskan dalam Dokumen Persyaratan Produk.

Fitur Utama
-----------

*   **Analisis Multi-Sumber**: Menganalisis sekumpulan file teks dari direktori data/ untuk mensimulasikan agregasi dari berbagai sumber.
    
*   **Identifikasi Klaim**: Menggunakan NLTK untuk membagi teks menjadi klaim-klaim individual (kalimat).
    
*   **Analisis Konsensus**: Mengelompokkan klaim-klaim serupa menggunakan normalisasi teks dan algoritma kesamaan Jaccard untuk mengidentifikasi ide-ide yang dilaporkan oleh banyak sumber.
    
*   **Klasifikasi Hasil**: Dengan jelas memisahkan hasil menjadi dua kategori:
    
    *   **Fakta Konsensus**: Klaim yang didukung oleh persentase sumber yang tinggi (ambang batas dapat disesuaikan).
        
    *   **Klaim Bertentangan / Belum Diverifikasi**: Klaim yang didukung oleh lebih sedikit sumber atau hanya satu sumber.
        
*   **Antarmuka Baris Perintah (CLI)**: Aplikasi yang mudah dijalankan dari terminal yang menampilkan laporan analisis yang terformat dengan baik.
    

Teknologi yang Digunakan
------------------------

*   **Python 3**
    
*   **NLTK (Natural Language Toolkit)**: Untuk tugas-tugas NLP inti seperti tokenisasi kalimat dan pemfilteran stopword.
    

Instalasi
---------

Untuk menyiapkan proyek ini secara lokal, ikuti langkah-langkah berikut:

1.  git clone cd
    
2.  pip install -r requirements.txt
    
3.  python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt\_tab')"
    

Penggunaan
----------

Untuk menjalankan Truth Consensus Engine, navigasikan ke direktori root proyek dan jalankan skrip main.py:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python main.py   `

Aplikasi akan secara otomatis:

1.  Membaca dan mengumpulkan semua file sumber (.txt) dari direktori data/.
    
2.  Menganalisis konten untuk menemukan konsensus dan klaim yang bertentangan.
    
3.  Mencetak laporan analisis yang diformat dengan baik ke konsol.
    

Anda dapat menyesuaikan analisis dengan memodifikasi atau mengganti file teks di dalam direktori data/.

Kontribusi
----------

Kontribusi dipersilakan! Jika Anda ingin meningkatkan proyek ini, silakan buka _issue_ untuk mendiskusikan ide-ide Anda atau kirimkan _pull request_ dengan perbaikan Anda.

Lisensi
-------

Proyek ini dilisensikan di bawah [Lisensi MIT](https://jules.google.com/LICENSE).
