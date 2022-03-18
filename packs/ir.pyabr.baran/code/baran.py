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
import datetime,csv
import json
import os,multiprocessing
import random
from re import sub
import subprocess
import sys, hashlib,shutil,psutil, requests
from pyabr.core import *
from pyabr.quick import *

try:
    issue = subprocess.check_output(['cat','/etc/issue.net']).decode('utf-8').replace('\n','')
except:
    issue = ''

def windows_manager ():
    try:
        subprocess.call([control.read_record('external-windows-manager','/etc/gui')])
    except:
        pass

def vkey():
    try:
        subprocess.call(['/usr/bin/rm','-rf','/root/.config/dconf'])
        subprocess.call(['/usr/bin/onboard', '--theme', 'Droid'])

        app.launchedlogo('Onboard','@icon/onboard')
    except:
        pass

application = QGuiApplication(sys.argv)
application.setWindowIcon(QIcon(res.get('@icon/pyabr')))

jdata = '''{"1": {"1": "آغاز نوروز", "2": "آغاز عملیات فتح المبین", "3": "عید نوروز", "4": "عید نوروز", "5": null, "6": null, "7": "روز هنرهای نمایشی", "8": null, "9": null, "10": null, "11": "تقویم هجری شمسی به طور قانونی در ایران تصویب شده", "12": "روز جمهوری اسلامی ایران", "13": "روز طبیعت", "14": null, "15": "روز زخایر ژنتیکی و زیستی", "16": null, "17": null, "18": "روز سلامتی", "19": null, "20": "روز ملی فناوری هسته ای", "21": "شهادت امیر سپهبد علی صیاد شیرازی", "22": null, "23": null, "24": null, "25": "روز بزرگداشت عطار نیشابوری", "26": null, "27": null, "28": null, "29": "روز ارتش جمهوری اسلامی و نیروی زمینی", "30": null, "31": null}, "2": {"1": "روز بزرگداشت سعدی", "2": "سالروز اعلام انقلاب فرهنگی", "3": "روز بزرگداشت شیخ بهایی", "4": null, "5": "شکست حمله نظامی آمریکا به ایران در طبس", "6": null, "7": "روز ایمنی و حمل و نقل", "8": null, "9": "روز شوراها", "10": "روز ملی خلیج فارس", "11": "روز جهانی کار و کارگر", "12": "شهادت استاد مرتضی مطهری", "13": null, "14": null, "15": "روز بزرگداشت شیخ صدوق", "16": null, "17": null, "18": "روز بیماری های خاص و صعب العلاج", "19": "خروج نیروهای شوروی از ایران", "20": null, "21": null, "22": null, "23": null, "24": "لغو امتیاز تنباکو به فتوای آیت الله میرزا حسن شیرازی", "25": "روز بزرگداشت حکیم ابوالقاسم فردوسی و پاسداشت زبان فارسی", "26": null, "27": "روز ارتباطات و روابط عمومی", "28": "روز بزرگداشت حکیم عمر خیام", "29": null, "30": "روز ملی جمعیت", "31": " امضاء معاهده استانبول بین ایران و عثمانی و واگزاری سرزمین های قفقاز به دولت عثمانی به مدت چندین سال "}, "3": {"1": "روز بزرگداشت ملاصدرا", "2": null, "3": "فتح خرمشهر در عملیات بیت المقدس", "4": "روز دزفول - روز مقاومت و پایداری", "5": "روز حمایت از خانواده زندانیان", "6": null, "7": "افتتاح اولین دوره مجلس شورای اسلامی", "8": null, "9": null, "10": null, "11": null, "12": null, "13": null, "14": "رحلت امام خمینی(ره) بنیانگزار جمهوری اسلامی ایران", "15": "قیام 15 خرداد", "16": null, "17": null, "18": null, "19": null, "20": "روز صنایع دستی", "21": null, "22": null, "23": null, "24": null, "25": null, "26": null, "27": "روز جهاد کشاورزی", "28": null, "29": "درگذشت دکتر علی شریعتی", "30": null, "31": "شهادت دکتر مصطفی چمران"}, "4": {"1": "روز اصناف", "2": null, "3": null, "4": null, "5": null, "6": null, "7": "روز قوه قضاییه", "8": "روز مبارزه با سلاح های شیمیایی و میکروبی", "9": null, "10": "روز بزرگداشت صائب تبریزی", "11": "شهادت ایت الله صدوقی", "12": "حمله ناو آمریکایی به هواپیمای مسافربری جمهوری اسلامی", "13": null, "14": "روز شهرداری و دهیاری", "15": null, "16": "روز مالیات", "17": null, "18": "روز ادبیات کودکان و نوجوانان", "19": null, "20": null, "21": "روز فرهنگ پهلوانی و ورزش زورخانه ای", "22": null, "23": "گشایش اولین مجلس خبرگان رهبری", "24": null, "25": "روز بهزیستی و تأمین اجتماعی", "26": "سالروز تأسیس نهاد شورای نگهبان", "27": "اعلام پذیرش قطعنامه 598 شورای امنیت سازمان ملل از سوی ایران", "28": null, "29": null, "30": null, "31": null}, "5": {"1": null, "2": null, "3": null, "4": null, "5": "سالروز عملیات مرصاد", "6": "روز کارآفرینی و آموزش های فنی و حرفه ای", "7": null, "8": "روز بزرگداشت شیخ شهاب الدین سهروردی", "9": "روز اهدای خون", "10": null, "11": "شهادت آیت الله شیخ فضل الله نوری", "12": null, "13": null, "14": "صدور فرمان مشروطیت", "15": null, "16": "تشکیل جهاد دانشگاهی", "17": "روز خبرنگار", "18": null, "19": null, "20": null, "21": "روز حمایت از صنایع کوچک", "22": "روز تشکل ها و مشارکت های اجتماعی", "23": null, "24": null, "25": "جنگ های ایران و روسیه - حمله ایران به سرزمین های تازه اشغال شده توسط روس ها به منظور بازپس گیری این مناطق", "26": "آغاز بازگشت اسرای جنگی به ایران", "27": null, "28": "کودتای آمریکا برای بازگرداندن شاه", "29": null, "30": "روز بزرگداشت علامه مجلسی", "31": "روز صنعت دفاعی"}, "6": {"1": "روز بزرگداشت ابو علی سینا", "2": "آغاز هفته دولت", "3": "اشغال ایران توسط متفقین و فرار رضاخان", "4": "روز کارمند", "5": "روز بزرگداشت محمدبن زکریای رازی", "6": null, "7": null, "8": "انفجار دفتر نخست وزیری و شهادت رجایی و باهنر", "9": null, "10": "روز بانکداری اسلامی", "11": null, "12": "روز بهورز", "13": "امضاء معاهده گردان بین ایران و امپراطوری عثمانی ", "14": null, "15": "ورود پادشاه عثمانی به تبریز در پی اشغال شمال غربی ایران توسط عثمانی", "16": null, "17": "قیام 17 شهریور بر علیه حکومت پهلوی", "18": null, "19": "وفات آیت الله محمود طالقانی اولین امام جمعه تهران", "20": "نبرد کرتسانیسی بین آقامحمدخان قاجار و هراکلیوس دوم (حاکم گرجستان) و پیروزی آقا محمدخان و پیوستن دوباره منطقه قفقاز به ایران", "21": "امضاء معاهده سنت پترزبورگ بین ایران و روسیه", "22": null, "23": null, "24": null, "25": "روز خانواده و تکریم بازنشستگان", "26": "رسیدن نیروهای برتانیا و روسیه به یکدیگر در تهران در پی اشغال ایران در جنگ جهانی دوم", "27": "روز شعر و ادب فارسی", "28": null, "29": null, "30": "امضاء عهدنامه آخال میان ایران و امپراتوری روسیه", "31": "آغاز جنگ تحمیلی"}, "7": {"1": null, "2": null, "3": null, "4": null, "5": "شکست حصر آبادان در عملیات ثامن الائمه", "6": null, "7": "روز بزرگداشت شمس تبریزی", "8": "روز بزرگداشت مولوی", "9": "روز جهانی سالمندان", "10": "روز تجلیل از اسرا و مفقودان", "11": null, "12": null, "13": "روز نیروی انتظامی", "14": "روز دامپزشکی", "15": "روز روستا و عشایر", "16": null, "17": null, "18": null, "19": null, "20": "روز بزرگداشت حافظ", "21": null, "22": "روز جهانی استاندارد", "23": "روز جهانی نابینایان", "24": "روز پیوند اولیا و مربیان", "25": null, "26": "روز تربیت بدنی و ورزش", "27": null, "28": null, "29": "روز صادرات", "30": null}, "8": {"1": "روز آمار و برنامه ریزی", "2": " امضاء عهدنامه گلستان بین ایران و روسیه -  قفقاز ،ارمنستان و ایالت‌های شرقی گرجستان از ایران سلب و به روسیه واگذار شد", "3": null, "4": null, "5": "روز بزرگداشت سلمان فارسی", "6": null, "7": null, "8": "روز نوجوان و بسیج دانش آموزی", "9": null, "10": null, "11": null, "12": null, "13": "روز دانش آموز", "14": "روز فرهنگ عمومی", "15": null, "16": null, "17": null, "18": "روز کیفیت", "19": "روز جهانی علم در خدمت صلح و توسعه", "20": null, "21": null, "22": null, "23": null, "24": "روز کتاب، کتاب خوانی و کتابدار", "25": "روز وقف", "26": "سالروز آزادسازی سوسنگرد", "27": null, "28": null, "29": null, "30": null}, "9": {"1": null, "2": null, "3": null, "4": null, "5": "سالروز قیام مردم گرگان", "6": null, "7": "روز نیروی دریای", "8": null, "9": "روز بزرگداشت شیخ مفید", "10": "روز مجلس", "11": "شهادت میرزا کوچک خان جنگلی", "12": "روز قانون اساسی جمهوری اسلامی ایران (تصویب قانون اساسی جمهوری اسلامی ایران)", "13": "روز بیمه", "14": null, "15": null, "16": "روز دانشجو", "17": null, "18": "معرفی عراق به عنوان آغازگر جنگ از سوی سازمان ملل", "19": "تشکیل شورای فرهنگی به فرمان امام خمینی(ره)", "20": "ایران مناطق تحت کنترل حکومت ملی آذربایجان را باز پس گرفت", "21": null, "22": null, "23": null, "24": "تصرف مهاباد توسط ارتش ایران", "25": "روز پژوهش", "26": "روز حمل و نقل و رانندگان", "27": "روز جهان عاری از خشونت و افراطی گری", "28": null, "29": null, "30": "شب یلدا"}, "10": {"1": "جنگ های ایران و روسیه - حمله ارتش روسیه به گنجه واقع در جمهوری آذربایجان", "2": null, "3": "روز ثبت احوال", "4": "ولادت حضرت مسیح(ع)", "5": "روز ایمنی در برابر زلزله و کاهش اثرات بلایای طبیعی", "6": null, "7": "تشکیل نهضت سواد آموزی", "8": "روز صنعت پتروشیمی", "9": null, "10": null, "11": null, "12": null, "13": null, "14": null, "15": null, "16": null, "17": null, "18": null, "19": "قیام مردم قم", "20": "شهادت میرزا تقی خان امیر کبیر", "21": null, "22": "تشکیل شورای انقلاب", "23": null, "24": null, "25": null, "26": "فرار شاه از ایران", "27": null, "28": null, "29": null, "30": null}, "11": {"1": null, "2": "اعلام استقلال جمهوری کردستان از ایران با پشتیبانی اتحاد جماهیر شوروی", "3": null, "4": null, "5": null, "6": null, "7": null, "8": null, "9": null, "10": null, "11": null, "12": "بازگشت امام خمینی(ره) به ایران و آغاز دهه فجر", "13": null, "14": "روز فناوری فضایی", "15": null, "16": null, "17": null, "18": null, "19": "روز نیروی هوایی", "20": null, "21": null, "22": "پیروزی انقلاب اسلامی", "23": null, "24": null, "25": null, "26": null, "27": null, "28": null, "29": "قیام مردم تبریز", "30": null}, "12": {"1": "امضاء عهدنامه ترکمنچای", "2": null, "3": "کودتای رضاخان", "4": null, "5": "روز بزرگداشت خواجه نصیرالدین طوسی", "6": null, "7": null, "8": null, "9": "روز حمایت از حقوق مصرف کنندگان", "10": null, "11": "نیروهای انگلیسی از ایران خارج شدند. اتحاد جماهیر شوروی موافقت قبلی خود را نقض و عقب نشینی نکرد", "12": null, "13": null, "14": "روز احسان و نیکوکاری", "15": "روز درختکاری", "16": null, "17": null, "18": null, "19": null, "20": null, "21": "روز بزرگداشت نظامی گنجوی", "22": null, "23": null, "24": null, "25": "بمباران شیمیایی حلبچه به دست ارتش بعث عراق", "26": null, "27": null, "28": null, "29": "روز ملی شدن صنعت نفت", "30": null}}'''
x = json.loads(jdata)

