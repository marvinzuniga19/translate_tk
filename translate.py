import tkinter as tk
from google.cloud import translate_v2 as translate

# Especificar la ruta absoluta al archivo JSON con la clave de API
creds_path = "/ruta/absoluta/a/tktanslatekey.json"

# Crear una instancia del cliente de la API de Google Translate
translate_client = translate.Client.from_service_account_json(creds_path)


def translate_text():
    try:
        # Obtener el texto introducido por el usuario
        text = input_text.get("1.0", "end-1c").strip()

        # Detectar el idioma del texto original
        detection = translate_client.detect_language(text)
        source_language = detection["language"]

        # Traducir el texto al español (es)
        translation = translate_client.translate(
            text, target_language="es", source_language=source_language
        )

        # Mostrar el resultado de la traducción en el cuadro de texto de salida
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translation["translatedText"])
    except Exception as e:
        print("Error al traducir el texto:", e)


# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Google Translate")

# Etiqueta y cuadro de texto para introducir el texto a traducir
input_label = tk.Label(root, text="Introduce el texto a traducir:")
input_label.pack()
input_text = tk.Text(root)
input_text.pack()

# Botón para iniciar la traducción
translate_button = tk.Button(root, text="Traducir", command=translate_text)
translate_button.pack()

# Etiqueta y cuadro de texto para mostrar el resultado de la traducción
output_label = tk.Label(root, text="Traducción:")
output_label.pack()
output_text = tk.Text(root)
output_text.pack()

# Iniciar el bucle de eventos de la interfaz gráfica
root.mainloop()
