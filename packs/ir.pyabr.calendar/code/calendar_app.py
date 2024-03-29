'''
    Pyabr OS

    Python Cloud Operating System Platform (c) 2021 PyFarsi. Free Software GNU General Public License v3.0

    - Informations

    * Name:             Pyabr
    * Founder:          Mani Jamali
    * Developers:       PyFarsi Community
    * Package Manager:  Paye, PyPI
    * License:          GNU General Publice License v3.0

    - Official Website

    * Persian Page:     https://pyabr.ir
    * English Page:     https://en.pyabr.ir
'''
import requests
from pyabr.core import *
from pyabr.quick import *
import json

jdata = '''{"1": {"1": "آغاز نوروز", "2": "آغاز عملیات فتح المبین", "3": "عید نوروز", "4": "عید نوروز", "5": null, "6": null, "7": "روز هنرهای نمایشی", "8": null, "9": null, "10": null, "11": "تقویم هجری شمسی به طور قانونی در ایران تصویب شده", "12": "روز جمهوری اسلامی ایران", "13": "روز طبیعت", "14": null, "15": "روز زخایر ژنتیکی و زیستی", "16": null, "17": null, "18": "روز سلامتی", "19": null, "20": "روز ملی فناوری هسته ای", "21": "شهادت امیر سپهبد علی صیاد شیرازی", "22": null, "23": null, "24": null, "25": "روز بزرگداشت عطار نیشابوری", "26": null, "27": null, "28": null, "29": "روز ارتش جمهوری اسلامی و نیروی زمینی", "30": null, "31": null}, "2": {"1": "روز بزرگداشت سعدی", "2": "سالروز اعلام انقلاب فرهنگی", "3": "روز بزرگداشت شیخ بهایی", "4": null, "5": "شکست حمله نظامی آمریکا به ایران در طبس", "6": null, "7": "روز ایمنی و حمل و نقل", "8": null, "9": "روز شوراها", "10": "روز ملی خلیج فارس", "11": "روز جهانی کار و کارگر", "12": "شهادت استاد مرتضی مطهری", "13": null, "14": null, "15": "روز بزرگداشت شیخ صدوق", "16": null, "17": null, "18": "روز بیماری های خاص و صعب العلاج", "19": "خروج نیروهای شوروی از ایران", "20": null, "21": null, "22": null, "23": null, "24": "لغو امتیاز تنباکو به فتوای آیت الله میرزا حسن شیرازی", "25": "روز بزرگداشت حکیم ابوالقاسم فردوسی و پاسداشت زبان فارسی", "26": null, "27": "روز ارتباطات و روابط عمومی", "28": "روز بزرگداشت حکیم عمر خیام", "29": null, "30": "روز ملی جمعیت", "31": " امضاء معاهده استانبول بین ایران و عثمانی و واگزاری سرزمین های قفقاز به دولت عثمانی به مدت چندین سال "}, "3": {"1": "روز بزرگداشت ملاصدرا", "2": null, "3": "فتح خرمشهر در عملیات بیت المقدس", "4": "روز دزفول - روز مقاومت و پایداری", "5": "روز حمایت از خانواده زندانیان", "6": null, "7": "افتتاح اولین دوره مجلس شورای اسلامی", "8": null, "9": null, "10": null, "11": null, "12": null, "13": null, "14": "رحلت امام خمینی(ره) بنیانگزار جمهوری اسلامی ایران", "15": "قیام 15 خرداد", "16": null, "17": null, "18": null, "19": null, "20": "روز صنایع دستی", "21": null, "22": null, "23": null, "24": null, "25": null, "26": null, "27": "روز جهاد کشاورزی", "28": null, "29": "درگذشت دکتر علی شریعتی", "30": null, "31": "شهادت دکتر مصطفی چمران"}, "4": {"1": "روز اصناف", "2": null, "3": null, "4": null, "5": null, "6": null, "7": "روز قوه قضاییه", "8": "روز مبارزه با سلاح های شیمیایی و میکروبی", "9": null, "10": "روز بزرگداشت صائب تبریزی", "11": "شهادت ایت الله صدوقی", "12": "حمله ناو آمریکایی به هواپیمای مسافربری جمهوری اسلامی", "13": null, "14": "روز شهرداری و دهیاری", "15": null, "16": "روز مالیات", "17": null, "18": "روز ادبیات کودکان و نوجوانان", "19": null, "20": null, "21": "روز فرهنگ پهلوانی و ورزش زورخانه ای", "22": null, "23": "گشایش اولین مجلس خبرگان رهبری", "24": null, "25": "روز بهزیستی و تأمین اجتماعی", "26": "سالروز تأسیس نهاد شورای نگهبان", "27": "اعلام پذیرش قطعنامه 598 شورای امنیت سازمان ملل از سوی ایران", "28": null, "29": null, "30": null, "31": null}, "5": {"1": null, "2": null, "3": null, "4": null, "5": "سالروز عملیات مرصاد", "6": "روز کارآفرینی و آموزش های فنی و حرفه ای", "7": null, "8": "روز بزرگداشت شیخ شهاب الدین سهروردی", "9": "روز اهدای خون", "10": null, "11": "شهادت آیت الله شیخ فضل الله نوری", "12": null, "13": null, "14": "صدور فرمان مشروطیت", "15": null, "16": "تشکیل جهاد دانشگاهی", "17": "روز خبرنگار", "18": null, "19": null, "20": null, "21": "روز حمایت از صنایع کوچک", "22": "روز تشکل ها و مشارکت های اجتماعی", "23": null, "24": null, "25": "جنگ های ایران و روسیه - حمله ایران به سرزمین های تازه اشغال شده توسط روس ها به منظور بازپس گیری این مناطق", "26": "آغاز بازگشت اسرای جنگی به ایران", "27": null, "28": "کودتای آمریکا برای بازگرداندن شاه", "29": null, "30": "روز بزرگداشت علامه مجلسی", "31": "روز صنعت دفاعی"}, "6": {"1": "روز بزرگداشت ابو علی سینا", "2": "آغاز هفته دولت", "3": "اشغال ایران توسط متفقین و فرار رضاخان", "4": "روز کارمند", "5": "روز بزرگداشت محمدبن زکریای رازی", "6": null, "7": null, "8": "انفجار دفتر نخست وزیری و شهادت رجایی و باهنر", "9": null, "10": "روز بانکداری اسلامی", "11": null, "12": "روز بهورز", "13": "امضاء معاهده گردان بین ایران و امپراطوری عثمانی ", "14": null, "15": "ورود پادشاه عثمانی به تبریز در پی اشغال شمال غربی ایران توسط عثمانی", "16": null, "17": "قیام 17 شهریور بر علیه حکومت پهلوی", "18": null, "19": "وفات آیت الله محمود طالقانی اولین امام جمعه تهران", "20": "نبرد کرتسانیسی بین آقامحمدخان قاجار و هراکلیوس دوم (حاکم گرجستان) و پیروزی آقا محمدخان و پیوستن دوباره منطقه قفقاز به ایران", "21": "امضاء معاهده سنت پترزبورگ بین ایران و روسیه", "22": null, "23": null, "24": null, "25": "روز خانواده و تکریم بازنشستگان", "26": "رسیدن نیروهای برتانیا و روسیه به یکدیگر در تهران در پی اشغال ایران در جنگ جهانی دوم", "27": "روز شعر و ادب فارسی", "28": null, "29": null, "30": "امضاء عهدنامه آخال میان ایران و امپراتوری روسیه", "31": "آغاز جنگ تحمیلی"}, "7": {"1": null, "2": null, "3": null, "4": null, "5": "شکست حصر آبادان در عملیات ثامن الائمه", "6": null, "7": "روز بزرگداشت شمس تبریزی", "8": "روز بزرگداشت مولوی", "9": "روز جهانی سالمندان", "10": "روز تجلیل از اسرا و مفقودان", "11": null, "12": null, "13": "روز نیروی انتظامی", "14": "روز دامپزشکی", "15": "روز روستا و عشایر", "16": null, "17": null, "18": null, "19": null, "20": "روز بزرگداشت حافظ", "21": null, "22": "روز جهانی استاندارد", "23": "روز جهانی نابینایان", "24": "روز پیوند اولیا و مربیان", "25": null, "26": "روز تربیت بدنی و ورزش", "27": null, "28": null, "29": "روز صادرات", "30": null}, "8": {"1": "روز آمار و برنامه ریزی", "2": " امضاء عهدنامه گلستان بین ایران و روسیه -  قفقاز ،ارمنستان و ایالت‌های شرقی گرجستان از ایران سلب و به روسیه واگذار شد", "3": null, "4": null, "5": "روز بزرگداشت سلمان فارسی", "6": null, "7": null, "8": "روز نوجوان و بسیج دانش آموزی", "9": null, "10": null, "11": null, "12": null, "13": "روز دانش آموز", "14": "روز فرهنگ عمومی", "15": null, "16": null, "17": null, "18": "روز کیفیت", "19": "روز جهانی علم در خدمت صلح و توسعه", "20": null, "21": null, "22": null, "23": null, "24": "روز کتاب، کتاب خوانی و کتابدار", "25": "روز وقف", "26": "سالروز آزادسازی سوسنگرد", "27": null, "28": null, "29": null, "30": null}, "9": {"1": null, "2": null, "3": null, "4": null, "5": "سالروز قیام مردم گرگان", "6": null, "7": "روز نیروی دریای", "8": null, "9": "روز بزرگداشت شیخ مفید", "10": "روز مجلس", "11": "شهادت میرزا کوچک خان جنگلی", "12": "روز قانون اساسی جمهوری اسلامی ایران (تصویب قانون اساسی جمهوری اسلامی ایران)", "13": "روز بیمه", "14": null, "15": null, "16": "روز دانشجو", "17": null, "18": "معرفی عراق به عنوان آغازگر جنگ از سوی سازمان ملل", "19": "تشکیل شورای فرهنگی به فرمان امام خمینی(ره)", "20": "ایران مناطق تحت کنترل حکومت ملی آذربایجان را باز پس گرفت", "21": null, "22": null, "23": null, "24": "تصرف مهاباد توسط ارتش ایران", "25": "روز پژوهش", "26": "روز حمل و نقل و رانندگان", "27": "روز جهان عاری از خشونت و افراطی گری", "28": null, "29": null, "30": "شب یلدا"}, "10": {"1": "جنگ های ایران و روسیه - حمله ارتش روسیه به گنجه واقع در جمهوری آذربایجان", "2": null, "3": "روز ثبت احوال", "4": "ولادت حضرت مسیح(ع)", "5": "روز ایمنی در برابر زلزله و کاهش اثرات بلایای طبیعی", "6": null, "7": "تشکیل نهضت سواد آموزی", "8": "روز صنعت پتروشیمی", "9": null, "10": null, "11": null, "12": null, "13": null, "14": null, "15": null, "16": null, "17": null, "18": null, "19": "قیام مردم قم", "20": "شهادت میرزا تقی خان امیر کبیر", "21": null, "22": "تشکیل شورای انقلاب", "23": null, "24": null, "25": null, "26": "فرار شاه از ایران", "27": null, "28": null, "29": null, "30": null}, "11": {"1": null, "2": "اعلام استقلال جمهوری کردستان از ایران با پشتیبانی اتحاد جماهیر شوروی", "3": null, "4": null, "5": null, "6": null, "7": null, "8": null, "9": null, "10": null, "11": null, "12": "بازگشت امام خمینی(ره) به ایران و آغاز دهه فجر", "13": null, "14": "روز فناوری فضایی", "15": null, "16": null, "17": null, "18": null, "19": "روز نیروی هوایی", "20": null, "21": null, "22": "پیروزی انقلاب اسلامی", "23": null, "24": null, "25": null, "26": null, "27": null, "28": null, "29": "قیام مردم تبریز", "30": null}, "12": {"1": "امضاء عهدنامه ترکمنچای", "2": null, "3": "کودتای رضاخان", "4": null, "5": "روز بزرگداشت خواجه نصیرالدین طوسی", "6": null, "7": null, "8": null, "9": "روز حمایت از حقوق مصرف کنندگان", "10": null, "11": "نیروهای انگلیسی از ایران خارج شدند. اتحاد جماهیر شوروی موافقت قبلی خود را نقض و عقب نشینی نکرد", "12": null, "13": null, "14": "روز احسان و نیکوکاری", "15": "روز درختکاری", "16": null, "17": null, "18": null, "19": null, "20": null, "21": "روز بزرگداشت نظامی گنجوی", "22": null, "23": null, "24": null, "25": "بمباران شیمیایی حلبچه به دست ارتش بعث عراق", "26": null, "27": null, "28": null, "29": "روز ملی شدن صنعت نفت", "30": null}}'''
x = json.loads(jdata)