if 'Pyabr' in issue:
    shutil.copyfile('/stor/etc/default/openbox.xml','/root/.config/openbox/rc.xml')
    subprocess.call(['/usr/bin/sudo','openbox','--reconfigure'])
    s = multiprocessing.Process(target=windows_manager)
    s.start()
    keylessx = ''
    for i in files.list ('/usr/share/locales'):
        if i.endswith('.locale') and control.read_record('keyless.enable',f'/usr/share/locales/{i}')=='Yes':
            ic = control.read_record ('keyless',f'/usr/share/locales/{i}')
            if keylessx=='':
                keylessx+=ic
            else:
                keylessx+=f',{ic}'

    subprocess.call(f'/usr/bin/setxkbmap -layout "{keylessx}" -option "grp:alt_shift_toggle"',shell=True)

    if files.isfile ('/proc/info/randr'): subprocess.call(['/usr/bin/xrandr','-s',files.readall('/proc/info/randr')])

files.write('/proc/info/id','baran')


## Get data ##
def getdata (name):
    return control.read_record (name,'/etc/gui')

class Backend (MainApp):
    def runSplash (self):
        self.splash = Splash([self])

    def runLogin (self):
        self.login = Login([self])

    def runEnter (self):
        self.enter = Enter([self,control.read_record("username","/etc/gui")])
        control.write_record('username','guest','/etc/gui')

    def runDesktop (self):
        self.desktop = Desktop([self,control.read_record("username","/etc/gui"),control.read_record("password","/etc/gui")])
        control.write_record('username', 'guest', '/etc/gui')
        control.write_record('password', '*', '/etc/gui')

    def runUnlock (self):
        control.write_record('username', 'guest', '/etc/gui')

    def __init__(self):
        super(Backend,self).__init__()

        
        self.load (res.get('@layout/backend'))
        self.setProperty ('height',int(getdata("height")))
        self.setProperty ('width',int(getdata("width")))
        self.setProperty ('title','Pyabr OS')
        self.setProperty ('visibility',getdata("visibility"))

        # Actions

        params = getdata('params')

        control.write_record('params', 'gui', '/etc/gui')

        self.close()

        if params == 'splash':
            self.runSplash()
        elif params == 'login':
            self.runLogin()
        elif params == 'enter':
            self.runEnter()
        elif params == 'desktop':
            self.runDesktop()
        elif params == 'unlock':
            self.runUnlock()
        else:
            QTimer.singleShot(1000, self.runSplash)  ## Run splash after 1s

class Splash (MainApp):
    def runLogin (self):
        self.close()
        self.login = Login([self.Backend])

    def __init__(self,ports):
        super(Splash, self).__init__()

        
        self.Backend = ports[0]
        self.load(res.get('@layout/splash'))
        self.logo = self.findChild ('logo')
        self.logo.setProperty('source',res.qmlget('@icon/pyabr'))
        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('title', 'Pyabr OS')
        self.setProperty('visibility', getdata("visibility"))

        QTimer.singleShot(3000, self.runLogin)  ## Run login

