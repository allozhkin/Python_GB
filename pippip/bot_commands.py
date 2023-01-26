from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_command(update,context)
    await update.message.reply_text(f'Welcome {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_command(update,context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_command(update,context)
    await update.message.reply_text(f'/hello\n/time\n/help\n/sum')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_command(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')
