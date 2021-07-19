import telebot
from telebot import types
from collections import Counter

user_dict = {}
gejala = []
diagnosa = 0
cf = 0
bot = telebot.TeleBot('1875878204:AAEu4JNZN-jjMsi0nSKvQXce0-bEDGmHCO4')

class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None
        self.q1= None
        self.q2= None
        self.q3= None
        self.q4= None
        self.q5= None
        self.q6= None
        self.q7= None
        self.q8= None
        self.q9= None
        self.q10= None
        self.q11= None
        self.q12= None
        self.q13= None
        self.q14= None
        self.q15= None
        self.q16= None


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.chat.id
    name = message.chat.first_name
    msg = bot.reply_to(message, """\
Selamat datang, Ini merupakan bot Diagnosa Awal Penyakit Kista.\n 
""")
    bot.send_message(chat_id, 'Silahkan menjawab semua pertanyaan diagnosa berikut dengan yakin. Jawablah dengan menekan jawaban yang disediakan.')
    bot.send_message(chat_id, 'Kita mulai berkenalan dulu, Siapa Nama Anda?')
    print(name + ' is using your bot')
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        bot.reply_to(message, 'Haloo '+ name)
        msg = bot.reply_to(message, 'Berapakah umur anda? ')
        bot.register_next_step_handler(msg, process_age_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan name step')


def process_age_step(message):
    try:
        chat_id = message.chat.id
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Umur haruslah sebuah angka. Berapakah usia anda?')
            bot.register_next_step_handler(msg, process_age_step)
            return
        user = user_dict[chat_id]
        user.age = age
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Lanjut')
        msg = bot.reply_to(message, 'Silahkan tekan tombol lanjut untuk melanjutkan diagnosa', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q1_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan age step')

def process_q1_step(message):
    try:
        chat_id = message.chat.id
        sex = message.text
        user = user_dict[chat_id]
        user.sex = sex
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '1. Apakah mengalami menstruasi yg tidak teratur?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q2_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q1 step')


def process_q2_step(message):
    try:
        chat_id = message.chat.id
        q1 = message.text
        user = user_dict[chat_id]
        user.q1 = q1
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '2. Apakah anda merasa nyeri pada perut bagian bawah?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q3_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q2 step')

def process_q3_step(message):
    try:
        chat_id = message.chat.id
        q2 = message.text
        user = user_dict[chat_id]
        user.q2 = q2
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '3. Apakah perut anda berasa penuh?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q4_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q3 step')

def process_q4_step(message):
    try:
        chat_id = message.chat.id
        q3 = message.text
        user = user_dict[chat_id]
        user.q3 = q3
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '4. Apakah ada benjolan pada perut?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q5_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q4 step')


def process_q5_step(message):
    try:
        chat_id = message.chat.id
        q4 = message.text
        user = user_dict[chat_id]
        user.q4 = q4
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '5. Apakah tnyeri parah pada saat haid?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q6_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q5 step')

def process_q6_step(message):
    try:
        chat_id = message.chat.id
        q5 = message.text
        user = user_dict[chat_id]
        user.q5 = q5
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '6. Apakah berat badan anda menurun?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q7_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q6 step')


def process_q7_step(message):
    try:
        chat_id = message.chat.id
        q6 = message.text
        user = user_dict[chat_id]
        user.q6 = q6
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '7. Apakah anda merasa tidak sanggup mencerna?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q8_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q7 step')


def process_q8_step(message):
    try:
        chat_id = message.chat.id
        q7 = message.text
        user = user_dict[chat_id]
        user.q7 = q7
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '8. Menstruasi yg datang terlambat?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q9_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q8 step')


def process_q9_step(message):
    try:
        chat_id = message.chat.id
        q8 = message.text
        user = user_dict[chat_id]
        user.q8 = q8
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '9. Apakah rasa nyeri perut tiba-tiba muncul?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q10_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q9 step')


