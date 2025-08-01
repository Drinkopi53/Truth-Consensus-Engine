import unittest
import sys
import os

# Tambahkan direktori 'src' ke path untuk mengimpor modul kita
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from src.analysis_engine import normalize_claim, analyze_sources
    from src.data_aggregator import aggregate_sources
except ImportError:
    # Fallback untuk lingkungan di mana path mungkin sudah benar
    from analysis_engine import normalize_claim, analyze_sources
    from data_aggregator import aggregate_sources

class TestAnalysisEngine(unittest.TestCase):
    """Menguji fungsionalitas inti dari mesin analisis."""

    def test_normalize_claim(self):
        """Menguji fungsi normalisasi klaim."""
        claim = "Ini adalah sebuah klaim PENTING dengan beberapa kata-kata."
        # Kata-kata seperti 'penting' dan 'beberapa' kemungkinan ada di daftar stopwords NLTK.
        # Pengujian ini memverifikasi bahwa normalisasi (huruf kecil, tanpa tanda baca, stopwords) berfungsi.
        expected = {'klaim', 'katakata'}
        self.assertEqual(normalize_claim(claim), expected)

    def test_analyze_sources_logic(self):
        """Menguji logika analisis inti dengan data tiruan yang terkontrol."""
        mock_data = [
            {'source_name': 's1.txt', 'content': 'Kucing suka tidur di bawah sinar matahari. Anjing suka bermain bola.'},
            {'source_name': 's2.txt', 'content': 'Kucing sangat suka tidur. Cuaca hari ini cerah.'},
            {'source_name': 's3.txt', 'content': 'Anjing suka sekali bermain. Kucing juga suka tidur.'},
            {'source_name': 's4.txt', 'content': 'Buku adalah sumber pengetahuan yang tak ternilai.'}
        ]

        # Dengan 4 sumber, kita atur rasio menjadi 0.75 agar ambang batas menjadi int(4 * 0.75) = 3.
        consensus, conflicting = analyze_sources(mock_data, similarity_threshold=0.4, consensus_threshold_ratio=0.75)

        # Harapan: 1 klaim konsensus (tentang kucing, dari 3 sumber)
        self.assertEqual(len(consensus), 1, "Harusnya ada 1 klaim konsensus (kucing)")
        self.assertEqual(consensus[0]['source_count'], 3, "Klaim konsensus kucing harusnya dari 3 sumber")
        self.assertIn('Kucing', consensus[0]['claim'])

        # Harapan: 3 klaim yang bertentangan/belum terverifikasi (anjing, cuaca, buku)
        self.assertEqual(len(conflicting), 3, "Harusnya ada 3 klaim yang bertentangan")

        # Verifikasi klaim 'Anjing' (2 sumber)
        anjing_claim = next((c for c in conflicting if 'Anjing' in c['claim']), None)
        self.assertIsNotNone(anjing_claim, "Klaim tentang anjing harusnya ada di daftar bertentangan")
        self.assertEqual(anjing_claim['source_count'], 2, "Klaim anjing harusnya dari 2 sumber")

class TestDataAggregator(unittest.TestCase):
    """Menguji fungsionalitas dari agregator data."""

    def test_aggregate_sources_happy_path(self):
        """Menguji bahwa agregator menemukan semua 10 file sumber."""
        # Pengujian ini bergantung pada data yang dibuat di langkah 2
        sources = aggregate_sources()
        self.assertEqual(len(sources), 10)
        # Verifikasi bahwa file diurutkan dengan benar
        self.assertEqual(sources[0]['source_name'], 'sumber_01.txt')
        self.assertEqual(sources[9]['source_name'], 'sumber_10.txt')

    def test_aggregate_sources_no_directory(self):
        """Menguji perilaku agregator dengan direktori yang tidak ada."""
        # Kita mengharapkan ini mencetak error, tetapi mengembalikan list kosong
        sources = aggregate_sources(data_directory='direktori_yang_tidak_ada/')
        self.assertEqual(len(sources), 0)

if __name__ == '__main__':
    unittest.main()