class MainApp (MainApp):
    def loop (self):
        if not self.dsel.property('text')=='':
            self.xplit = self.dsel.property('text').split('/')
            self.x1plit = self.dselm.property('text').split('/')

            self.txtD.setProperty('text',x[self.xplit[0]][self.xplit[1]])

        QTimer.singleShot (100,self.loop)
    def __init__(self):
        super(MainApp, self).__init__()

        self.load (res.get('@layout/calendar'))
        self.setProperty('title',res.getname('calendar'))
        app.launchedlogo(self.property('title'), res.etc('calendar', 'logo'))

        self.Jalali = self.findChild('Jalali')
        self.Gregorian = self.findChild('Gregorian')
        self.dsel = self.findChild('dsel')
        self.dselm = self.findChild('dselm')
        self.txtD = self.findChild('txtD')
        x = res.getuserdata ('type')

        if x==None:
            x = control.read_record ('type','/etc/default/calendar')
        
        if x=='0':
            self.Gregorian.setProperty('visible',True)
        elif x=='1':
            self.Jalali.setProperty('visible',True)
        elif x=='2':
            locale = res.getdata("locale")
            
            if locale=="fa":
                self.Gregorian.setProperty('visible',False)
                self.Jalali.setProperty('visible',True)
            else:
                self.Gregorian.setProperty('visible',True)
                self.Jalali.setProperty('visible',False)

        self.loop()


application = QtGui.QGuiApplication([])
application.setWindowIcon (QIcon(res.get(res.etc('calendar','logo'))))

w = MainApp()
application.exec()