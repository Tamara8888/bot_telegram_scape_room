from telegram import Update, InputMediaPhoto, InputMediaAudio
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Diccionario con los textos del escape room
TEXTS = {
    "start": {
        "intro": "¡Bienvenida a tu regalo de cumpleaños! Te he preparado un Escape Room ambientado en Resident Evil. Tienes que ir completando las misiones para desvelar el regalo final. ¡Suerte!",
        "image": "https://drive.google.com/uc?export=view&id=1SRe5ZRZi3ZRWiCvGnuYot85Znkt57EZc",
        "first_hint": "Tu primera pista: 'Un virus ha infectado Raccoon City. La solución está en un código. Recuerda el número que viste en la comisaría... ¿Te suena 617?'",
        "next_hint": "Envía /pista1 para continuar con la próxima pista."
    },
    "pista1": {
        "intro": "Introduce el código para salir de la comisería.",
        "audio": "https://link_a_tu_audio_de_tension.mp3",
        "hint": "Ahora, resuelve este acertijo para avanzar. ¿Qué número de código aparece repetidamente en las puertas de seguridad en *Resident Evil*?",
        "answer": "Respuesta: El código es 617. Escribe '617' para avanzar a la siguiente pista."
    },
    "pista2": {
        "incorrect": "¡Ups! El código no es correcto. Intenta de nuevo.",
        "correct": "¡Código correcto! Has desbloqueado la puerta. Ahora, te enfrentas a un nuevo desafío.",
        "image": "https://link_a_tu_imagen_laboratorio.jpg",
        "hint": "Te encuentras en un laboratorio. Allí hay un candado con una combinación de letras. El mensaje dice: 'LA CURA ESTÁ EN EL PASADO'.",
        "next_hint": "Descifra el mensaje y escribe la respuesta de 3 letras. Escribe /pista3 cuando creas que tienes la respuesta."
    },
    "pista3": {
        "correct": "¡Excelente! Has resuelto el acertijo. La combinación es 'ABC'. Ahora avanzas al siguiente nivel.",
        "audio": "https://link_a_tu_audio_de_suspenso.mp3",
        "hint": "En este nivel, debes encontrar la clave secreta. El virus T tiene una relación con algo que se encuentra en la estación de policía.",
        "next_hint": "Busca en las imágenes que te voy a enviar y responde correctamente. ¿Cuál es el nombre del protagonista de la saga que no ha sido infectado? Envía /pista4 para la próxima pista."
    },
    "pista4": {
        "incorrect": "¡No es correcto! Intenta otra vez.",
        "correct": "¡Correcto! El protagonista es Leon S. Kennedy. Ahora, eres más cerca de la salida.",
        "image": "https://link_a_tu_imagen_de_leon.jpg",
        "hint": "La próxima pista está relacionada con una famosa frase del juego. 'Todo es parte del plan.' ¿Qué significa esto?",
        "next_hint": "Envía /pista5 para continuar."
    },
    "pista5": {
        "incorrect": "La respuesta no es correcta. Vuelve a intentarlo.",
        "correct": "¡Lo lograste! 'Todo es parte del plan' era la clave. Ahora, te acercas al final de tu Escape Room.",
        "audio": "https://link_a_tu_audio_de_victoria.mp3",
        "final_hint": "Ahora busca la carta de papiroflexia con la clave final escondida en tu casa. Está con un mensaje muy especial: 'Te amo'.",
        "nfc_hint": "Escanea el NFC para completar el Escape Room y obtener tu recompensa final."
    }
}

# Función para iniciar el escape room
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(TEXTS["start"]["intro"])
    await update.message.reply_photo(photo=TEXTS["start"]["image"])
    await update.message.reply_text(TEXTS["start"]["first_hint"])
    await update.message.reply_text(TEXTS["start"]["next_hint"])

# Función para la primera pista
async def pista1(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(TEXTS["pista1"]["intro"])
    await update.message.reply_audio(audio=TEXTS["pista1"]["audio"])
    await update.message.reply_text(TEXTS["pista1"]["hint"])
    await update.message.reply_text(TEXTS["pista1"]["answer"])

# Función para la segunda pista
async def pista2(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response == '617':
        await update.message.reply_text(TEXTS["pista2"]["correct"])
        await update.message.reply_photo(photo=TEXTS["pista2"]["image"])
        await update.message.reply_text(TEXTS["pista2"]["hint"])
        await update.message.reply_text(TEXTS["pista2"]["next_hint"])
    else:
        await update.message.reply_text(TEXTS["pista2"]["incorrect"])

# Función para la tercera pista
async def pista3(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response.lower() == 'abc':
        await update.message.reply_text(TEXTS["pista3"]["correct"])
        await update.message.reply_audio(audio=TEXTS["pista3"]["audio"])
        await update.message.reply_text(TEXTS["pista3"]["hint"])
        await update.message.reply_text(TEXTS["pista3"]["next_hint"])
    else:
        await update.message.reply_text(TEXTS["pista3"]["incorrect"])

# Función para la cuarta pista
async def pista4(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response.lower() == 'leon':
        await update.message.reply_text(TEXTS["pista4"]["correct"])
        await update.message.reply_photo(photo=TEXTS["pista4"]["image"])
        await update.message.reply_text(TEXTS["pista4"]["hint"])
        await update.message.reply_text(TEXTS["pista4"]["next_hint"])
    else:
        await update.message.reply_text(TEXTS["pista4"]["incorrect"])

# Función para la quinta pista
async def pista5(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    if user_response.lower() == 'unplan':
        await update.message.reply_text(TEXTS["pista5"]["correct"])
        await update.message.reply_audio(audio=TEXTS["pista5"]["audio"])
        await update.message.reply_text(TEXTS["pista5"]["final_hint"])
        await update.message.reply_text(TEXTS["pista5"]["nfc_hint"])
    else:
        await update.message.reply_text(TEXTS["pista5"]["incorrect"])

# Función principal para manejar el bot
def main() -> None:
    # Crear la aplicación del bot con tu Token
    application = Application.builder().token('7920703839:AAF5-p5gDLlsqiG0R6VaftYOP-Zl2ijtroQ').build()

    # Agregar los manejadores de comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("pista1", pista1))
    application.add_handler(CommandHandler("pista2", pista2))
    application.add_handler(CommandHandler("pista3", pista3))
    application.add_handler(CommandHandler("pista4", pista4))
    application.add_handler(CommandHandler("pista5", pista5))

    # Manejador de texto (para que la respuesta del usuario sea procesada)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, pista2))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
