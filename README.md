# telespam
Spam Scammer Bot Telegram

## Cara Pakenya Gimana?
- Buka file ``target.json`` atau ``target.txt``
- Masukan list ``token`` dan ``chat_id`` target mu kedalam filenya
- Jalankan file ``python bot.py``
  
<br>

<br>

ubah bagian <br>
``timeout`` jika ingin mengabaikan bot yang kena too many request jika lebih dari X detik <br>
``looping`` Seberapa banyak mengirim pesan kepada target <br>
``TargetList`` Lokasi file yang berisi token telegram target bisa format ``.txt`` atau ``.json``<br>

``isWordlist`` Apakah ingin menggunakan wordlist untuk spamming atau tidak, set ``True`` jika iya atau ``False`` jika tidak. jika menggunakan ``False`` maka bot akan mengirimkan satu pesan, kemudian bot akan dilogout. <br>
``WordList`` Lokasi file yang berisi wordlist/kalimat yang akan dispam, bisa format ``.txt`` atau ``.json`` <br>
``WordSingle`` Pesan yang akan dikirim, jika ``isWordlist`` diset ``False`` maka akan mengirimkan pesan ini satu kali, kemudian bot akan dilogout dan tidak bisa digunakan lagi<br>

``isFirstMessage`` Jika ingin mengirimkan pesan pertama kali sebelum melakukan spamming, set ``True`` jika iya atau ``False`` jika tidak.<br>
``isFirstMessageImage`` Apakah pesan pertama berupa gambar atau hanya text biasa, set ``True`` jika gambar atau ``False`` jika text biasa.<br>
``firstMessage`` Pesan yang akan dikirim, jika ``isFirstMessageImage`` diset ``False`` maka hanya akan mengirimkan pesan ini saja<br>
``firstMessageImage`` URL gambar untuk pesan yang akan dikirimkan, jika ``isFirstMessageImage`` diset ``True`` maka akan mengirimkan gambar ini dan pesan<br>
``isPinMessage`` Jika ingin Pin pesan yang pertama kali dikirim, set ``True`` jika iya atau ``False`` jika tidak.<br>
``isUnpinAll`` Jika ingin Unpin semua pesan yang pernah diPin sebelumnya, jadi hanya pesan yang pertama kali dikirim tadi yang diPin, set ``True`` jika iya atau ``False`` jika tidak.<br>

``isUpdateBot`` Apakah ingin mengubah settingan bot, set ``True`` jika iya atau ``False`` jika tidak.<br>
``botNameSet`` Merubah nama akun Bot tersebut, jika ``isUpdateBot`` diset ``False`` maka tidak akan diubah<br>
``botDescSet`` Merubah Deskripsi Bot tersebut, jika ``isUpdateBot`` diset ``False`` maka tidak akan diubah<br>
``botShortDescSet`` Merubah Deskripsi Singkat Bot tersebut, jika ``isUpdateBot`` diset ``False`` maka tidak akan diubah<br>

``isMarkup`` Jika ingin mengirimkan pesan pertama kali sebelum melakukan spamming, set ``True`` jika iya atau ``False`` jika tidak.<br>
``botMarkup`` Tombol/Markup/CTAs yang akan muncul pada setiap pesan yang dikirim, jika ``isMarkup`` diset ``False`` maka tidak akan ada markupnya<br>

```python
# Config
TargetList = "target.json" 
timeout = 900 # Timeout 900 seconds = 15 minutes (60 seconds = 1 minutes, 3600 seconds = 1 hours)
looping = 10000

isWordlist = True 
WordList = "word.txt" 
WordSingle = "CONTOH PESAN YANG AKAN DIKIRIM" 

isFirstMessage = True 
isFirstMessageImage = True
firstMessage = "CONTOH PESAN YANG AKAN DIKIRIM"
firstMessageImage = 'https://i.imgur.com/sNiTqn1.png'
isPinMessage = True 
isUnpinAll = False 

isUpdateBot = True 
botNameSet = 'Spammed by @xTwnk'
botDescSet = 'Bxot ini Telah Terkena Spamming oleh @xTwnk silahkan hubungi saya untuk menghentikan'
botShortDescSet = 'Bxot ini Telah Terkena Spamming oleh @xTwnk'

isMarkup = True 
botMarkup = '{"inline_keyboard": [[{ "text": "Hubungi Saya Untuk Menghentikan Spam", "url": "https://t.me/xTwnk" }]]}'
```

<br>

