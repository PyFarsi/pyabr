import QtQuick 2.0
import QtQuick.Controls 1.4


Calendar{
    property bool isPersianMode: true
    property date persianGregorianSelectedDate
    onPersianGregorianSelectedDateChanged: {
        console.log(persianGregorianSelectedDate)
    }

    property var  persianDate

    function gregorian_to_jalali(gy,gm,gd){
        var g_d_m=[0,31,59,90,120,151,181,212,243,273,304,334];
        var jy=(gy<=1600)?0:979;
        gy-=(gy<=1600)?621:1600;
        var gy2=(gm>2)?(gy+1):gy;
        var days=(365*gy) +(parseInt((gy2+3)/4)) -(parseInt((gy2+99)/100))
                +(parseInt((gy2+399)/400)) -80 +gd +g_d_m[gm-1];
        jy+=33*(parseInt(days/12053));
        days%=12053;
        jy+=4*(parseInt(days/1461));
        days%=1461;
        jy+=parseInt((days-1)/365);
        if(days > 365)days=(days-1)%365;
        var jm=(days < 186)?1+parseInt(days/31):7+parseInt((days-186)/30);
        var jd=1+((days < 186)?(days%31):((days-186)%30));
        return [jy,jm,jd];
    }
    function jalali_to_gregorian(jy,jm,jd){
        var gy=(jy<=979)?621:1600;
        jy-=(jy<=979)?0:979;
        var days=(365*jy) +((parseInt(jy/33))*8) +(parseInt(((jy%33)+3)/4))
                +78 +jd +((jm<7)?(jm-1)*31:((jm-7)*30)+186);
        gy+=400*(parseInt(days/146097));
        days%=146097;
        if(days > 36524){
            gy+=100*(parseInt(--days/36524));
            days%=36524;
            if(days >= 365)days++;
        }
        gy+=4*(parseInt((days)/1461));
        days%=1461;
        gy+=parseInt((days-1)/365);
        if(days > 365)days=(days-1)%365;
        var gd=days+1;
        var sal_a=[0,31,((gy%4==0 && gy%100!=0) || (gy%400==0))?29:28,31,30,31,30,31,31,30,31,30,31];
        var gm
        for(gm=0;gm<13;gm++){
            var v=sal_a[gm];
            if(gd <= v)break;
            gd-=v;
        }
        return [gy,gm,gd];
    }
    function monthName(i){
        switch(i)
        {
        case 1:
            return "فروردین";
        case 2:
            return "اردیبهشت";
        case 3:
            return "خرداد";
        case 4:
            return "تیر";
        case 5:
            return "مرداد";
        case 6:
            return "شهریور";
        case 7:
            return "مهر";
        case 8:
            return "آبان";
        case 9:
            return "آذر";
        case 10:
            return "دی";
        case 11:
            return "بهمن";
        case 12:
            return "اسفند";
        }
    }
    function dayName(i,mode){
        switch(i)
        {
        case 0:
            return "ش";
        case 1:
            return "ی";
        case 2:
            return "د";
        case 3:
            return "س";
        case 4:
            return "چ";
        case 5:
            return "پ";
        case 6:
            return "ج";
        }
    }
    function dayNumber(jy,jm,jd)
    {
        var gr = jalali_to_gregorian(jy,jm,jd)
        return Date.fromLocaleString(Qt.locale(), gr[0]+"-"+gr[1]+"-"+gr[2], "yyyy-M-d").getDay()*1 + 1;
    }
    function dayInMonth(year,month)
    {
        month = month - 1
        if(month<0)return -1;
        if(month<6)return 31;
        if(month<11)return 30;

        var ary = [1, 5, 9, 13, 17, 22, 26, 30];
        var b = year % 33;
        for (var i = 0;i < ary.length; i++)
            if (b === ary[i])
                return 30;
        return 29;
    }

    style: PersianCalendarStyle{

    }
}