class Login (MainApp):
    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        subprocess.call(['systemctl','suspend'])

    def lang_(self):
        pass

    def clean(self):
        self._username.setProperty('enabled',True)
        self._username.setProperty('placeholderText',res.get('@string/username_placeholder'))

    def next_(self):
        if self._username.property("text")=='':
            pass
        elif self._username.property("text")=='guest' and files.readall('/etc/guest')=='enable':
            self.close()
            self.desktop = Desktop([self.Backend, self._username.property("text"),'*'])
        elif files.isfile(f'/etc/users/{self._username.property("text")}') and not self._username=='guest':
            self.close()
            self.enter = Enter([self.Backend,self._username.property("text")])
        else:
            self.usernamet = self._username.property('text')
            self._username.setProperty('text','')
            self._username.setProperty("placeholderText",res.get('@string/user_not_found').replace('{0}',self.usernamet))
            self._username.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    def __init__(self,ports):
        super(Login, self).__init__()

        self.Backend = ports[0]

        self.load(res.get('@layout/login'))

        if not self.rootObjects():
            sys.exit(-1)

        self.profile = self.findChild('profile')
        self.profile.setProperty('source',res.qmlget('@icon/users'))

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects

        self._next = self.findChild( 'next')
        self._username = self.findChild( 'username')
        self._username.setProperty("placeholderText",res.get('@string/username_placeholder'))
        self._next.clicked.connect(self.next_)
        self._next.setProperty('text',res.get('@string/next'))
        self._background = self.findChild( 'background')

        self.shutdown = self.findChild('shutdown')
        self.txtShutdown = self.findChild('txtShutdown')
        self.txtShutdown.setProperty('text', res.get('@string/escape'))
        self.shutdown.clicked.connect(self.shutdown_)
        self.shutdown_img = self.findChild('shutdown_img')
        self.shutdown_img.setProperty('source', res.qmlget('@icon/breeze-shutdown'))
        self.reboot = self.findChild('reboot')
        self.txtReboot = self.findChild('txtReboot')
        self.txtReboot.setProperty('text', res.get('@string/restart'))
        self.reboot.clicked.connect(self.restart_)
        self.reboot_img = self.findChild('reboot_img')
        self.reboot_img.setProperty('source', res.qmlget('@icon/breeze-reboot'))
        self.suspend = self.findChild('suspend')
        self.txtSuspend = self.findChild('txtSuspend')
        self.txtSuspend.setProperty('text', res.get('@string/sleep'))
        self.suspend.clicked.connect(self.sleep_)
        self.suspend_img = self.findChild('suspend_img')
        self.suspend_img.setProperty('source', res.qmlget('@icon/breeze-suspend'))
        self.popup_pysys = self.findChild('popup_pysys')

        if getdata("login.background").startswith('@background/'):
            self._background.setProperty('source', res.qmlget(getdata("login.background")))
        else:
            self._background.setProperty('source', files.input_qml(getdata("login.background")))

