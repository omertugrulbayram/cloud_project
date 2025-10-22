# ⚡ My First Serverless Function+

Bu proje, AWS Lambda ve API Gateway kullanılarak oluşturulmuş tamamen sunucusuz (serverless) bir uygulamadır.
Kullanıcı, API üzerinden “Hello” uç noktasına erişebilir ve basit bir HTML arayüzü ile bu verileri görebilir.

---

🧠 Proje Amacı

Modern bulut tabanlı uygulamaların sunucusuz mimari ile nasıl geliştirileceğini öğrenmek ve avantajlarını deneyimlemek.

Motivasyon:

Sunucusuz mimari sayesinde altyapı yönetimine odaklanmadan sadece iş mantığını geliştirebilirsiniz.

AWS Lambda ve API Gateway kullanımı pratikte deneyimlenir.

Basit bir web arayüzü ile fonksiyonun çıktısını görselleştirmek.

🧩 Proje Hakkında

Proje iki ana bileşenden oluşuyor:

1️⃣ Backend (API Katmanı)

AWS Lambda fonksiyonları ile yazılmıştır.

API Gateway üzerinden /hello uç noktası açılmıştır.

Fonksiyonlar Python ortamında çalışmaktadır.

Örnek uç noktalar:

GET /hello → {"message": "Hello, World!"}

GET /hello?name=Omer → {"message": "Hello, Omer!"}

POST /square → JSON: {"n":5} → {"n":5,"square":25}

2️⃣ Frontend (Basit HTML/JS Arayüzü)

Statik olarak Lambda veya herhangi bir S3/host üzerinde çalıştırılabilir.

API uç noktalarıyla etkileşim kurar ve kullanıcıya mesaj veya hesaplama sonuçlarını gösterir.

🔧 Teknoloji Yığını
Katman	Teknolojiler
Backend	AWS Lambda, API Gateway, Python
Frontend	HTML, CSS, JavaScript
Deployment	AWS SAM CLI
🌟 Özellikler

Sunucusuz Mimari: AWS üzerinde, yönetilmesi gereken sunucu yok.

Hızlı Dağıtım: SAM CLI ile tek komutla deploy edilebilir.

API Entegrasyonu: Frontend, Lambda fonksiyonlarının API uç noktalarıyla doğrudan iletişim kurar.

Cloud Logging: CloudWatch ile fonksiyon logları takip edilebilir.

Esnek Geliştirme: GET ve POST taleplerini destekler, parametre alıp işlem yapabilir.

🚀 Kurulum ve Çalıştırma

SAM CLI ve AWS CLI kurulu olmalı. AWS IAM kullanıcı bilgilerinizi girin:

aws configure


Projeyi deploy etmek için:

git clone https://github.com/kullanici/my-first-serverless.git
cd my-first-serverless
sam build
sam deploy --guided


Deploy tamamlandıktan sonra API URL’ini terminalde göreceksiniz ve tarayıcıdan test edebilirsiniz.

🎬 Deneme

GET /hello → varsayılan mesaj

GET /hello?name=Omer → kişiselleştirilmiş mesaj

POST /square → JSON üzerinden sayının karesi

Frontend ile tüm çıktılar tarayıcıdan görüntülenebilir.
