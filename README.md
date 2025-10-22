# cloud_project
My First Serverless Function TSGK Project

Bu proje, AWS Lambda + API Gateway kullanılarak oluşturulmuş basit ama fonksiyonel bir sunucusuz (serverless) uygulamadır.
Kullanıcılar /hello API uç noktasına erişip isimlerini vererek selam alabilir, ayrıca POST isteği ile sayıların karesini hesaplayabilir.

Neden Bu Proje?

Amaç, modern bulut ortamında sunucusuz mimariyi deneyimlemek ve hızlıca çalışan bir API geliştirmektir.
Sunucusuz yapılar sayesinde altyapı yönetimiyle uğraşmadan sadece iş mantığına odaklanabiliyoruz.

Motivasyon:

AWS servislerini öğrenmek: Lambda, API Gateway, CloudWatch

Sunucusuz mimarinin hız ve ölçeklenebilirliğini görmek

Basit bir CI/CD akışı ile deploy sürecini anlamak

Proje Yapısı
Backend

Lambda fonksiyonu Python ile yazıldı.

/hello uç noktası GET ve POST desteğine sahip:

GET /hello?name=Omer → {"message": "Hello, Omer!"}

POST /hello JSON: {"n":5} → {"n":5,"square":25}

CloudWatch logları ile tüm çağrılar izlenebilir.

Frontend (Opsiyonel)

Basit bir HTML + CSS + JS arayüzü ile API sonuçları gösterilebilir.

Statik olarak S3 üzerinden yayınlanabilir.

Kullanılan Teknolojiler

Katman	Teknolojiler
Backend	AWS Lambda, API Gateway, Python
Logging	AWS CloudWatch
Frontend	HTML, CSS, JavaScript (opsiyonel)
Deployment	AWS SAM CLI, S3

Öne Çıkan Özellikler

Sunucusuz: Sunucu yönetimine gerek yok, AWS her şeyi hallediyor.

Hızlı: Kod değişikliği → sam deploy ile anında yayında.

İzlenebilir: CloudWatch logları sayesinde API çağrıları takip edilebilir.

Kolay test: GET ve POST ile kolayca test edilebilir.

🧭 Kurulum ve Deploy

1️⃣ AWS CLI ile IAM kullanıcı bilgilerinizi girin:

aws configure


2️⃣ Depoyu klonlayın ve SAM ile deploy edin:

git clone https://github.com/kullanici/my-first-serverless.git
cd my-first-serverless
sam build
sam deploy --guided


3️⃣ Test etmek için tarayıcı veya Postman kullanabilirsiniz:

GET  https://<api-id>.execute-api.<region>.amazonaws.com/Prod/hello?name=Omer
POST https://<api-id>.execute-api.<region>.amazonaws.com/Prod/hello
Body: {"n":5}

💡 Notlar ve Öğrendiklerim

Serverless mimari ile altyapı derdi yok, sadece iş mantığına odaklanıyorsunuz.

En büyük zorluk: event objesini doğru parse etmek ve GET/POST mantığını düzgün ayırmak.

Bu yaklaşım özellikle hızlı prototipler, microservices ve küçük API servisleri için ideal.
