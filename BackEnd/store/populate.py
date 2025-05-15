from store.models import Device

def run():
    if Device.objects.exists():
        print("Dispositivos já existem. Nenhum dado inserido.")
        return

    produtos = [
        {
            "name": "Camera",
            "price": 2999.99,
            "description": "Câmera com alta definição, ideal para criadores de conteúdo e monitoramento.",
            "image": "device_images/Camera.png"
        },
        {
            "name": "Celular iPhone",
            "price": 4299.90,
            "description": "Smartphone iPhone com ótimo desempenho e câmeras avançadas.",
            "image": "device_images/CeleularIphone.png"
        },
        {
            "name": "Celular Samsung",
            "price": 2499.90,
            "description": "Smartphone Samsung com Android, ideal para o dia a dia.",
            "image": "device_images/CelularSamsung.png"
        },
        {
            "name": "PS5",
            "price": 3899.00,
            "description": "Console de última geração com jogos imersivos e gráficos realistas.",
            "image": "device_images/PS5.png"
        },
        {
            "name": "TV Smart",
            "price": 1899.00,
            "description": "Smart TV com acesso à internet e aplicativos de streaming.",
            "image": "device_images/TvSmart.png"
        }
    ]

    for produto in produtos:
        Device.objects.create(**produto)

    print("Produtos inseridos com sucesso.")
