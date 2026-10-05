from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8966730515:AAFDtOt_u1cXh1JQdQQIIIojZH_laW9UEy0"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام چطوری میتونم کمکت کنم")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

def run_web_server():
    port = int(os.environ.get("PORT", 8080))
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Bot is running")
    HTTPServer(("0.0.0.0", port), Handler).serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

app.run_polling()
