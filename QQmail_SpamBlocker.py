#!/usr/bin/env python
# coding=utf-8
import os
import time
import winreg
import requests

os.environ['no_proxy'] = '*' #避免因系统代理设置导致请求失败

def syscheck(): #判断系统版本是否支持、是否存在失败列表，若有失败列表则优先拉黑失败列表，若无失败列表则使用内置黑名单提交拉黑
    if os.name == 'nt':
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders')
        desktop_path = winreg.QueryValueEx(key,'Desktop')[0]
        fail_list_path = os.path.join(desktop_path,'fail_list.txt')
        if os.path.exists(fail_list_path):
            with open (fail_list_path,'r') as file:
                block_list = file.readline().replace('[','').replace(']','').replace("'",'').replace(' ','').split(',')
            return desktop_path,block_list
        else:
            block_list = ['dnotice@mastermindkitchen.buzz', 'rbykwiakl@163.com', 'quzfkp@kpuze.com', 'resume@mail2.goodjobs.cn', 'return-to@letter.xiu.com', 'return-to@mail001.xiu.com', 'return-to@newsletter.mail.taobao.com', 'return-to@newsletter.quwan.com', 'return-to@v5cn.dmdelivery.com', 'return-to@wp.leshu.com', 'rht@shengda.edu.cn', 'qwergdsg@jyxkzg.com', 'pvpooycet@gotodie.com', 'quwan@newsletter.quwan.com', 'qq@bus3.cn', 'qq22888hj@yingjia.cn', 'qpjtm@211.157.4.2', 'qiinit@online.cq.cn', 'qidacheng@sdhj.com.cn', 'qidacheng01@shimaocopper.com', 'qe@farese.ch', 'qahake@feardearg.com', 'pzf123456@shendong.com.cn', 'pzf123456@hhzx.net', 'pzf123456@freebike.net', 'py@zmeetb.com', 'postmaster@liandisol.com.cn', 'sender@ler25.zaobang.com', 'shejianshang@wybgy.net', 'service@wal8.com', 'service@quwan.cn', 'service@playcomet.com', 'service@newsletter.zaobang.com', 'service@mingjiang104721156.com', 'service@fanrry.com', 'service@a13.newsletter.zaobang.com', 'server@wp.leshu.com', 'serve@guomeidqie5.cscorp.com', 'serive21@basketauihuigex03715442.com', 'sender@ler30.zaobang.com', 'sender@ler28.zaobang.com', 'rio803@126.com', 'sender@ler23.zaobang.com', 'sender@ler21.zaobang.com', 'sender@ler16.zaobang.com', 'selected@right.tmall.com', 'scottr@apigee.com', 'sales@cshaiyan.cn', 'rvylteyuxo@eramet-comilog.com', 'rtyrdudthfffxddh@126.com', 'rsc1@sqk.com.cn', 'rpgkjg7400@163.com', 'root@latinbits.com', 'rjutudio@everest-interactive.com', 'messenger@baishengunion.com', 'newsletter2@360buy.com', 'news@wal8.net', 'news@mailbox.etao.com', 'newjob2011@sina.cn', 'mychemicalromancerawksmysawks@yahoo.com', 'mvyfkhv@ne.com', 'mta4@tencent.com', 'mnfn@ssjbx.com', 'mlp@zsepower.com.cn', 'mlp@wybgy.net', 'midauto@x17.yesmywine.net', 'mgilapdqyz@exp-travel.com', 'metemeh@ergocomputersupplies.com', 'newsletter3@360buy.com', 'mengfei@mail-ruijie.com.cn', 'meishi@newsletter2.zaobang.com', 'master@6677bank.com', 'market@lingguang.com.cn', 'maonan189@naver.com', 'maobin@js11183.com', 'mansoor@consultstart.com', 'mail234.suw12.mcsv.net#info@woocommerce.com', 'mail188.wdc02.mcdlv.net#support@bluefx.net', 'mail-noreply01@mx.kaba365.com', 'm1@liaozhai.tv', 'lwm@nfc.sh', 'nuiatyu@esperanzza.de', 'pqq1328872918062@system.mail', 'shirz@robot.nankai.edu.cn', 'podongtymt@yahoo.cn', 'phbids@ewrjik.org', 'peter.xu@tourandersson.com.cn', 'papamama@publica.bj.cninfo.net', 'otxcgl@tychlqu.com', 'orders@nrcha.com', 'coachchina@news.coach.com', 'newsletter@newsletter.aliyun.com', 'online@better90w.07919.com', 'onetone@weekly71.webclassroom.cn', 'omtdxb@eim.ae', 'olg@eurodiesel.com.au', 'ok.bj@163.com', 'prvs=3615340a2=grazyna_pilatowicz@exchange.fitnyc.edu', 'nrwbg@ydimrwb.com', 'nqp1336533274671@system.mail', 'notified@ccpfinance.com', 'notification+zj4o29t0fyac@facebookmail.com', 'noreply183@m128.strmae.com', 'nobody@mail2.goodjobs.cn', 'no-replytopo@vip90.finalfselc.com', 'no-reply@lrqa.com', 'newsletter@quwan.com', 'newsletter@24home.com', 'xiu@letter.xiu.com', 'yfmkwn@ezdmpl.gov', 'yanyuanwei@p-s-a.cn', 'yangxia@xhjd.gov.cn', 'yangqianesqc@sohu.com', 'xvxmgq@dlnhdk.org', 'xuanleizrch@yahoo.cn', 'xntuijian@163.com', 'xmvmqmx@vip.sohu.com', 'xkwoh@mx1813.6711fcse.com', 'xkeuvyqu@fbs.net', 'xkcltcs8.126@daum.net', 'xkcgzxy@sunnychinese.com', 'xkc17@daum.net', 'yinchao@holpe.net', 'xiu-eu@mail001.xiu.com', 'xinkechengzwx@zjscedu.org', 'xinkechengzwh1@4008844442.net', 'xinkechengybx@ybxez.com', 'xinkechengxxzj@xxzj.com.cn', 'xinkechengmch@hkjulong.com', 'xinkechengmch@ewitgroup.com', 'xinkechengmch1@bojia.net.cn', 'xinkechengmch14@lyc.com.cn', 'xinkechengl123654@shimaocopper.com', 'xinkechengjin01@starwl.net', 'xinkechengjin01@eskin.cn', 'xinkechengbijibp@bjxzgw.gov.cn', 'zhjsdq@sina.com', 'zxauoeoie@everestlimited.co.uk', 'zuodan1@mail.wztvu.cn', 'ztesodmoi@esrogworld.com', 'zsw@dac.org.cn', 'zs2wdwec@yeah.net', 'zlq@zjfr.com', 'zlnchc@quctpk.gov', 'zkz2007@linzon.ru', 'zjy@flyerp.com', 'zjgbvlvz@ndx.org', 'zijin@ql.com.cn', 'zigc@jbuzhxxn.com', 'zhouxians@couhum.com', 'xinkecheng_wang@daum.net', 'zhinian@hkjulong.com', 'zhaopin_nj@chinesemedia.com.cn', 'zhanwaibao@moon.sinomrkt.com', 'zhanwaibao@gmail.com', 'zhangll1@ahyc.com.cn', 'yuesuixinxdong@zsepower.com.cn', 'yuanyupeng@toefljuniorchina.com', 'youyi@uiyi.webmrkter.com', 'youxiuqikan@ql.com.cn', 'yongju17@sina.com', 'ykdlqtj@etekmetal.com', 'yjkfs@ufavhr.com', 'yiqifar1@eqifa.com', 'tada66hyj@ruyi.com', 'uhz1331355980121@system.mail', 'uhysjpmetmjklde@yeah.net', 'ualqp@zjrs.gov.cn', 'tqsgbr6037@gmail.com', 'toy@glip.com.cn', 'tolme@longbank.com.cn', 'tmvwltbb@praazy.com', 'thoyph@gdzisi.gov', 'tgbtee@cthlsh.gov', 'test@jsbowerfoundation.org', 'tear12286@tom.com', 'teacher3047@hzcom.cn', 'tailor@kyff-trans.de', 'unhelpful@dg.scsalud.es', 'sxchns@nsxch.com', 'swspx@cslg.cn', 'support@svnet.com.cn', 'support@germanpod101.com', 'support@bluefx.net', 'super@xtuone.sendcloud.org', 'sunchao@bdahc.com', 'suggest@ncplaza.cn', 'stone@szhitong.com', 'sonstenes@elginbowlinglanes.ca', 'snqc@mx1915.mqrebfg.com', 'shuyf@autek.cn', 'lvsngo@ubmwqx.gov', 'webmaster@fashionmag.com', 'xinkecheng33@hr33.net', 'xiaozhuang@chinascyl.com', 'xianren@kingfengshen.com', 'xaupee@tdbyrx.org', 'xahr@worldunion.com.cn', 'wwxxyyz@intl.com', 'wvo@eplanetit.net', 'wowotuan-edm@55tuan.com', 'wf4wqmz85gf@yglxcvyvwuny.com', 'wei86qiangliu@tom.com', 'weekly8@noreply.dangdang.com', 'weekly5@noreply.dangdang.com', 'weekly1@noreply.dangdang.com', 'shenjidnkj@yahoo.cn', 
                'webmaster@cshongrun.com', 'webmaster@cotswold-window.com.hk', 'wangxueling123@haian.gov.cn', 'wangxueling0001@haian.gov.cn', 'wangxing12@sdsj.com', 'wangchengxi@longriver.cn', 'w10120517@sdhj.com.cn', 'w10120517@jxdpf.gov.cn', 'vyqbelte@einsteinmms.com', 'vvfoefycey@grupo-aguilar.com', 'vaglrxd@otzek.com', 'unktxm@jzmgvv.org', 'chairs@56youk.ef.com', 'daysinnsz@daysinnsz.com', 'daniel@vipedm.com', 'daixiang@nbip.net', 'daemon300@163.com', 'cz@huiyuangongyu.com.cn', 'csfyb@naver.com', 'couple@u.xiuxian.com', 'cnesle@tryjev.gov', 'clampitt_cm@yahoo.com.mx', 'ciaik053@yahoo.es', 'chenfei@samic.com.cn', 'chenfei@cquae.com', 'chendy@cssc.com.cn', 'dbank068@vip1.dbank.com', 'cdwqtti@primaconsultants.com.sa', 'cdesf@staff.soufun.com', 'callose@abzaustria.at', 'bzeic-kr@xj.cninfo.net', 'bxgan@zhmo.linsh.com', 'business@public.xa.sn.cn', 'burasuta_man@yahoo.com', 'buoqu@mincloud.com', 'btv1==419428cff6b==wwxxyyz@intl.com', 'btv1==37875664ebf==hyj@atmb.cn', 'bsdzd@baoshan.cn', 'bs@equipmentspecialists.com', 'bowei@bo-wei.com.cn', 'eb@mlr.com', 'florentinoaqge3n@yahoo.com.tw', 'firedragon625@yahoo.com', 'fengling@system.mail', 'fckbkqzhoky@sina.cn', 'faxsky@taikang.com', 'fanrry-6o55512619@lk6.k6hui.net', 'fangebo0519@sogou.com', 'f702@otz.com', 'export@thaitaiyo.co.th', 'employment@ourmysteryshopper.com', 'elong@elongmail.com', 'edwin1391@hotmail.com', 'edit@idwindow.com', 'book@jxdpf.gov.cn', 'dzzyqn@roalgb.org', 'dvowwn@rpijai.org', 'dukegny@espressocafe.bg', 'duba@kingsoft.com', 'dream@bankinfo53.standardcharted.com.cn', 'dream@bankinfo24.standardcharted.com.cn', 'donotreply@wordpress.com', 'dong@risho.cn', 'dmb@gxrb.com.cn', 'dingyue@bang17.zaobang.com', 'dingbo@dingbolw.com', 'dfi1330533199338@system.mail', 'derbyjones77123@mail2.aibangtuan.com', '34130396@163.com', 'jason@indianair.net', 'irma@8email.com', 'iris@zhutuiqi.com', 'info@fevia.be', 'ge81ec@380009188.com.cn', 'grazyna_pilatowicz@exchange.fitnyc.edu', 'qpjtm@[211.157.4.2]', '8service@cdndns.cn', '89613391@sd-wit.com', '409171@mjrg.net', '3vcphtgwjct0zsgdmzlzhkbmflzhk.bnl286660566pp.bnl@m3kw2wvrgufz5godrsrytgd7.apphosting.bounces.google.com', 'asfr@xx5.51pidai.info', 'omar@mofaspace.info', '2653901882@qq.com', '2425124557@qq.com', '21stcentury@lh52.huitech.net', '21stcentury@21st.webmrkter.com', '21stcentury-2o102254337@eg10.ecworlds.com', '204@bolejob.com', '18603656133@wo.com.cn', '153@bolejob.com', '13002400245@e130133.com', '1264819672@qq.com', '10service@780666.com', '10000@sh1892.cn', '00@sdyingcai.com', 'alfrecastro@yahoo.com.ar', 'bo@htxx.com.cn', 'bo-bwj23ksbfs00z5au7xxxsbymfc3tzv@b.q.viplad.com', 'bkjs75@yahoo.cn', 'bjsqf@sohu.com', 'bj55tuan@new28.new55tuan.com', 'bin@mail.qdcatv.com.cn', 'bianjislz@naver.com', 'bianjibu@jxdpf.gov.cn', 'bianji@chinascyl.com', 'basa97262@yahoo.com.my', 'avdhoot@cactimedia.com', 'atqxsbadn@163.com', 'aqwer@sohu.com', 'fpj111@jzxx.net', 'akwfkmmwvpvn@sina.com', 'ajdaoyfipqkh@sina.com', 'admin@system.mail', 'admin@apcmchina.com.cn', 'adc1336035820502@system.mail', 'actividades@polonortemdq.com.ar', 'accounting@calarm.cn', 'a@jobdu.com', 'vipshop@q.viplad.com', 'test@jsbowerfoundation.org', 'stanley@mofaspace.info', 'phil@mofaspace.info', 'jlbwis@mfpwsl.org', 'karrcm@carolina.rr.com', 'kangnanyide456941@163.com', 'kamklkk1984@sohu.com', 'kaemux@fjauzg.org', 'jyxq@xj169.com', 'jyujyu26@yahoo.cn', 'jyqy17@yahoo.cn', 'jykc50@yahoo.cn', 'jxb@hhzq.com', 'jsji28@sina.cn', 'job0917@job0917.com', 'jmkevegsi@excalibursystems.net', 'jlcfe1981@sohu.com', 'karsh@hilit.net', 'jkoiu9@daum.net', 'jjjqfcz@mail.colombiaaprende.edu.co', 'jizhong@fengle.com.cn', 'jitxuu@lchyqa.org', 'jinxia123@xhschool.com', 'jinxia123@sdan.com.cn', 'jie.kang14441@googlemail.com', 'jiaoyuqy73@yahoo.cn', 'jiaoyubaijia01@system.mail', 'jiaoguanlun@sogou.com', 'jiangsj@cneucc.cn', 'jiangli@createver.com', 'jenifferknowles@s8.coowo.com', 'lina@china-ah.com', 'luxj@orient-hongye.com', 'lsz@yeehao.net', 'lovefu3002@72hr.cn', 'louzl@zjjmw.gov.cn', 'lou14562@yahoo.co.id', 'lllmn@beautionplus.co.kr', 'lizhengyue@land.net.cn', 'liuxue0100@sjzdrc.gov.cn', 'liuxue001@sjzdrc.gov.cn', 'liushen92573@m016.caishi.info', 'lisa@maymullet.info', 'lingyungo@libra.wuxiedm.com', 'jcum@elkonkonka.com', 'lim@esonex.com.hk', 'lil@tup.tsinghua.edu.cn', 'life@r1.weibo.travelzoo.com', 'li-jia@telecomjs.com', 'lhkwzj@cuelrr.com', 'kyc@hfuu.edu.cn', 'kropfi5@yahoo.com', 'kou1330184497406@system.mail', 'koehlinha@yahoo.com', 'kju1330315067953@system.mail', 'kf@wyx173.com', 'kevingu@zinch.com', 'gxf@ufida.com.cn', 'hr@motech.cn', 'honghua@21fj.com', 'hfwjsjm@21cn.net', 'hetian7787@gmail.com', 'hengyi@3see.com', 'hd@boloni.cn', 'hatnuk@houtcz.org', 'hasansoz@uludag.edu.tr', 'hanbingyiye@shol.org.cn', 'hanbingyiye@email.jsca.com.cn', 'hamptondaly@yahoo.com', 'halujiaoyu@126.com', 'gywtxc@371.net', 'hrh3_cd@xiaotong.com.cn', 'gxcgdp@wdynbf.org', 'gummiebear1115@yahoo.com', 'gm123@lanshan.net', 'giancarlo.peli@digitalsynapsis.tv', 'geili@service.geili360.com', 'geili360@mkt.emdeliver.net', 'geili360@huiyee.webmrkter.com', 'gcl@ldclean.cn', 'fzoysxlbt@google.com', 'fzkd@fzkd.net.cn', 'fuuwxf@vlybgh.org', 'frzwqw@ifkjhh.gov', 'fqac2000@public.fz.fj.cn', 'imat@imat.com.mx', 'iro1330694789109@system.mail', 'invite@30secs57.winenice.com', 'invite@30secs43.winenice.com', 'info@wjwy.com', 'info@moversdirectory.com', 'info@kgsgbank.co.in', 'info@kangva.com', 'info@churrascariaplataforma.com', 'indurate@ugogroup.co.uk', 'lwm@nfc.sh', 'ikykgl@sdztjg.gov', 'ikj1330798239140@system.mail', 'iaobj@iao.com.cn', 'hysa@growelsoftech.com', 'hyj@atmb.cn', 'huyu@jkang8.com', 'huoxiaohua@igowei.com', 'huntermail@hun.huntermail-sender.com', 'huashun@hslace.com', 'huaiyin@jnnc.com', 'hsyqbipai@gottfriedville.net', 'hs.liu@sofima.cn', 'onlooker@tacit.jiaobuser.com', 'pmail@pospay.mnpyq.com', 'brown@green.jiaobuser.com', 'buckle@whop.sentfuli.com', 'lakala@pospay.zoorea.com', 'memberclub.club@samsung.com', 'vild@creadit.eastyan.com', 'hurry@modpos.xijiga.com', 'root@hxxyk.eastyan.com', 'lakala@pospay.moutor.com', 'list@yidopay.wudgang.com', 'inform@lakalapos.cosemail.cn', 'lishua@contact.cosemp.com', 'lakala@gift.seakpy.com', 'info@baidu.wudgang.com', 'youqian@baidu.whornn.com', 'box@poszf.wdgan.com', 'lkl@pospay.copeter.com', 'youqianhua@info.cosemp.com', 'tyf@matu.cossend.com', 'newsletter@newsletter.aliyun.com', 'root@yidopay.caidewang.com', 'pmail@pospay.mnpyq.com', 'jwubh@evuadmin.n5wgqx.cyou']
            return desktop_path,block_list
    exit('系统版本不支持')

