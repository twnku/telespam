# telespam
Spam Scammer Bot Telegram

## Cara Pakenya Gimana?
- Buka file ``target.json`` 
- Masukan list ``token`` dan ``chat_id`` target mu
- Jalankan file ``python bot.py``
  
<br>

<br>

ubah bagian <br>
``timeout`` jika ingin mengabaikan bot yang kena too many request jika lebih dari X detik <br>
``looping`` Seberapa banyak mengirim pesan kepada target <br>
```python
# Config
timeout = 900 
looping = 1000
```

<br>

pada bagian <br>
``text`` juga bisa kamu tambahkan atau ubah sendiri sesuai kemauanmu <br>
```python
def worker(task_id, token_info, sentences, stop_event, timeout, looping):
    ...
    for i in range(looping):
        # Text message for target
        text = f"{random.choice(sentences)}\n\n【 💀 𝐇𝐔𝐁𝐔𝐍𝐆𝐈 𝐒𝐀𝐘𝐀 𝐉𝐈𝐊𝐀 𝐈𝐍𝐆𝐈𝐍 𝐃𝐈𝐇𝐄𝐍𝐓𝐈𝐊𝐀𝐍 𝐒𝐏𝐀𝐌𝐍𝐘𝐀 💀 】 \n【 https://t.me/xTwnk 】 "
    ...
```
## Contoh word.json
```json
[
    "Astaga ini apa yah?? Pantesan anak saya kok suka sekali mainan Discord sampe lupa waktu, Ternyata setelah saya periksa hp nya saat anak saya tidur dan isi nya ya allah kok banyak foto kartun telanjang. Ini adik adik umur berapa tahun kok udah ngirim kartun telanjang, kalo masih kecil jangan suka nonton video porno. Grup apaan nih anak saya, anak saya selalu bermain handphone dari pagi hingga larut malam!, saat anak saya tertidur saya melihat grup ini dan saya tidak sangka banyak sekali gambar porno , anak saya sudah bergaul dengan anak anak yang tidak benar! Saya akan laporkan kalian ke polisi!",
    "Mengapa tuhan menciptakan sesuatu yang begitu sempurna? Sesuatu yang sangat menggoda iman? Mereka pasti tertawa setelah melihat tulisan ku ini (membayangkan betapa cabulnya diriku) tapi jujur, aku hanya tidak bisa menahan diriku lagi",
    "GW BENAR-BENAR PENGEN JILATI KAKI NAMA WAIFU. GW PENGEN BANGET MENJILAT SETIAP BAGIAN KAKINYA SAMPAI AIR LIUR GW BERCUCURAN KAYAK AIR KERINGAT LALU NGENOD DENGANNYA SETIAP HARI SAMPAI TUBUH KITA MATI RASA YA TUHAN. GW INGIN MEMBUAT ANAK-ANAK DENGAN NAMA WAIFU SEBANYAK SATU TIM SEPAK BOLA DAN MEMBUAT SATU TIM SEPAK BOLA LAINNYA UNTUK MELAWAN ANAK-ANAK TIM SEPAK BOLA PERTAMA GW YANG GW BUAT SAMA NAMA WAIFU. GW PENGEN MASUK KE SETIAP LUBANG TUBUHNYA, MAU ITU LUBANG HIDUNG, LUBANG TELINGA, RONGGA MATA MAUPUN PUSAR, KECUALI PORI-PORI KULIT. KEMUDIAN GW AKAN MENJADIKANNYA MANUSIA YANG TIDAK BISA HIDUP KALO TIDAK GW KENTOG SETIAP HARI. DAN KALAU GUA DISEPONG GUA RELA KONTL GUA PUTUS.",
    "ANJING NUNGGING GA LU, NUNGGING SEKARANG!!! GUA DAH GAK TAHAN, LO POKOKNYA HARUS NUNGGING ANJING PLEASE LO  APA SETIAP HARINYA LIAT LU SLIWAR SLIWER, GUA NGACENG BANGSATTTT LU PAHAM GA SIH SELAMA INI GUA PENGEN LIAT ELU POSTUR NUNGGING, TAU GAK GUA SELALU NAHAN HORNY, DI KANTOR , DI WARUNG, DI RUMAH CUMA PENGEN PUAS PUASIN HASRAT GUA BUAT LIAT ELU NUNGGING PLIS SEKALI AJA PLIS, GAPEDULI DILUAR SANA APA YANG TERJADI, ELO NUNGGING GUA UDAH SENENG BANGSAT ANJING LU KUDU PAHAM GUA GA SUDI KEHILANGAN ELU, LU HARUS SETIDAKNYA NUNGGING DAN MEMBEKAS DI MEMORI INDAH GUA PLIS DEH GW MINTA SEGENAP HATI GW AGAR LU NUNGGING",
    "BUKA BAJU NAMA WAIFU LANGSUNG CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROTCEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROTCEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT MONNCROOOTOOOOOOOOOOOOOOOOOOOOOOO"
]
```
## Contoh target.json
```json
[
    {
        "token": "69696969:Axsadfw243fszcz-xade456y65",
        "id": "6094206969"
    },
    {
        "token": "69696969:Axsadfw243fszcz-xade456y65",
        "id": "6094206969"
    },
    {
        "token": "69696969:Axsadfw243fszcz-xade456y65",
        "id": "6094206969"
    }
]
```
