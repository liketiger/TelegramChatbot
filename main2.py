from telegram.ext import Updater, MessageHandler, Filters

from emoji import emojize



updater = Updater(token='985545259:AAF8vaxtq_M-Xw4R5KrFTDeSyn_T4QuA9dI')

dispatcher = updater.dispatcher

updater.start_polling()

checker = 1


def handler(bot, update):

  text = update.message.text

  chat_id = update.message.chat_id

  if '-help' in text:

   bot.send_message(chat_id=chat_id, text='-date of wishcourse-subject enrollment / -wishcourse-subject enrollment notification date / -subject cart function available date / -date of course enrollment / -course enrollment correction date / -menu of lunch in school diner / -operating hour of the library / -location of the library / -operating hour of school diner / -first day of semester / final day of semester / -period of mid-term exam / -period of final exam')

  elif '-date of wishcourse-subject enrollment' in text:

    bot.send_message(chat_id=chat_id, text=emojize('It starts at 10:00AM on August 1 and ends at 12:00PM on August 6', use_aliases=True))

  elif '-wishcourse-subject enrollment notification date' in text:

    bot.send_message(chat_id=chat_id, text='You can check the result since 17:00 on August 14')

  elif '-location of the library' in text:

    bot.send_photo(chat_id=chat_id, photo=open('img/library.jpg', 'rb'))
      
  elif '-subject cart function available date' in text:

    bot.send_message(chat_id=chat_id, text='You can use subject cart function from August 14, 17:00 to August 8:00AM')

  elif '-date of course enrollment' in text:
      
    bot.send_message(chat_id=chat_id, text = 'Seniors - 8/16 10:00AM ~ 8/17 9:00AM, Juniors - 8/19 10:00AM ~ 8/20 9:00AM, Sophomores - 8/20 10:00AM ~ 8/21 9:00AM, Freshman - 8/21 10:00 ~ 8/22 9:00AM, new and transfer students - 8/26 10:00AM ~ 8/27 12:00PM')

  elif '-course enrollment correction date' in text:
      
    bot.send_message(chat_id=chat_id, text = 'Seniors - 9/8 18:30 ~ 9/9 12:00PM, Juniors - 9/8 19:30 ~ 9/9 12:00PM, Sophomores - 9/9 18:30 ~ 9/10 12:00PM, Freshman - 9/9 19:30 ~ 9/10 12:00, Every Students can correct courses between 9/10 18:30 ~ 9/11 12:00PM')

  elif '-menu of lunch in school diner' in text:
      
    bot.send_message(chat_id=chat_id, text = '1. Ramyun(Korean spicy noodle) + Rice 2. Spaghetti + Bread 3. Burrito + Soda')

  elif '-operating hour of the library' in text:
      
    bot.send_message(chat_id=chat_id, text = 'Weekdays - 9:00 ~ 22:00, Saturday - 9:00 ~ 15:00, During Vacation = Weekdays - 9:00 ~ 19:00, Saturday - 9:00 ~ 13:00')

  elif '-operating hour of school diner' in text:
      
    bot.send_message(chat_id=chat_id, text = 'Breakfast - 7:00 ~ 9:00, Lunch - 10:30 ~ 14:20, Dinner 17:00 ~ 19:30')

  elif '-first day of semester' in text:
      
    bot.send_message(chat_id=chat_id, text = 'It starts on September 2')

  elif '-final day of semester' in text:
      
    bot.send_message(chat_id=chat_id, text = 'It ends on December 23')

  elif '-period of mid-term exam' in text:
      
    bot.send_message(chat_id=chat_id, text = 'October 21 ~ October 25')

  elif '-period of final exam' in text:
      
    bot.send_message(chat_id=chat_id, text = 'December 16 ~ December 20')

  elif '헬프' in text:
    
    bot.send_message(chat_id=chat_id, text = '수강희망과목 등록 날짜 / 수강 희망과목 신청 결과 날짜 / 과목 담아두기 가능 날짜 / 수강신청 날짜 / 수강신청정정 날짜 / 오늘 점심 학식 메뉴 / 도서관 자료실 이용시간 / 도서관 위치 / 식당 운영 시간 / 개강일 / 종강일 / 중간고사 기간 / 기말고사 기간')

  elif '수강희망과목 등록 날짜' in text:
    
    bot.send_message(chat_id=chat_id, text = '8월 1일 10시부터 8월 6일 12시 까지')

  elif '수강 희망과목 신청 결과 날짜' in text:
    
    bot.send_message(chat_id=chat_id, text = '8월 14일 17:00')

  elif '과목 담아두기 가능 날짜' in text:
    
    bot.send_message(chat_id=chat_id, text = '8월 14일 17:00 부터 8월 16일 8:00 까지')

  elif '수강신청 날짜' in text:
    
    bot.send_message(chat_id=chat_id, text = '4학년은 8월 16일 10:00 - 8월 17일 9:00 / 3학년은 8월 19일 10:00 - 8월 20일 9:00 / 2학년은 8월 20일 10:00 - 8월 21일 9:00 / 1학년은 8월 21일 10:00 - 8월 22일 9:00 / 신입생, 편입생은 8월 26일 10:00 - 8월 27 12:00 ')

  elif '수강신청정정 날짜' in text:
    
    bot.send_message(chat_id=chat_id, text = '4학년은 9월 8일 18:30 - 9월 9일 12:00 / 3학년은 9월 8일 19:30 - 9월 9일 12:00 / 2학년은 9월 9일 18:30 - 9월 10일 12:00 / 1학년은 9월 9일 19:30 - 9월 10일 12:00 / 전체는 9월 10일 18:30 - 9월 11일 12:00 ')

  elif '오늘 점심 학식 메뉴' in text:
    
    bot.send_message(chat_id=chat_id, text = '1. 라면 + 공기밥 2. 스파게티 + 빵 3. 브리또 + 탄산음료 ')

  elif '도서관 자료실 이용시간' in text:
    
    bot.send_message(chat_id=chat_id, text = '평일은 9:00 - 22:00 / 토요일은 9:00 - 15:00 / 방학기간에는 평일은 9:00 - 19:00 / 토요일은 9:00 - 13:00 ')

  elif '도서관 위치' in text:
    
    bot.send_photo(chat_id=chat_id, photo=open('img/library.jpg', 'rb'))

  elif '식당 운영 시간' in text:
    
    bot.send_message(chat_id=chat_id, text = '아침은 7:00 - 9:00 / 점심은 10:30 - 14:20 / 저녁은 17:00 - 19:30')

  elif '개강일' in text:
    
    bot.send_message(chat_id=chat_id, text = '2019년 9월 2일')

  elif '종강일' in text:
    
    bot.send_message(chat_id=chat_id, text = '2019년 12월 23일')

  elif '중간고사 기간' in text:
    
    bot.send_message(chat_id=chat_id, text = '2019년 10월 21일 - 25일')

  elif '기말고사 기간' in text:
    
    bot.send_message(chat_id=chat_id, text = '2019년 12월 16일 - 20일')

  else:

    bot.send_message(chat_id=chat_id, text='Enter -help to see command lines / 명령어를 보시려면 헬프를 치세요')


echo_handler = MessageHandler(Filters.text, handler)

dispatcher.add_handler(echo_handler)