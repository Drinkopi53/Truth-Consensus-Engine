import sys
import os

# Tambahkan direktori 'src' ke Python path untuk memungkinkan impor modul kita
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

try:
    from data_aggregator import aggregate_sources
    from analysis_engine import analyze_sources
except ImportError as e:
    print(f"Gagal mengimpor modul yang diperlukan: {e}")
    print("Pastikan Anda menjalankan skrip dari direktori root proyek dan direktori 'src' ada.")
    sys.exit(1)

def display_results(consensus, conflicting):
    """Memformat dan menampilkan hasil analisis."""
    print("\n" + "="*60)
    print("       HASIL ANALISIS MESIN KONSENSUS KEBENARAN")
    print("="*60)

    print("\n--- FAKTA KONSENSUS ---")
    print("Klaim-klaim berikut didukung secara luas di berbagai sumber.")
    if consensus:
        consensus.sort(key=lambda x: x['source_count'], reverse=True)
        for i, item in enumerate(consensus, 1):
            print(f"{i}. ({item['source_count']} sumber): {item['claim']}")
    else:
        print(" -> Tidak ada fakta konsensus yang kuat ditemukan (didukung oleh <60% sumber).")

    print("\n--- KLAIM BERTENTANGAN / BELUM DIVERIFIKASI ---")
    print("Klaim-klaim berikut ditemukan di lebih sedikit sumber atau hanya satu sumber.")
    if conflicting:
        conflicting.sort(key=lambda x: x['source_count'], reverse=True)
        for i, item in enumerate(conflicting, 1):
            print(f"{i}. ({item['source_count']} sumber): {item['claim']}")
    else:
        print(" -> Tidak ada klaim yang bertentangan yang ditemukan.")

    print("\n" + "="*60)

def main():
    """Fungsi utama untuk menjalankan Mesin Konsensus Kebenaran."""
    print("Memulai Mesin Konsensus Kebenaran...")

    # Untuk MVP, kita menganalisis satu set sumber yang telah ditentukan di direktori 'data'
    print("\nLangkah 1: Mengumpulkan informasi dari sumber data...")
    sources_data = aggregate_sources()

    if not sources_data:
        print("\n[ERROR] Tidak dapat menemukan sumber data di direktori 'data/'. Proses dibatalkan.")
        return

    print(f" -> Berhasil mengumpulkan data dari {len(sources_data)} sumber.")

    print("\nLangkah 2: Menganalisis data untuk menemukan konsensus...")
    consensus_claims, conflicting_claims = analyze_sources(sources_data)
    print(" -> Analisis selesai.")

    # Langkah 3: Menampilkan hasil
    display_results(consensus_claims, conflicting_claims)

if __name__ == '__main__':
    main()