def v1block(block_list,sid,cookie):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "%s"%cookie,
        "Host": "mail.qq.com",
        "Origin": "https://mail.qq.com",
        "Referer": "https://mail.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
    }
    url = 'https://mail.qq.com/cgi-bin/config_blackwhitelist?sid=%s'%sid
    fail_list = []
    fail_times = 0
    for i in range(0,len(block_list)):
        mail_addr = block_list[i]
        data = {
            'sid':'%s'%sid,
            'act':'blacklist',
            'Fun':'submit',
            'confirm':'0',
            'group':'%s'%mail_addr
        }
        if fail_times > 2:
            fail_list.append(mail_addr)
        else:
            req = requests.post(url=url,data=data,headers=headers)
            content_length = len(req.content)
            if content_length != 604: #QQ邮箱拉黑操作成功返回的内容长度是固定的，以此判断是否成功
                print('\n%s 拉黑失败，继续操作中……'%mail_addr)
                fail_times += 1
                fail_list.append(mail_addr)
            else:
                print('\n第%i个邮箱 %s 已拉黑！'%(i+1,mail_addr))
                time.sleep(2) #避免请求过快，每次请求间隔2秒
    fail(fail_list)
    return

def v2block(block_list,sid,cookie,r):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": "%s"%cookie,
        "Host": "wx.mail.qq.com",
        "Origin": "https://wx.mail.qq.com",
        "Referer": "https://wx.mail.qq.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56",
    }
    url = 'https://wx.mail.qq.com/setting/blackwhitelist?sid=%s&r=%s'%(sid,r)
    fail_list = []
    fail_times = 0
    for i in range(0,len(block_list)):
        mail_addr = block_list[i]
        data = {
            'func':'2',
            'addr_type':'1',
            'addrs':'%s'%mail_addr
        }
        if fail_times > 2:
            fail_list.append(mail_addr)
        else:
            req = requests.post(url=url,data=data,headers=headers).json()['head']
            if req['ret'] != 0: #新版QQ邮箱拉黑成功返回的ret参数是0
                print('\n%s 拉黑失败，继续操作中……错误信息：%s'%(mail_addr,req['msg']))
                fail_times += 1
                fail_list.append(mail_addr)
            else:
                print('\n第%i个邮箱 %s 已拉黑！'%(i+1,mail_addr))
                time.sleep(2) #避免请求过快，每次请求间隔2秒
    fail(fail_list)
    return 

def fail(fail_list):
    total = len(fail_list)
    if total > 0:
        print('\n剩余未拉黑的黑名单数量：%i 个\n'%total)
        fail_list_path = os.path.join(desktop_path,'fail_list.txt')
        with open(fail_list_path,'w+') as file:
            file.write(str(fail_list))
            exit('未拉黑的邮箱列表已保存至桌面')
    exit('黑名单内邮箱地址均已拉黑！')
    return '全部操作完成'

if __name__ == '__main__':
    sid = input('\n请粘贴sid：')
    cookie = input('\n请粘贴cookie：')
    desktop_path = syscheck()[0]
    block_list = syscheck()[1]
    os.system('cls')
    while True:
        print('\n请选择QQ邮箱版本，根据邮箱网址判断\n')
        select_ver = input('1.网址以mail开头 2.网址以WX开头：')
        if select_ver == '1':
            v1block(block_list,sid,cookie)
        elif select_ver == '2':
            r = input('\n请输入参数r的数据：')
            while len(r) < 26:
                r = input('\n参数错误，请重新输入参数r的数据：')
            v2block(block_list,sid,cookie,r)
        else:
            print('\n***** 输入无效，请重新输入1或2 *****')
