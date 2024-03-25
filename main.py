from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import asyncio

async def start(update, context):
    await update.message.reply_text('Bot telah aktif!')

async def send_message_to_groups(update, context):
    group_ids = ["@noraatest", "@ressnoraa"]
    with open("custom_message.txt", "r") as file:
        message = file.read().strip()  # Membaca isi file pesan.txt

    for group_id in group_ids:
        try:
            await context.bot.send_message(chat_id=group_id, text=message)
            print(f"Pesan berhasil dikirim ke grup {group_id}")

            # Kirim pesan balasan dengan informasi detail bahwa pesan sudah dikirim
            await update.message.reply_text(f"Pesan berhasil dikirim ke grup {group_id}.")
        except Exception as e:
            print(f"Gagal mengirim pesan ke grup {group_id}: {str(e)}")
            await update.message.reply_text(f"Gagal mengirim pesan ke grup {group_id}: {str(e)}")

async def loop_send_messages(context):
    while True:
        await asyncio.sleep(60)  # Ganti dengan interval waktu yang diinginkan, misalnya 3600 detik (1 jam)
        await send_message_to_groups(None, context)

        

if __name__ == '__main__':
    app = ApplicationBuilder().token("6853589780:AAFyHnjmhaKE-sKdOdFVvjZi_VY1S6ZeQXU").build()

    # Tambahkan handler untuk perintah /start
    app.add_handler(CommandHandler("start", start))

    # Tambahkan handler untuk perintah yang akan mengirim pesan ke grup-grup
    app.add_handler(CommandHandler("gas", send_message_to_groups))

    # Jalankan polling bot
    app.run_polling()

    # Mulai loop untuk mengirim pesan secara berkala
    loop = asyncio.get_event_loop()
    loop.create_task(loop_send_messages(app.dispatcher))
    loop.run_forever()
