# Pertemuan 13 - Debugging dan Testing

**Nama:** Nurul Aisyah Wulan Dela P.  
**NIM:** 2225250087 
**Kelas:** 3F

## Kasus

Program yang diuji merupakan program pengolahan nilai mahasiswa menggunakan Python. Program memiliki tiga fungsi utama, yaitu menghitung rata-rata nilai, menentukan status kelulusan, dan mencari nilai tertinggi.

Pengujian dilakukan untuk menemukan kesalahan logika pada setiap fungsi agar program dapat menghasilkan output yang sesuai dengan hasil yang diharapkan.

## Test Case

Data yang digunakan: `[80, 60, 90, 70]`

| ID | Input | Expected | Actual Awal | Status |
|---|---|---|---|---|
| TC01 | `[80, 60, 90, 70]` (rata-rata) | 75 | 60 | Gagal |
| TC02 | `60` (status) | Lulus | Tidak lulus | Gagal |
| TC03 | `[80, 60, 90, 70]` (tertinggi) | 90 | 0 | Gagal |

## Bug Report

Ditemukan tiga kesalahan pada program:

1. **Fungsi hitung_rata_rata**
   - Gejala: Hasil rata-rata tidak sesuai.
   - Lokasi: `return sum(nilai) / 5`.
   - Akar penyebab: Pembagi menggunakan angka tetap 5, bukan jumlah data sebenarnya.
   - Perbaikan: Mengganti angka 5 dengan `len(nilai)` dan menambahkan penanganan list kosong.

2. **Fungsi status**
   - Gejala: Nilai 60 dinyatakan tidak lulus.
   - Lokasi: `if nilai > 60`.
   - Akar penyebab: Operator hanya menerima nilai yang lebih besar dari 60.
   - Perbaikan: Mengubah operator `>` menjadi `>=`.

3. **Fungsi nilai_tertinggi**
   - Gejala: Hasil nilai tertinggi adalah 0.
   - Lokasi: `if x < tertinggi`.
   - Akar penyebab: Operator pembanding terbalik sehingga nilai tertinggi tidak diperbarui.
   - Perbaikan: Mengubah operator `<` menjadi `>` dan menginisialisasi nilai tertinggi menggunakan `nilai[0]`.

## Retest

Setelah perbaikan dilakukan, seluruh pengujian dijalankan kembali.

| ID | Expected | Actual Setelah Perbaikan | Status |
|---|---|---|---|
| TC01 | 75 | 75.0 | Berhasil |
| TC02 | Lulus | Lulus | Berhasil |
| TC03 | 90 | 90 | Berhasil |

Hasil retest menunjukkan bahwa ketiga fungsi sudah berjalan sesuai dengan hasil yang diharapkan.

## Cara Menjalankan

Buka terminal pada VS Code, kemudian jalankan perintah:

```bash
python3 praktik/praktik_4_debugging.py
```

## Refleksi

Teknik debugging yang paling membantu adalah menggunakan test case dan breakpoint. Dengan test case, saya dapat membandingkan hasil yang diharapkan dengan hasil aktual sehingga lebih mudah menemukan kesalahan program.

Selain itu, breakpoint membantu saya mengamati perubahan nilai variabel saat program dijalankan. Dari latihan ini, saya belajar bahwa kesalahan kecil pada operator pembanding maupun pembagian dapat memengaruhi hasil akhir program. Oleh karena itu, pengujian perlu dilakukan dengan beberapa kondisi input agar program lebih akurat dan dapat diandalkan.