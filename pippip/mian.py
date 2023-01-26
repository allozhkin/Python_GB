from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *





app = ApplicationBuilder().token("5436221930:AAFwavmQ_kQHCYQswuoJo95_tG1pdZmESGc").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))


app.run_polling()