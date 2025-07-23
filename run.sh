#!/bin/bash
pm2 start bot.py --name "downloader-bot"
pm2 save
pm2 logs
