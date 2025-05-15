from store.models import Device

def run():
    if Device.objects.exists():
        print("Dispositivos já existem. Nenhum dado inserido.")
        return

    produtos = [
        {
            "name": "Camera",
            "price": 2999.99,
            "description": "Camera com alta definição, ideal para criadores de conteúdo e segurança.",
            "image": "device_images/Camera.png"
        },
        {
            "name": "Celeulariphone",
            "price": 1499.90,
            "description": "Celeulariphone com alta definição, ideal para criadores de conteúdo.",
            "image": "device_images/CeleularIphone.png"
        },
        {
            "name": "Celularsamsung",
            "price": 1499.90,
            "description": "Celularsamsung com alta definição, ideal para criadores de conteúdo.",
            "image": "device_images/CelularSamsung.png"
        },
        {
            "name": "Ps5",
            "price": 1499.90,
            "description": "Ps5 com alta definição, ideal para criadores de conteúdo.",
            "image": "device_images/PS5.png"
        },
        {
            "name": "Tvsmart",
            "price": 1499.90,
            "description": "Tvsmart com alta definição, ideal para criadores de conteúdo.",
            "image": "device_images/TvSmart.png"
        }
    ]

    for produto in produtos:
        Device.objects.create(**produto)

    print("Produtos inseridos com sucesso.")