pada bagian <br>
``text`` juga bisa kamu tambahkan atau ubah sendiri sesuai kemauanmu <br>
```python
def worker(taskId, tokenInfo): # Line 168
    ...
    if isWordlist == True: # Line 203
                text = f"{random.choice(wordlistData)}\n\n\n【 💀 𝐇𝐔𝐁𝐔𝐍𝐆𝐈 𝐒𝐀𝐘𝐀 𝐉𝐈𝐊𝐀 𝐈𝐍𝐆𝐈𝐍 𝐃𝐈𝐇𝐄𝐍𝐓𝐈𝐊𝐀𝐍 𝐒𝐏𝐀𝐌𝐍𝐘𝐀 💀 】"
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
## Contoh word.txt
text dipisah menggunakan baris baru/new line
```text
Astaga ini apa yah?? Pantesan anak saya kok suka sekali mainan Discord sampe lupa waktu, Ternyata setelah saya periksa hp nya saat anak saya tidur dan isi nya ya allah kok banyak foto kartun telanjang. Ini adik adik umur berapa tahun kok udah ngirim kartun telanjang, kalo masih kecil jangan suka nonton video porno. Grup apaan nih anak saya, anak saya selalu bermain handphone dari pagi hingga larut malam!, saat anak saya tertidur saya melihat grup ini dan saya tidak sangka banyak sekali gambar porno , anak saya sudah bergaul dengan anak anak yang tidak benar! Saya akan laporkan kalian ke polisi!
Mengapa tuhan menciptakan sesuatu yang begitu sempurna? Sesuatu yang sangat menggoda iman? Mereka pasti tertawa setelah melihat tulisan ku ini (membayangkan betapa cabulnya diriku) tapi jujur, aku hanya tidak bisa menahan diriku lagi
GW BENAR-BENAR PENGEN JILATI KAKI NAMA WAIFU. GW PENGEN BANGET MENJILAT SETIAP BAGIAN KAKINYA SAMPAI AIR LIUR GW BERCUCURAN KAYAK AIR KERINGAT LALU NGENOD DENGANNYA SETIAP HARI SAMPAI TUBUH KITA MATI RASA YA TUHAN. GW INGIN MEMBUAT ANAK-ANAK DENGAN NAMA WAIFU SEBANYAK SATU TIM SEPAK BOLA DAN MEMBUAT SATU TIM SEPAK BOLA LAINNYA UNTUK MELAWAN ANAK-ANAK TIM SEPAK BOLA PERTAMA GW YANG GW BUAT SAMA NAMA WAIFU. GW PENGEN MASUK KE SETIAP LUBANG TUBUHNYA, MAU ITU LUBANG HIDUNG, LUBANG TELINGA, RONGGA MATA MAUPUN PUSAR, KECUALI PORI-PORI KULIT. KEMUDIAN GW AKAN MENJADIKANNYA MANUSIA YANG TIDAK BISA HIDUP KALO TIDAK GW KENTOG SETIAP HARI. DAN KALAU GUA DISEPONG GUA RELA KONTL GUA PUTUS.
ANJING NUNGGING GA LU, NUNGGING SEKARANG!!! GUA DAH GAK TAHAN, LO POKOKNYA HARUS NUNGGING ANJING PLEASE LO  APA SETIAP HARINYA LIAT LU SLIWAR SLIWER, GUA NGACENG BANGSATTTT LU PAHAM GA SIH SELAMA INI GUA PENGEN LIAT ELU POSTUR NUNGGING, TAU GAK GUA SELALU NAHAN HORNY, DI KANTOR , DI WARUNG, DI RUMAH CUMA PENGEN PUAS PUASIN HASRAT GUA BUAT LIAT ELU NUNGGING PLIS SEKALI AJA PLIS, GAPEDULI DILUAR SANA APA YANG TERJADI, ELO NUNGGING GUA UDAH SENENG BANGSAT ANJING LU KUDU PAHAM GUA GA SUDI KEHILANGAN ELU, LU HARUS SETIDAKNYA NUNGGING DAN MEMBEKAS DI MEMORI INDAH GUA PLIS DEH GW MINTA SEGENAP HATI GW AGAR LU NUNGGING
BUKA BAJU NAMA WAIFU LANGSUNG CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROTCEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROTCEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CEPLOK CROT CEPLOK CEPLOK CEPLOK CEPLOK CROT MONNCROOOTOOOOOOOOOOOOOOOOOOOOOOO
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
## Contoh target.txt
target dipisah menggunakan garis baru/new line. kemudian token dan id dipisah menggunakan ``|``
```text
69696969:Axsadfw243fszcz-xade456y65|6094206969
69696969:Axsadfw243fszcz-xade456y65|6094206969
69696969:Axsadfw243fszcz-xade456y65|6094206969
```