def process_q10_step(message):
    try:
        chat_id = message.chat.id
        q9 = message.text
        user = user_dict[chat_id]
        user.q9 = q9
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '10. Sering merasakan nyeri di punggung bawah?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q11_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q10 step')


def process_q11_step(message):
    try:
        chat_id = message.chat.id
        q10 = message.text
        user = user_dict[chat_id]
        user.q10 = q10
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '11. Apakah tubuh anda merasa lemas?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q12_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q11 step')


def process_q12_step(message):
    try:
        chat_id = message.chat.id
        q11 = message.text
        user = user_dict[chat_id]
        user.q11 = q11
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '12. Apakah anda sering muntah-muntah?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q13_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q12 step')


def process_q13_step(message):
    try:
        chat_id = message.chat.id
        q12 = message.text
        user = user_dict[chat_id]
        user.q12 = q12
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '13. Apakah anda mengalami nyeri saat berhubungan seksual?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q14_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q13 step')


def process_q14_step(message):
    try:
        chat_id = message.chat.id
        q13 = message.text
        user = user_dict[chat_id]
        user.q13 = q13
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '14. Apakah anda mengalami gangguan buang air besar atau kecil adanya darah pada urine atau tinja?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q15_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q14 step')


def process_q15_step(message):
    try:
        chat_id = message.chat.id
        q14 = message.text
        user = user_dict[chat_id]
        user.q14 = q14
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '15. Apakah pendarahan menstruasi berlebihan?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_q16_step)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q15 step')


def process_q16_step(message):
    try:
        chat_id = message.chat.id
        q15 = message.text
        user = user_dict[chat_id]
        user.q15 = q15
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Ya', 'Tidak')
        msg = bot.reply_to(message, '16. sulit punya anak dalam kurun waktu 1 tahun?', reply_markup=markup)
        bot.register_next_step_handler(msg, process_diagnosa)
    except Exception as e:
        bot.reply_to(message, 'Kesalahan q16 step')




def process_diagnosa(message):
    try:
        chat_id = message.chat.id
        q16 = message.text
        user = user_dict[chat_id]
        user.q16 = q16

        #Start of engine
        A = ['Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        B = ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        C = ['Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak']
        D = ['Tidak', 'Ya', 'Tidak', 'Tidak', 'Ya', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Tidak', 'Ya', 'Ya', 'Ya', 'Ya']
        

        gejala.extend((user.q1, user.q2, user.q3, user.q4, user.q5, user.q6, user.q7, user.q8, user.q9, user.q10, user.q11, user.q12, user.q13, user.q14, user.q15, user.q16))

        input_multiset = Counter(gejala)

        if gejala == A:
            diagnosa = 'Kistadenoma Ovarii Serosum'
            user.diagnosa = diagnosa
        elif gejala == B:
            diagnosa = 'Kistadenoma Ovarii Musinosum'
            user.diagnosa = diagnosa
        elif gejala == C:
            diagnosa = 'Kista Dermoid'
            user.diagnosa = diagnosa
        elif gejala == D:
            diagnosa = 'Kista Endometriosis'
            user.diagnosa = diagnosa
        else:
            diagnosa = 'Bukan Penyakit Kista'
            user.diagnosa = diagnosa
        #End of engine    
        
        if gejala != A & gejala != B & gejala != C & gejala != C:
            bot.send_message(chat_id, 'Halo ' + user.name + ',\nAnda tidak terdiagnosa penyakit kista. ' )
        else:
            bot.send_message(chat_id, 'Halo ' + user.name + ',\nBerikut ini hasil diagnosa awal anda adalah : ' )
            bot.send_message(chat_id, '\n Anda beresiko mengalami ' + diagnosa + '\n')
            bot.send_message(chat_id, 'Mohon melakukan diagnosa lebih lanjut ke Dokter untuk kepastian penyakit anda.' )
    except Exception as e:
        bot.reply_to(message, 'oooops diagnosa')


print('Bot is Running')
bot.polling()