class Enter (MainApp):
    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        subprocess.call(['systemctl','suspend'])

    def lang_(self):
        pass

    def clean(self):
        self._password.setProperty('enabled',True)
        self._password.setProperty('placeholderText', res.get('@string/password_placeholder').replace('{0}',self.username))

    def login_(self):

        if control.read_record('code',f'/etc/users/{self.username}')==hashlib.sha3_512(self._password.property("text").encode()).hexdigest():
            self.close()
            self.desktop = Desktop([self.Backend, self.username, self._password.property("text")])
        else:
            self._password.setProperty('text','')
            self._password.setProperty('placeholderText', res.get('@string/wrong_password'))
            self._password.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    def logout_(self):

        self.close()

        System ("kma")

        # Logout
        files.create ('/proc/info/pause')
        subprocess.call([sys.executable,'vmabr.pyc','gui-login'])

    def getdata(self, name):
        try:
            x = control.read_record(name, f'/etc/users/{self.username}')
            if x == '' or x == None:
                x = getdata(name)
        except:
            x = getdata(name)

        return x

    def __init__(self, ports):
        super(Enter, self).__init__()

        self.Backend = ports[0]
        self.username = ports[1]

        self.load(res.get('@layout/enter'))
        if not self.rootObjects():
            sys.exit(-1)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects

        self.shutdown = self.findChild('shutdown')
        self.txtShutdown = self.findChild('txtShutdown')
        self.txtShutdown.setProperty('text', res.get('@string/escape'))
        self.shutdown.clicked.connect(self.shutdown_)
        self.shutdown_img = self.findChild('shutdown_img')
        self.shutdown_img.setProperty('source', res.qmlget('@icon/breeze-shutdown'))
        self.logout = self.findChild('logout')
        self.txtLogout = self.findChild('txtLogout')
        self.txtLogout.setProperty('text', res.get('@string/logout'))
        self.logout.clicked.connect(self.logout_)
        self.logout_img = self.findChild('logout_img')
        self.logout_img.setProperty('source', res.qmlget('@icon/breeze-logout'))
        self.reboot = self.findChild('reboot')
        self.txtReboot = self.findChild('txtReboot')
        self.txtReboot.setProperty('text', res.get('@string/restart'))
        self.reboot.clicked.connect(self.restart_)
        self.reboot_img = self.findChild('reboot_img')
        self.reboot_img.setProperty('source', res.qmlget('@icon/breeze-reboot'))
        self.suspend = self.findChild('suspend')
        self.txtSuspend = self.findChild('txtSuspend')
        self.txtSuspend.setProperty('text', res.get('@string/sleep'))
        self.suspend.clicked.connect(self.sleep_)
        self.suspend_img = self.findChild('suspend_img')
        self.suspend_img.setProperty('source', res.qmlget('@icon/breeze-suspend'))


        self._login = self.findChild( 'login')
        self._password = self.findChild( 'password')
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.username))
        self._login.clicked.connect(self.login_)
        self._login.setProperty('text',res.get('@string/login'))

        self._background = self.findChild( 'background')

        if self.getdata("enter.background").startswith('@background/'):        
            self._background.setProperty('source', res.qmlget(self.getdata("enter.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("enter.background")))
        self._profile = self.findChild('profile')

        if self.getdata("profile").startswith('@icon/'):
            self._profile.setProperty('source',res.qmlget(self.getdata("profile")))
        else:
            self._profile.setProperty('source',files.input_qml(self.getdata("profile")))


class Unlock (MainApp):
    def clean(self):
        self._password.setProperty('enabled',True)
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.Env.username))

    def unlock_(self):

        if control.read_record('code',f'/etc/users/{self.Env.username}')==hashlib.sha3_512(self._password.property("text").encode()).hexdigest():
            self.close()
        else:
            self._password.setProperty('text','')
            self._password.setProperty("placeholderText",res.get('@string/wrong_password'))
            self._password.setProperty('enabled',False)
            QTimer.singleShot(3000,self.clean)

    def getdata(self, name):
        x = control.read_record(name, f'/etc/users/{self.Env.username}')
        if x == '' or x == None:
            x = getdata(name)

        return x

    def __init__(self, ports):
        super(Unlock, self).__init__()

        

        self.Backend = ports[0]
        self.Env = ports[1]

        self.load(res.get('@layout/unlock'))
        if not self.rootObjects():
            sys.exit(-1)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects

        self._password = self.findChild( 'password')
        self._password.setProperty('placeholderText',res.get('@string/password_placeholder').replace('{0}',self.Env.username))
        self._unlock = self.findChild('login')
        self._unlock.setProperty('text',res.get('@string/unlock'))
        self._unlock.clicked.connect(self.unlock_)

        self._background = self.findChild( 'background')

        if  self.getdata("unlock.background").startswith('@background/'):     
            self._background.setProperty('source', res.qmlget(self.getdata("unlock.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("unlock.background")))
        self._profile = self.findChild( 'profile')

        if self.getdata("profile").startswith('@icon/'):
            self._profile.setProperty('source', res.qmlget(self.getdata("profile")))
        else:
            self._profile.setProperty('source', files.input_qml(self.getdata("profile")))

class Lock (MainApp):
    def unlock_(self):
        self.close()
        if not self.Env.username=='guest':
            self.unlock = Unlock([self.Backend,self.Env])

    def getdata (self,name):
        x = control.read_record(name,f'/etc/users/{self.Env.username}')
        if x=='' or x==None:
            x = getdata(name)

        return x

    def showTime (self):
        current_time = QTime.currentTime()
  
        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.txtClock.setProperty('text',res.num(label_time))

    def __init__(self, ports):
        super(Lock, self).__init__()

        

        self.Backend = ports[0]
        self.Env = ports[1]

        self.load(res.get('@layout/lock'))
        if not self.rootObjects():
            sys.exit(-1)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # Get data

        self.setProperty('height', int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title', 'Pyabr OS')

        # Connects
        self._unlock = self.findChild('unlock')
        self._unlock.clicked.connect (self.unlock_)


        self._background = self.findChild( 'background')
        self.txtClock = self.findChild('txtClock')

        if self.getdata("lock.background").startswith('@background/'):
            self._background.setProperty('source', res.qmlget(self.getdata("lock.background")))
        else:
            self._background.setProperty('source', files.input_qml(self.getdata("lock.background")))        

class Desktop (MainApp):
    AUDIOS = ''
    DESKTOP = ''
    DOCUMENTS = ''
    DOWNLOADS = ''
    PICTURES = ''
    PROJECTS = ''
    SAMPLES = ''
    VIDEOS = ''


    def shutdown_ (self):
        subprocess.call(['poweroff'])

    def restart_ (self):
        subprocess.call(['reboot'])

    def sleep_ (self):
        subprocess.call(['systemctl','suspend'])

    def logout_(self):
        self.close()
        
        System ("kma")

        # Logout
        files.create ('/proc/info/pause')
        subprocess.call([sys.executable,'vmabr.pyc','gui-login'])

    def lock_(self):
        self.lock = Lock([self.Backend,self])

    NameRole = QtCore.Qt.ItemDataRole.UserRole + 1000
    LabelRole = QtCore.Qt.ItemDataRole.UserRole + 1001
    LogoRole = QtCore.Qt.ItemDataRole.UserRole + 1002


    pins = 0

    def showTime(self):
        current_time = QTime.currentTime()

        # converting QTime object to string
        label_time = current_time.toString('hh:mm:ss')
        self.leClock.setProperty('text', res.num(label_time))

    def create_model(self,dir_path,category):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name",self.LabelRole: b'label',self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list(dir_path):
            categoryx = control.read_record('category',f'{dir_path}/{name}')
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if categoryx==category and not hidden=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]',f'{dir_path}/{name}')
                if namex=='' or namex==None:
                    namex = control.read_record(f'name[en]', f'{dir_path}/{name}')
                it.setData(namex,self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo',f'{dir_path}/{name}')),self.LogoRole)
                model.appendRow(it)
        return model


    def check_cat (self,dir_path,category):
        i = 0
        for name in files.list(dir_path):
            categoryx = control.read_record('category',f'{dir_path}/{name}')
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if categoryx==category and not hidden=='Yes':
                i+=1
        return i

    def create_model2(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/locales'):
            if control.read_record('keyless.enable',f'/usr/share/locales/{name}')=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record('name', f'/usr/share/locales/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/locales/{name}')), self.LogoRole)
                model.appendRow(it)
        return model


    def create_model3(self):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list('/usr/share/applications'):
            if res.etc(name.replace('.desk',''),'pin')=='Yes':
                self.pins+=1
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]', f'/usr/share/applications/{name}')
                if namex == '' or namex == None:
                    namex = control.read_record(f'name[en]', f'/usr/share/applications/{name}')
                it.setData(namex, self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo', f'/usr/share/applications/{name}')), self.LogoRole)
                model.appendRow(it)
        return model

    def create_model4(self,dir_path):
        model = QtGui.QStandardItemModel()
        roles = {self.NameRole: b"name",self.LabelRole: b'label',self.LogoRole: b'logo'}
        model.setItemRoleNames(roles)
        for name in files.list(dir_path):
            hidden = control.read_record('hidden',f'{dir_path}/{name}')
            if not hidden=='Yes':
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                namex = control.read_record(f'name[{getdata("locale")}]',f'{dir_path}/{name}')
                if namex=='' or namex==None:
                    namex = control.read_record(f'name[en]', f'{dir_path}/{name}')
                it.setData(namex,self.LabelRole)
                it.setData('../../../'+res.get(control.read_record('logo',f'{dir_path}/{name}')),self.LogoRole)
                model.appendRow(it)
        return model

    launchedapps = 0

    def get_launchedapps (self):
        try:
            lista = subprocess.check_output(['wmctrl', '-l']).decode('utf-8').split('\n')
            list2 = []
            for i in lista:
                try:
                    list2.append(i.split('  0 pyabr ')[1])
                except:
                    pass

            list2 = list(dict.fromkeys(list2))
            try:
                list2.pop(0)
            except:
                pass
        except:
            list2 = []

        return list2

    def get_len_of_launchedapps (self):
        try:
            return len(self.get_launchedapps())
        except:
            return 0

    def create_model_launchedapps (self):
        try:
            #https://www.w3schools.com/python/python_howto_remove_duplicates.asp
            self.launchedapps = self.get_len_of_launchedapps()

            model = QtGui.QStandardItemModel()
            roles = {self.NameRole: b"name", self.LabelRole: b'label', self.LogoRole: b'logo'}
            model.setItemRoleNames(roles)
            for name in self.get_launchedapps():
                it = QtGui.QStandardItem(name)
                it.setData(name, self.NameRole)
                it.setData(name, self.LabelRole)
                correctname = name.replace('\n','').replace('(','').replace(')', '').replace('0', '').replace('1', '').replace('2', '').replace('3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace('8', '').replace('9', '')
                if not control.read_record(correctname,'/etc/launched/logo.list')==None:
                    it.setData(res.qmlget(control.read_record(correctname,'/etc/launched/logo.list')), self.LogoRole)
                elif ' - ' in correctname:
                    scorrent = correctname.split(" - ")
                    it.setData(res.qmlget(control.read_record(scorrent[1],'/etc/launched/logo.list')), self.LogoRole)
                else:
                    worked = False
                    scorrent = correctname.split(" ")
                    for i in scorrent:
                        if not control.read_record(i,'/etc/launched/logo.list')==None:
                            worked = True
                            it.setData(res.qmlget(control.read_record(i,'/etc/launched/logo.list')), self.LogoRole)
                            break
                    if not worked:
                        it.setData(res.qmlget('@icon/app'), self.LogoRole)

                model.appendRow(it)
            return  model
        except:
            pass

    def getdata (self,name):
        try:
            x = control.read_record(name,f'/etc/users/{self.username}')
            if x=='' or x==None:
                x = getdata(name)
        except:
            x = res.get('@string/guest')

        return x

    def getnamex (self,database):
        try:
            x = control.read_record(f'name[{self.getdata("locale")}]', database)
            if x=='' or x==None:
                x = control.read_record(f'name[en]', database)
        except:
            x = control.read_record(f'name[en]', database)
        return x

    def signal (self):
        if not files.isfile('/proc/info/sig'):
            files.create('/proc/info/sig')

        elif files.readall('/proc/info/sig')=='sleep':
            files.create('/proc/info/sig')
            self.sleep_()

        elif files.readall('/proc/info/sig')=='pysys':
            files.create('/proc/info/sig')
            self.popup_pysys.open()

        elif files.readall('/proc/info/sig')=='shutdown':
            files.create('/proc/info/sig')
            self.shutdown_()

        elif files.readall('/proc/info/sig') == 'restart':
            files.create('/proc/info/sig')
            self.restart_()

        elif files.readall('/proc/info/sig')=='lock':
            files.create('/proc/info/sig')
            self.lock_()

        elif files.readall('/proc/info/sig')=='logout':
            files.create('/proc/info/sig')
            self.logout_()

        elif files.readall('/proc/info/sig')=='background':
            files.create('/proc/info/sig')
            self.update_background()

        elif files.readall('/proc/info/sig')=='apps':
            files.create('/proc/info/sig')
            self.update_apps()

        elif files.readall('/proc/info/sig')=='dock':
            files.create('/proc/info/sig')
            self.update_dock()

        elif files.readall('/proc/info/sig') == 'menu':
            files.create('/proc/info/sig')
            self.update_menu()

        files.create('/proc/info/sig')

    def update_background(self):
        try:
            if self.getdata('desktop.background').startswith('@background/'):
                self._background.setProperty('source', res.qmlget(self.getdata("desktop.background")))
            else:
                self._background.setProperty('source', files.input_qml(self.getdata("desktop.background")))
        except:
            pass

    def update_dock_bottom (self):
        self.xall = self.pins + self.launchedapps
        self.toolbar_height = self._toolbar.property('height')
        self._toolbar.setProperty('width', self.xall * self.toolbar_height)
        self._toolbar.setProperty('visible', True)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)
        # menu 1

    def update_menu1 (self):
        self._btnMenu = self.findChild('btnMenu')
        self.btnMenu_anim = self.findChild('btnMenu_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps')
        self.menuApps_anim = self.findChild('menuApps_anim')

    def update_dock_top(self):
        self.xall = self.pins + self.launchedapps
        self.toolbar_height2 = self._toolbar2.property('height')
        self._toolbar2.setProperty('width', self.xall * self.toolbar_height2)
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', True)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)
        # menu 2

    def update_menu2 (self):
        self._btnMenu = self.findChild('btnMenu2')
        self.btnMenu_anim = self.findChild('btnMenu2_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps2')
        self.menuApps_anim = self.findChild('menuApps2_anim')

    def update_dock_left (self):
        self.xall = self.pins + self.launchedapps
        self.toolbar_width3 = self._toolbar3.property('width')
        self._toolbar3.setProperty('height', self.xall * self.toolbar_width3)
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', True)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu3 (self):
        self._btnMenu = self.findChild('btnMenu3')
        self.btnMenu_anim = self.findChild('btnMenu3_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps3')
        self.menuApps_anim = self.findChild('menuApps3_anim')

    def update_dock_right (self):
        self.xall = self.pins + self.launchedapps
        self.toolbar_width4 = self._toolbar4.property('width')
        self._toolbar4.setProperty('height', self.xall * self.toolbar_width4)
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', True)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)


    def update_menu4 (self):
        self._btnMenu = self.findChild('btnMenu4')
        self.btnMenu_anim = self.findChild('btnMenu4_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps4')
        self.menuApps_anim = self.findChild('menuApps4_anim')

    def update_dock_windows_bottom (self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', True)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu5 (self):
        self._btnMenu = self.findChild('btnMenu5')
        self.btnMenu_anim = self.findChild('btnMenu5_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps')
        self.menuApps_anim = self.findChild('menuApps_anim')

    def update_dock_windows_top (self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', True)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu6 (self):
        self._btnMenu = self.findChild('btnMenu6')
        self.btnMenu_anim = self.findChild('btnMenu6_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps2')
        self.menuApps_anim = self.findChild('menuApps2_anim')

    def update_dock_windows_left(self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', True)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu7 (self):
        self._btnMenu = self.findChild('btnMenu7')
        self.btnMenu_anim = self.findChild('btnMenu7_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps3')
        self.menuApps_anim = self.findChild('menuApps3_anim')

    def update_dock_windows_right(self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', True)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu8 (self):
        self._btnMenu = self.findChild('btnMenu8')
        self.btnMenu_anim = self.findChild('btnMenu8_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps4')
        self.menuApps_anim = self.findChild('menuApps4_anim')

    def update_dock_unity_bottom (self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', True)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu9 (self):
        self._btnMenu = self.findChild('btnMenu9')
        self.btnMenu_anim = self.findChild('btnMenu9_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps')
        self.menuApps_anim = self.findChild('menuApps_anim')

    def update_dock_unity_top (self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', True)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', False)

    def update_menu10 (self):
        self._btnMenu = self.findChild('btnMenu10')
        self.btnMenu_anim = self.findChild('btnMenu10_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps2')
        self.menuApps_anim = self.findChild('menuApps2_anim')

    def update_dock_unity_left(self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', True)
        self._toolbar12.setProperty('visible', False)

    def update_menu11 (self):
        self._btnMenu = self.findChild('btnMenu11')
        self.btnMenu_anim = self.findChild('btnMenu11_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps3')
        self.menuApps_anim = self.findChild('menuApps3_anim')

    def update_dock_unity_right(self):
        self._toolbar.setProperty('visible', False)
        self._toolbar2.setProperty('visible', False)
        self._toolbar3.setProperty('visible', False)
        self._toolbar4.setProperty('visible', False)
        self._toolbar5.setProperty('visible', False)
        self._toolbar6.setProperty('visible', False)
        self._toolbar7.setProperty('visible', False)
        self._toolbar8.setProperty('visible', False)
        self._toolbar9.setProperty('visible', False)
        self._toolbar10.setProperty('visible', False)
        self._toolbar11.setProperty('visible', False)
        self._toolbar12.setProperty('visible', True)

    def update_menu12 (self):
        self._btnMenu = self.findChild('btnMenu12')
        self.btnMenu_anim = self.findChild('btnMenu12_anim')
        self._btnMenu.clicked.connect(self.menuApps_)
        self._menuApps = self.findChild('menuApps4')
        self.menuApps_anim = self.findChild('menuApps4_anim')

    def update_dock (self):
        if self.getdata('dock') == 'bottom':
            self.update_dock_bottom()

        elif self.getdata('dock') == 'top':
            self.update_dock_top()

        elif self.getdata('dock') == 'left':
            self.update_dock_left()

        elif self.getdata('dock') == 'right':
            self.update_dock_right()

        elif self.getdata('dock') == 'windows' or self.getdata('dock') == 'windows-bottom':
            self.update_dock_windows_bottom()

        elif self.getdata('dock') == 'windows-top':
            self.update_dock_windows_top()

        elif self.getdata('dock') == 'windows-left':
            self.update_dock_windows_left()

        elif self.getdata('dock') == 'windows-right':
            self.update_dock_windows_right()

        elif self.getdata('dock') == 'unity' or self.getdata('dock') == 'unity-bottom':
            self.update_dock_unity_bottom()

        elif self.getdata('dock') == 'unity-top':
            self.update_dock_unity_top()

        elif self.getdata('dock') == 'unity-left':
            self.update_dock_unity_left()

        elif self.getdata('dock') == 'unity-right':
            self.update_dock_unity_right()

    def update_menu (self):
        if self.getdata('dock') == 'bottom':
            self.update_menu1()

        elif self.getdata('dock') == 'top':
            self.update_menu2()

        elif self.getdata('dock') == 'left':
            self.update_menu3()

        elif self.getdata('dock') == 'right':
            self.update_menu4()

        elif self.getdata('dock') == 'windows' or self.getdata('dock') == 'windows-bottom':
            self.update_menu5()

        elif self.getdata('dock') == 'windows-top':
            self.update_menu6()

        elif self.getdata('dock') == 'windows-left':
            self.update_menu7()

        elif self.getdata('dock') == 'windows-right':
            self.update_menu8()

        elif self.getdata('dock') == 'unity' or self.getdata('dock') == 'unity-bottom':
            self.update_menu9()

        elif self.getdata('dock') == 'unity-top':
            self.update_menu10()

        elif self.getdata('dock') == 'unity-left':
            self.update_menu11()

        elif self.getdata('dock') == 'unity-right':
            self.update_menu12()

    def update_lanuched_apps (self):
        if not self.launchedapps == self.get_len_of_launchedapps():
            self.modelAllApplicationsx = self.create_model_launchedapps()
            self.rootContext().setContextProperty('LaunchedAppApplications', self.modelAllApplicationsx)

    def update_apps (self):
        self.modelAllApplications = self.create_model4('/usr/share/applications')
        self.rootContext().setContextProperty('EntryAppApplications', self.modelAllApplications)

    def loop (self):
        # Applications starts in background

        try:
            self.update_lanuched_apps()
            self.update_dock()
        except:
            pass

        if not self._background_app.property('text')=='':
            self._menuApps.setProperty('visible', False)
            self.menuClicked = False
            
            if files.isfile ('/proc/info/ext'): files.remove ('/proc/info/ext')

            #System ('rma')

            app.start(self._background_app.property('text').replace('.desk',''),'')


        if not self._restore_app.property('text')=='':
            try:
                resapp = ''
                
                if 'Python' in self._restore_app.property("text"):
                    resapp = 'Python'
                elif 'Bash' in self._restore_app.property("text"):
                    resapp = 'Bash'
                elif 'Konsole' in self._restore_app.property("text"):
                    resapp = 'Konsole'
                else:
                    resapp = self._restore_app.property("text")
                self.winid = subprocess.check_output(f'xdotool search "{resapp}"',shell=True).decode('utf-8').split('\n')
                for i in self.winid:
                    try:
                        subprocess.call(f'xdotool windowactivate {i}',shell=True)
                    except:
                        pass
            except:
                pass

        # Check signals #
        if not files.isfile('/proc/info/pause'):
            files.write('/proc/info/su',self.username)

        self.signal()

        self._background_app.setProperty('text','')
        self._restore_app.setProperty('text','')

        # scrot

        if os.path.isfile('/usr/bin/scrot'): subprocess.call(f'/usr/bin/mv /root/*scrot* /stor/{self.PICTURES}',shell=True)

        #self.addFileModel('/root/Desktop')

        self.shells()

        # Check feeds #

        self.feedCheck()
        self.changeDate()

        # audio changing volume #
        if self.eventClicked:
            try:
                subprocess.call (f'amixer set \'Master\' {str(int(self.slAudio.property("value")))}%',shell=True)
            except:
                pass

        # jumper:

        QTimer.singleShot(200,self.loop)

    def changeDate (self):
        if not self.dsel.property('text')=='':
            self.xplit = self.dsel.property('text').split('/')
            self.x1plit = self.dselm.property('text').split('/')

            self.txtD.setProperty('text',x[self.xplit[0]][self.xplit[1]])

    # Check feeds #
    def feedCheck (self):
        if not self.feedsel.property('text')=='':
            self.showpanel.setProperty('visible',False)
            self.panelClicked = False
            app.start('jooya',self.feedsel.property('text'))
        self.feedsel.setProperty('text','')
    # function of battery #

    def update_shell_wifi (self,w20,w40,w80,w100):
        self.shell_w020.setProperty('visible', w20)
        self.shell_w040.setProperty('visible', w40)
        self.shell_w080.setProperty('visible', w80)
        self.shell_w100.setProperty('visible', w100)

    def update_shell_battery (self,dicargs):
        self.battery_000.setProperty('visible', dicargs['000'])
        self.battery_010.setProperty('visible', dicargs['010'])
        self.battery_020.setProperty('visible', dicargs['020'])
        self.battery_030.setProperty('visible', dicargs['030'])
        self.battery_040.setProperty('visible', dicargs['040'])
        self.battery_050.setProperty('visible', dicargs['050'])
        self.battery_060.setProperty('visible', dicargs['060'])
        self.battery_070.setProperty('visible', dicargs['070'])
        self.battery_080.setProperty('visible', dicargs['080'])
        self.battery_090.setProperty('visible', dicargs['090'])
        self.battery_100.setProperty('visible', dicargs['100'])
        self.battery_000_charging.setProperty('visible', dicargs['000c'])
        self.battery_010_charging.setProperty('visible', dicargs['010c'])
        self.battery_020_charging.setProperty('visible', dicargs['020c'])
        self.battery_030_charging.setProperty('visible', dicargs['030c'])
        self.battery_040_charging.setProperty('visible', dicargs['040c'])
        self.battery_050_charging.setProperty('visible', dicargs['050c'])
        self.battery_060_charging.setProperty('visible', dicargs['060c'])
        self.battery_070_charging.setProperty('visible', dicargs['070c'])
        self.battery_080_charging.setProperty('visible', dicargs['080c'])
        self.battery_090_charging.setProperty('visible', dicargs['090c'])
        self.battery_100_charging.setProperty('visible', dicargs['100c'])

    def shells (self):
        # WiFi Check
        try:
            self.wifi_signal = int(subprocess.check_output('nmcli -t -f SIGNAL dev wifi',shell=True))
            if self.wifi_signal<=20:
                self.update_shell_wifi_signal(True,False,False,False)
            elif self.wifi_signal<=40:
                self.update_shell_wifi_signal(False,True,False,False)
            elif self.wifi_signal<=80:
                self.update_shell_wifi_signal(False,False,True,False)
            elif self.wifi_signal<=100:
                self.update_shell_wifi_signal(False,False,False,True)
        except:
            pass

        # Battery check
        try:
            battery = psutil.sensors_battery()
            percent = int(battery.percent)
            plugged = battery.power_plugged

            self.battery_percent.setProperty('visible',True)
            self.battery_percent_text.setProperty('text',f"{str(percent)}%")

            if plugged:
                if percent<10:
                    self.update_shell_battery({
                        '000c':True,
                        '010c':False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent < 20:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': True,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<30:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': True,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<40:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': True,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<50:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': True,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<60:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': True,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<70:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': True,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<80:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': True,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<90:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': True,
                        '090c': False,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                elif percent<100:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': True,
                        '100c': False,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
                else:
                    self.update_shell_battery({
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': True,
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                    })
            else:
                if percent < 10:
                    self.update_shell_battery({
                        '000': True,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 20:
                    self.update_shell_battery({
                        '000': False,
                        '010': True,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 30:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': True,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 40:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': True,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 50:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': True,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 60:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': True,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 70:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': True,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 80:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': True,
                        '080': False,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 90:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': True,
                        '090': False,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                elif percent < 100:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': True,
                        '100': False,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
                else:
                    self.update_shell_battery({
                        '000': False,
                        '010': False,
                        '020': False,
                        '030': False,
                        '040': False,
                        '050': False,
                        '060': False,
                        '070': False,
                        '080': False,
                        '090': False,
                        '100': True,
                        '000c': False,
                        '010c': False,
                        '020c': False,
                        '030c': False,
                        '040c': False,
                        '050c': False,
                        '060c': False,
                        '070c': False,
                        '080c': False,
                        '090c': False,
                        '100c': False,
                    })
        except:
            self.battery_percent.setProperty('visible',True)

    def startup (self):
        # Startup applications
        try:
            lists = control.read_list('/etc/suapp')
            for i in lists:
                app.start(i, '')
        except:
            pass

    def saye (self):
        try:
            if 'Pyabr' in issue:
                if self.username=='guest':
                    f = open('/usr/bin/saye','w')
                    f.write(f'#!/usr/bin/bash\ncd /stor\npython3 vmabr.pyc user guest\nexit')
                    f.close()
                else:
                    f = open('/usr/bin/saye','w')
                    f.write(f'#!/usr/bin/bash\ncd /stor\npython3 vmabr.pyc user {self.username} {self.password}\nexit')
                    f.close()
                subprocess.call("/usr/bin/chmod +x /usr/bin/saye",shell=True)
        except:
            pass

    def pwduser (self):
        if self.username=='root':
            commands.cd (['/root'])
        else:
            commands.cd ([f'/desk/{self.username}'])

    def deskdirs (self):
        deskdirspath = files.readall('/etc/deskdirs')

        for i in files.list (deskdirspath):
            if files.isdir (f'{deskdirspath}/{i}'):
                try:
                    files.copydir (f'{deskdirspath}/{i}',f'{i}')
                except:
                    pass

        if self.username == 'root':
            self.AUDIOS = '/root/Audios'
            self.DESKTOP = '/root/Desktop'
            self.DOCUMENTS = '/root/Documents'
            self.DOWNLOADS = '/root/Downloads'
            self.PICTURES = '/root/Pictures'
            self.PROJECTS = '/root/Projects'
            self.SAMPLES = '/root/Samples'
            self.VIDEOS = '/root/Videos'
        else:
            self.AUDIOS = f'/desk/{self.username}/Audios'
            self.DESKTOP = f'/desk/{self.username}/Desktop'
            self.DOCUMENTS = f'/desk/{self.username}/Documents'
            self.DOWNLOADS = f'/desk/{self.username}/Downloads'
            self.PICTURES = f'/desk/{self.username}/Pictures'
            self.PROJECTS = f'/desk/{self.username}/Projects'
            self.SAMPLES = f'/desk/{self.username}/Samples'
            self.VIDEOS = f'/desk/{self.username}/Videos'

    def homelogo (self):
        files.write ('.logo','@icon/homes')

    menuClicked = False

    def update_menuapps (self,a0,a1):
        self._menuApps.setProperty('visible', a0)
        self.msaDesktop.setProperty('visible', a1)
        self.menuClicked = a0

    def menuApps_(self):
        if self.enable_anim.property('text')=='Yes':
            self.btnMenu_anim.start()
        if self.menuClicked:
            self.update_menuapps(False,True)
        else:
            if self.enable_anim.property('text') == 'Yes':
                self.menuApps_anim.start()
            self.update_menuapps(True,False)
            self.showpanel.setProperty('visible',False)
            self.eventpanel.setProperty('visible', False)
            self.notepanel.setProperty('visible', False)
            self.showclock.setProperty('visible',False)

    def account_setting_(self):
        app.start ('controls','users')

    def virtualkeyboard_(self):
        virtualkeyboard_run = multiprocessing.Process(target=vkey)
        virtualkeyboard_run.start()

    panelClicked = False
    eventClicked = False
    noteClicked = False
    clockClicked = False

    def showpanel_(self):

        if self.panelClicked:
            self.showpanel.setProperty('visible',False)
            self.panelClicked = False
        else:
            if self.enable_anim.property('text') == 'Yes':
                self.showpanel_anim.start()
            self.update_menuapps(False, True)
            self.showpanel.setProperty('visible', True)
            self.eventpanel.setProperty('visible', False)
            self.notepanel.setProperty('visible', False)
            self.showclock.setProperty('visible', False)
            self.panelClicked = True

    def eventpanel_(self):

        if self.eventClicked:
            self.eventpanel.setProperty('visible',False)
            self.eventClicked = False
        else:
            if self.enable_anim.property('text') == 'Yes':
                self.eventpanel_anim.start()

            self.update_menuapps(False, True)
            self.eventpanel.setProperty('visible', True)
            self.showpanel.setProperty('visible', False)
            self.showclock.setProperty('visible', False)
            self.notepanel.setProperty('visible', False)
            self.eventClicked = True

    def notepanel_(self):

        if self.noteClicked:
            self.notepanel.setProperty('visible',False)
            self.noteClicked = False
        else:
            if self.enable_anim.property('text') == 'Yes':
                self.notepanel_anim.start()

            self.update_menuapps(False, True)
            self.notepanel.setProperty('visible', True)
            self.showpanel.setProperty('visible', False)
            self.showclock.setProperty('visible', False)
            self.eventpanel.setProperty('visible', False)
            self.noteClicked = True

    def showclock_(self):
        if self.clockClicked:
            self.showclock.setProperty('visible',False)
            self.clockClicked = False
        else:
            if self.enable_anim.property('text') == 'Yes':
                self.showclock_anim.start()
            self.update_menuapps(False, True)
            self.showclock.setProperty('visible', True)
            self.showpanel.setProperty('visible', False)
            self.eventpanel.setProperty('visible', False)
            self.notepanel.setProperty('visible', False)
            self.clockClicked = True

    def calcTemp (self):
        try:
            Url = f"https://api.openweathermap.org/data/2.5/weather?q={files.readall('/etc/default/baadcity')}&appid=d2ae6d25c09549f38d8feed1d116c580"
        except:
            Url = f"https://api.openweathermap.org/data/2.5/weather?q=tehran&appid=d2ae6d25c09549f38d8feed1d116c580"

        try:
            data = (requests.get(Url)).json()
            temp = round( data['main']["temp"] - 275.15)
            type = data["weather"][0]['main'].lower()

            self.txtTemp = self.findChild('txtTemp')
            self.imgTemp = self.findChild('imgTemp')

            self.txtTemp.setProperty('text', res.num(str(temp)) + ' °C')

            if 'few' in type and 'wind' in type and 'clouds' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_FewClouds')))
            elif 'clear' in type and 'wind' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clear')))
            elif 'snow' in type and 'scattered' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'Baad_Snow')))
            elif 'shower' in type and 'scattered' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'Baad_Rain')))
            elif 'cloud' in type and 'wind' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clouds')))
            elif 'many' in type and 'clouds' in type and 'wind' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_FewClouds')))
            elif 'many' in type and 'clouds' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_FewClouds')))
            elif 'freezing' in type and 'rain' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Frozen')))
            elif 'overcast' in type and 'wind' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_FewClouds')))
            elif 'clear' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clear')))
            elif 'fog' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Fog')))
            elif 'hail' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Hails')))
            elif 'mist' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_BlackClouds')))
            elif 'snow' in type and 'rain' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Rain')))
            elif 'snow' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'Baad_Snow')))
            elif 'storm' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_BlackClouds')))
            elif 'showers' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Rain')))
            elif 'overcast' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clouds')))
            elif 'rain' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Rain')))
            elif 'few' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_FewClouds')))
            elif 'clouds' in type:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clouds')))
            else:
                self.imgTemp.setProperty('source', res.qmlget(res.etc('baad', 'BaaD_Clear')))
        except:
            pass

    def NotificationShow(self):
        try:
            n = Notifications()
            splitor = (n.Show()).split(":::")
            id_    = splitor[0]
            title_ = splitor[1]
            text_  = splitor[2]
            app_   = splitor[3]
            open_  = splitor[4]

            self.w = Notif (title_,text_,app_,open_)

        except:
            pass

        QTimer.singleShot(2000,self.NotificationShow)

    def __init__(self,ports):
        super(Desktop, self).__init__()

        self.addFileModel('/usr/share/samples/deskdirs')
        
        self.Backend = ports[0]
        self.username = ports[1]
        self.password = ports[2]
        self.modelDockApplications = self.create_model3()
        self.rootContext().setContextProperty('EntryDockApplications',self.modelDockApplications)

        #self.create_model5()

        self.modelAllApplications = self.create_model4('/usr/share/applications')
        self.rootContext().setContextProperty('EntryAppApplications', self.modelAllApplications)

        self.modelAllApplicationsx = self.create_model_launchedapps()
        self.rootContext().setContextProperty('LaunchedAppApplications', self.modelAllApplicationsx)
        self.addFeedModel()
        self.load(res.get('@layout/desktop'))
        if not self.rootObjects():
            sys.exit(-1)
        self.setProperty('height',int(getdata("height")))
        self.setProperty('width', int(getdata("width")))
        self.setProperty('visibility', getdata("visibility"))
        self.setProperty('title','Pyabr OS')
        self.imgMenu = self.findChild('imgMenu')
        self.enable_anim = self.findChild('enable_anim')
        self.feedsel = self.findChild('feedsel')
        self.enable_anim.setProperty('text',getdata('anim'))
        self.imgMenu.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu2 = self.findChild('imgMenu2')
        self.imgMenu2.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu3 = self.findChild('imgMenu3')
        self.imgMenu3.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu4 = self.findChild('imgMenu4')
        self.imgMenu4.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu5 = self.findChild('imgMenu5')
        self.imgMenu5.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu6 = self.findChild('imgMenu6')
        self.imgMenu6.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu7 = self.findChild('imgMenu7')
        self.imgMenu7.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu8 = self.findChild('imgMenu8')
        self.imgMenu8.setProperty('source',res.qmlget('@icon/pyabr'))
        self.imgMenu9 = self.findChild('imgMenu9')
        self.imgMenu9.setProperty('source', res.qmlget('@icon/pyabr'))
        self.imgMenu10 = self.findChild('imgMenu10')
        self.imgMenu10.setProperty('source', res.qmlget('@icon/pyabr'))
        self.imgMenu11 = self.findChild('imgMenu11')
        self.imgMenu11.setProperty('source', res.qmlget('@icon/pyabr'))
        self.imgMenu12 = self.findChild('imgMenu12')
        self.imgMenu12.setProperty('source', res.qmlget('@icon/pyabr'))
        self.appc = self.findChild( 'appc')
        self.appc.setProperty('text',res.get('@string/appearance'))
        self.displayc = self.findChild( 'displayc')
        self.displayc.setProperty('text',res.get('@string/display'))
        self.rmac = self.findChild( 'rmac')
        self.rmac.setProperty('text',res.get('@string/rma'))
        self.runc = self.findChild( 'runc')
        self.runc.setProperty('text',res.get('@string/runner'))
        self.refreshc = self.findChild('refreshc')
        #self.refreshc.setProperty('text', res.get('@string/runner'))

        self.shell_w100 = self.findChild('shell_w100')
        self.shell_w080 = self.findChild('shell_w080')
        self.shell_w040 = self.findChild('shell_w040')
        self.shell_w020 = self.findChild('shell_w020')

        self.virtualkeyboard = self.findChild('virtualkeyboard')
        self.virtualkeyboard.clicked.connect (self.virtualkeyboard_)

        self.showpanel = self.findChild('showpanel')
        self.showpanel_anim = self.findChild('showpanel_anim')
        self.eventpanel = self.findChild('eventpanel')
        self.eventpanel_anim = self.findChild('eventpanel_anim')
        self.showclock = self.findChild('showclock')
        self.showclock_anim = self.findChild('showclock_anim')
        self.notepanel = self.findChild('notepanel')
        self.notepanel_anim = self.findChild('notepanel_anim')

        self.Jalali = self.findChild('Jalali')
        self.dsel = self.findChild('dsel')
        self.dselm = self.findChild('dselm')
        self.txtD = self.findChild('txtD')

        self.btnPanel = self.findChild('btnPanel')
        if self.getdata("feed")=='Yes':
            self.btnPanel.setProperty('visible',True)
        else:
            self.btnPanel.setProperty('visible',False)
        self.btnPanel.clicked.connect (self.showpanel_)

        self.btnEvent = self.findChild('btnEvent')
        self.btnEvent.clicked.connect(self.eventpanel_)

        self.btnNote = self.findChild('btnNote')
        self.btnNote.clicked.connect(self.notepanel_)

        self.btnClock = self.findChild('btnClock')
        self.btnClock.clicked.connect(self.showclock_)

        self.shutdown = self.findChild('shutdown')
        self.txtShutdown = self.findChild('txtShutdown')
        self.txtShutdown.setProperty('text',res.get('@string/escape'))
        self.shutdown.clicked.connect (self.shutdown_)
        self.shutdown_img = self.findChild('shutdown_img')
        self.shutdown_img.setProperty('source', res.qmlget('@icon/breeze-shutdown'))
        self.lock = self.findChild('lock')
        self.txtLock = self.findChild('txtLock')
        self.txtLock.setProperty('text',res.get('@string/lock'))
        self.lock.clicked.connect (self.lock_)
        self.lock_img = self.findChild('lock_img')
        self.lock_img.setProperty('source', res.qmlget('@icon/lock'))
        self.logout = self.findChild('logout')

        self.txtLogout = self.findChild('txtLogout')
        self.txtLogout.setProperty('text',res.get('@string/logout'))
        self.logout.clicked.connect(self.logout_)
        self.logout_img = self.findChild('logout_img')
        self.logout_img.setProperty('source', res.qmlget('@icon/breeze-logout'))
        self.reboot = self.findChild('reboot')
        self.txtReboot = self.findChild('txtReboot')
        self.txtReboot.setProperty('text',res.get('@string/restart'))
        self.reboot.clicked.connect(self.restart_)
        self.reboot_img = self.findChild('reboot_img')
        self.reboot_img.setProperty('source', res.qmlget('@icon/breeze-reboot'))
        self.suspend = self.findChild('suspend')
        self.txtSuspend = self.findChild('txtSuspend')
        self.txtSuspend.setProperty('text',res.get('@string/sleep'))
        self.suspend.clicked.connect(self.sleep_)
        self.suspend_img = self.findChild('suspend_img')
        self.suspend_img.setProperty('source', res.qmlget('@icon/breeze-suspend'))

        self.popup_pysys = self.findChild('popup_pysys')
        self.popup_text = self.findChild('popup_text')

        self.slAudio = self.findChild ('slAudio')
        self.slAudio.setProperty('value','50')

        self.battery_000_charging = self.findChild('battery_000_charging')
        self.battery_010_charging = self.findChild('battery_010_charging')
        self.battery_020_charging = self.findChild('battery_020_charging')
        self.battery_030_charging = self.findChild('battery_030_charging')
        self.battery_040_charging = self.findChild('battery_040_charging')
        self.battery_050_charging = self.findChild('battery_050_charging')
        self.battery_060_charging = self.findChild('battery_060_charging')
        self.battery_070_charging = self.findChild('battery_070_charging')
        self.battery_080_charging = self.findChild('battery_080_charging')
        self.battery_090_charging = self.findChild('battery_090_charging')
        self.battery_100_charging = self.findChild('battery_100_charging')

        self.battery_000 = self.findChild('battery_000')
        self.battery_010 = self.findChild('battery_010')
        self.battery_020 = self.findChild('battery_020')
        self.battery_030 = self.findChild('battery_030')
        self.battery_040 = self.findChild('battery_040')
        self.battery_050 = self.findChild('battery_050')
        self.battery_060 = self.findChild('battery_060')
        self.battery_070 = self.findChild('battery_070')
        self.battery_080 = self.findChild('battery_080')
        self.battery_090 = self.findChild('battery_090')
        self.battery_100 = self.findChild('battery_100')

        self.battery_percent = self.findChild('battery_percent')
        self.battery_percent_text = self.findChild('battery_percent_text')

        self.leClock = self.findChild('leClock')

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        self._background = self.findChild( 'background')
        try:
            if self.getdata('desktop.background').startswith('@background/'):
                self._background.setProperty('source', res.qmlget(self.getdata("desktop.background")))
            else:
                self._background.setProperty('source', files.input_qml(self.getdata("desktop.background")))
        except:
            pass
        self._background_app = self.findChild('background_app')
        self._restore_app = self.findChild('restore_app')
        self._toolbar = self.findChild('toolbar')
        self._toolbar2 = self.findChild('toolbar2')
        self._toolbar3 = self.findChild('toolbar3')
        self._toolbar4 = self.findChild('toolbar4')
        self._toolbar5 = self.findChild('toolbar5')
        self._toolbar6 = self.findChild('toolbar6')
        self._toolbar7 = self.findChild('toolbar7')
        self._toolbar8 = self.findChild('toolbar8')
        self._toolbar9 = self.findChild('toolbar9')
        self._toolbar10 = self.findChild('toolbar10')
        self._toolbar11 = self.findChild('toolbar11')
        self._toolbar12 = self.findChild('toolbar12')
        self.msaDesktop = self.findChild('msaDesktop')
        self._keyless = self.findChild('keyless')

        self.Gregorian = self.findChild('Gregorian')
        self.Jalali = self.findChild('Jalali')

        x = control.read_record ('type','/etc/default/calendar')
        
        if x=='0':
            self.Gregorian.setProperty('visible',True)
            self.Jalali.setProperty('visible',False)
        elif x=='1':
            self.Gregorian.setProperty('visible',False)
            self.Jalali.setProperty('visible',True)
        elif x=='2':
            locale = self.getdata("locale")
            
            if locale=="fa":
                self.Gregorian.setProperty('visible',False)
                self.Jalali.setProperty('visible',True)
            else:
                self.Gregorian.setProperty('visible',True)
                self.Jalali.setProperty('visible',False)
        

        if self.getdata  ('dock')=='bottom':
            self.update_dock_bottom()
            self.update_menu1()

        elif self.getdata ('dock')=='top':
            self.update_dock_top()
            self.update_menu2()

        elif self.getdata  ('dock')=='left':
            self.update_dock_left()
            self.update_menu3()

        elif self.getdata  ('dock')=='right':
            self.update_dock_right()
            self.update_menu4()

        elif self.getdata  ('dock')=='windows' or self.getdata  ('dock')=='windows-bottom':
            self.update_dock_windows_bottom()
            self.update_menu5()

        elif self.getdata ('dock')=='windows-top':
            self.update_dock_windows_top()
            self.update_menu6()

        elif self.getdata ('dock')=='windows-left':
            self.update_dock_windows_left()
            self.update_menu7()

        elif self.getdata ('dock')=='windows-right':
            self.update_dock_windows_right()
            self.update_menu8()

        elif self.getdata  ('dock')=='unity' or self.getdata  ('dock')=='unity-bottom':
            self.update_dock_unity_bottom()
            self.update_menu9()

        elif self.getdata ('dock')=='unity-top':
            self.update_dock_unity_top()
            self.update_menu10()

        elif self.getdata ('dock')=='unity-left':
            self.update_dock_unity_left()
            self.update_menu11()

        elif self.getdata ('dock')=='unity-right':
            self.update_dock_unity_right()
            self.update_menu12()

        # check cats
        self.saye()
        self.pwduser()
        self.deskdirs()
        self.homelogo()

        # remove pause
        if files.isfile ('/proc/info/pause'): files.remove ('/proc/info/pause')

        # Start up applications
        self.startup()
        # Main Loop
        self.loop()
        QTimer.singleShot (10000,self.calcTemp)
        self.NotificationShow()

desktop = Backend()
sys.exit(application.exec())
