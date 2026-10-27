# Kartlık PWA

Kartlık, AnkiDroid'den bağımsız bir iPhone web uygulamasıdır. AnkiDroid'in Android arayüzünü kullanmaz; APKG paketini yerelde açar. Paket içindeki ZIP, SQLite, Zstandard ve medya verilerini cihazda işler. İlk ziyaret ve çevrimdışı dosyaların önbelleğe alınması dışında uygulama hesap, sunucu veya ağ bağlantısı kullanmaz.

## iPhone'a kurma

PWA kurulumu için ilk açılışta HTTPS adresi gerekir. Bu klasörü GitHub Pages, Cloudflare Pages veya başka bir statik HTTPS sunucusunda yayımlayın; iPhone Safari ile adresi bir kez açıp yüklemenin tamamlanmasını bekleyin. Sonra **Paylaş → Ana Ekrana Ekle** seçin. Dosyalar, SQLite WebAssembly dosyası da dahil, ilk açılışta önbelleğe alınır. Bundan sonra uygulama çevrimdışı açılabilir. iOS'ta `.html` dosyasını Dosyalar'dan açmak, PWA kurulumunun yerini tutmaz.

## APKG içe aktarma

1. Anki'den `.apkg` destesini dışa aktarın.
2. iPhone'da uygulamayı açın; Dosyalar'a kaydedilmiş paketi seçmek için **Ayarlar → Anki APKG içe aktar**'a dokunun. Mail veya AirDrop'tan gelen paketi önce Dosyalar'a kaydetmek gerekebilir.
3. İçe aktarma cihazda yapılır. Deste, HTML kart yüzleri ve paketteki görsel/ses dosyaları yerel depoya kaydedilir.

Legacy `.anki2` / `.anki21` ve modern `.anki21b` (Zstandard) veritabanları desteklenir. Paket çalışma bilgisi içeriyorsa yeni, öğrenme, tekrar, aralık, kolaylık, askı ve kardeş kart erteleme durumlarını alır. Günlük yeni/tekrar sınırları, özelleştirilebilir öğrenme adımları, tekrar döngüsü, ipucu, kart tarayıcısı, düzenleme, arama, deste yönetimi, istatistikler ve geri alma bulunur. Öğrenme kartları için Tekrar/Zor/İyi/Kolay ve kısa zaman aralıkları; tekrar kartları için aralık ve kolaylık katsayılı SM-2 benzeri yerel planlama kullanılır. Bu planlayıcı Anki’nin FSRS algoritmasıyla birebir aynı değildir. Anki kart şablonlarının yaygın alan ve cloze işaretlemeleri görüntülenir; tüm Anki filtreleri, gelişmiş koşullar, eklentiler ve özel JavaScript birebir çalışmayabilir. Ayarlar sekmesinden yeni kartın ön yüzünü ve isteğe bağlı cevabı telefonun yerleşik konuşma sesiyle okutabilirsiniz; okuma hızı da ayarlanır. Türkçe sistem sesi yoksa telefonun varsayılan sesi kullanılır. Ses sentezi cihazda çalışır, metin bir servise gönderilmez. Soru yüzünde bir kelimeye dokununca yalnızca o kelime telefonun seçili sesiyle okunur. Otomatik kart okuma varsayılan olarak kapalıdır; dil otomatik algılanır ve ayarlardan değiştirilebilir. AnkiWeb senkronizasyonu yoktur.

## Yedek ve depolama

Ayarlar sekmesinden tam `.kartlik` yedeği (kartlar, ilerleme ve medya) veya yalnızca metin içeren CSV yedeği indirebilirsiniz. APKG dosyanızı ayrıca saklayın. Kartlar ve medya iPhone'un bu siteye ait yerel depolamasında kalır; Safari site verilerini silmek bu yerel kopyayı kaldırabilir.

## Dahil edilen açık kaynak kütüphaneler

- sql.js 1.13.0 — SQLite WebAssembly, MIT lisansı
- fflate 0.8.2 — ZIP okuma, MIT lisansı
- fzstd 0.1.1 — Zstandard açma, MIT lisansı

Lisans metinleri `libs/` içindedir. Uygulama hiçbir üçüncü taraf sunucudan çalışma anında kod indirmez.
