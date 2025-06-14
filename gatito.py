import requests
import webbrowser

url = "https://api.thecatapi.com/v1/images/search"

try:
    response = requests.get(url)
    response.raise_for_status()  # Lanza error si no funciona la petición

    data = response.json()
    cat_image_url = data[0]["url"]

    print("Aquí tienes un gatito aleatorio 🐱💕:")
    print(cat_image_url)

    # Abrir la imagen en el navegador
    webbrowser.open(cat_image_url)

except requests.exceptions.RequestException as e:
    print("Ocurrió un error al intentar obtener la imagen de gatito:", e)
