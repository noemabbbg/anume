from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from dictant import Zugumomo
btnreturnmenu=InlineKeyboardButton(text='вернуться в меню↩️', callback_data='returnMenu')



clavaTOP = InlineKeyboardMarkup(row_width=1)




back=InlineKeyboardButton(text="вернуться↩️", callback_data="Back")
#clavaTOP.insert(GreenLight)
clavaTOP.insert(btnreturnmenu)

####28


clavaViborGenre=InlineKeyboardMarkup(row_width=1)
buy_pear1 = InlineKeyboardButton(text="Романтика", callback_data="Romantik")
buy_pear2 = InlineKeyboardButton(text="Экшн", callback_data="Ekhn")
buy_pear3 = InlineKeyboardButton(text="Триллер", callback_data="Triller")

buy_pear5 = InlineKeyboardButton(text="Драма", callback_data="Drama")



MHA=InlineKeyboardButton(text='Моя геройская академия(1)', callback_data='MHA')
Pharh=InlineKeyboardButton(text='Эта фарфоровая кукла влюбилась', callback_data='Pharh')
Zugumomo=InlineKeyboardButton(text='Цугумомо', callback_data='Zugumomo')
KRD=InlineKeyboardButton(text='Клинок, рассекающий демонов (1)', callback_data='KRD')
ehoTerrora=InlineKeyboardButton(text="Эхо террора(soon)", callback_data="ehoTerrora")
sharlotta=InlineKeyboardButton(text="Шарлотта(soon)", callback_data="sharlotta")
devochkaZayka=InlineKeyboardButton(text="Этот глупый свин не понимает мечту девочки-зайки(soon)", callback_data="devochkaZayka")
KRD2=InlineKeyboardButton(text='Клинок, рассекающий демонов (2) (soon)', callback_data='KRD2')
codeGeass=InlineKeyboardButton(text="Код Гиасс: Восстание Лелуша(1)(soon)", callback_data="codeGeass")
codeGeass2=InlineKeyboardButton(text="Код Гиас: Восставший Лелуш(2)(soon)", callback_data="codeGeass2")

clavaViborGenre.insert(buy_pear1)
clavaViborGenre.insert(buy_pear2)
clavaViborGenre.insert(buy_pear3)

clavaViborGenre.insert(buy_pear5)

clavaViborGenre.insert(btnreturnmenu)

ClavaDrama=InlineKeyboardMarkup(row_width=1)
ClavaDrama.insert(ehoTerrora)
ClavaDrama.insert(back)

Clavaromantik=InlineKeyboardMarkup(row_width=1)

Clavaromantik.insert(devochkaZayka)
Clavaromantik.insert(Pharh)
Clavaromantik.insert(Zugumomo)
Clavaromantik.insert(back)  



ClavaEkhn=InlineKeyboardMarkup(row_width=1)
ClavaEkhn.insert(KRD2)
ClavaEkhn.insert(codeGeass)
ClavaEkhn.insert(codeGeass2)
ClavaEkhn.insert(KRD)
ClavaEkhn.insert(Zugumomo)
ClavaEkhn.insert(MHA)
ClavaEkhn.insert(back)





clavaTriller=InlineKeyboardMarkup(row_width=1)
clavaTriller.insert(ehoTerrora)
clavaTriller.insert(back)


ClavaIsekai=InlineKeyboardMarkup(row_width=1)
ClavaIsekai.insert(back)






