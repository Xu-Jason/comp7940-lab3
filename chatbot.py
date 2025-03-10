import telegram
from telegram.ext import Updater, MessageHandler, Filters
import configparser
import logging


def main():
    # 读取配置文件，获取令牌并创建 Updater 对象
    config = configparser.ConfigParser()
    config.read('config.ini')
    updater = Updater(token=config['TELEGRAM']['ACCESS_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher

    # 配置日志记录，方便调试
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # 注册一个消息处理器，用于处理文本消息（非命令消息）
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # 启动机器人
    updater.start_polling()
    updater.idle()


def echo(update, context):
    # 将接收到的消息转换为大写并回复
    reply_message = update.message.text.upper()
    logging.info("Update:" + str(update))
    logging.info("context:" + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)


if __name__ == '__main__':
    main()