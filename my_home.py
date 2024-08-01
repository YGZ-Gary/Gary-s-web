'''主页'''
import streamlit as st
from PIL import Image
import pandas as pd
page=st.sidebar.radio('朕的首页',['兴趣推荐','图片处理工具','词典','留言区','网页跳转','知识答题'])
def page1():
    '''兴趣推荐'''
    choice = st.radio(
    '选择：',
    ['推荐1', '推荐2', '推荐3'],
    captions=['小说', '运动', '编程']
    )
    if choice=='推荐1':
        st.write("小说推荐")
        st.write("三体(THREE BODY)")
        st.text('《三体》是刘慈欣创作的长篇科幻小说系列，由《三体》《三体2：黑暗森林》《三体3：死神永生》组成 ')
        st.text("作品讲述了地球人类文明和三体文明的信息交流、生死搏杀及两个文明在宇宙中的兴衰历程。")
        st.text("通过对人类中心主义的解构，继而完成对人与自然、动物之间的伦理反思与文学表达，最终指向去人类中心化的思想内核。")
        st.image("tb.jpg")
    if choice=='推荐2':
        st.write('羽毛球')
        st.text("羽毛球是一项备受欢迎的体育运动，")
        st.text('它不仅能够增强体魄，还能够帮助缓解视力疲劳。')
        st.text('羽毛球起源于14-15世纪的日本，现代羽毛球运动起源于印度，形成于英国。')
        st.text('羽毛球比赛通常分为单打和双打两种形式。')
        st.text('比赛中，运动员隔网站立，用球拍击打羽毛球，运用发球、击球和移动等战术，将球在网上往返对击。')
        st.image('bd.jpg')
        st.write('详见羽球协会官网')
        st.link_button('go',"https://www.cba.org.cn/")
    if choice=='推荐3':
        st.write('编程')
        st.text('编程是一种理性认知并表达世界的语言，学习编程不仅可以帮助人们理解计算机，\n更能用其中的逻辑指导学习生活的各方面，\n成为有思维条理、有独立判断、有探索能力的真正创作者')
        st.text('目前市面上主流的编程语言有多种，其中Python是最流行的编程语言之一，\n被广泛运用在人工智能、Web开发等领域。')
        st.image('bc.jpg')
def page2():
    '''图片处理工具'''
    st.write(":sunglasses:奏始皇的图片处理:sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        ori=st.toggle('原图')
        ch=st.toggle('反色')
        bw = st.toggle('黑白滤镜')
        co = st.toggle('增强对比度')
        if ori:
            o=st.image(img)
        if ch:
            c=st.image(img_change(img,2,0,1))
        if bw:
            b=st.image(img_change(img,0,0,0))
        if co:
            B=st.image(img_change(img,1,2,0))
        o,c,b,B=st.columns([1,1,1,1])
        # tab1,tab2,tab3,tab4,tab5,tab6=st.tabs(["原图","改色1","改色2","改色3","改色4","改色5"])
        # with tab1:
        #     st.image(img)
        # with tab2:
        #     st.image(img_change(img,0,2,1))
        # with tab3:
        #     st.image(img_change(img,1,2,0))
        # with tab4:
        #     st.image(img_change(img,1,0,2))
        # with tab5:
        #     st.image(img_change(img,2,0,1))
        # with tab6:
        #     st.image(img_change(img,2,1,0))
        
def page3():
    '''词典'''
    st.write("智会词典")
    with open('words_space.txt','r',encoding="utf-8") as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split("#")
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('输单词谢谢')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open("check_out_times.txt",'w',encoding='utf-8') as f:
            message=' '
            for k,v in times_dict.items():
                message+=str(k)+'#'+str(v) + '\n'
            message=message[:-1]
            f.write(message)
        st.write('查询次数: ',times_dict[n])
        if word=='python':
            st.balloons()
            st.code('''
                    #彩蛋！！！，送你一行python代码
                    print('hello world')''')
        if word=='pull':
            st.balloons()
            st.code('''
                    #彩蛋！！！，送你一段音频(戴上耳机聆听效果更加【doge)''')
            with open("飞机空难警报铃声_耳聆网_[声音ID：33980].mp3","rb") as f:
                music1=f.read()
            st.audio(music1,format="audio/mp3",start_time=0)
        if word=='oh':
            st.code('''查看发音''')
            with open("oh.mp3","rb") as f:
                music2=f.read()
            st.audio(music2,format="audio/mp3",start_time=0)
        if word=='FBI':
            st.balloons()
            st.code('''
                    #彩蛋！！！，送你一段音频''')
            with open("fbi.wav","rb") as f:
                music3=f.read()
            st.audio(music3,format="audio/mp3",start_time=0)
def page4():
    '''留言区'''
    st.write('留言区')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list=f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i]=messages_list[i].split('#')
    for i in messages_list:
        if i[1]=="Up":
            with st.chat_message('⭐🆙'):
                st.write(i[1],':',i[2],"   <Up>®️")
        elif i[1]=="NPC_1":
            with st.chat_message('1️⃣'):
                st.write(i[1],':',i[2])
    name=st.selectbox('我是...',['Up','NPC_1'])
    new_message=st.text_input('请speak...')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message=' '
            for i in messages_list:
                message+=i[0]+'#'+i[1]+'#'+i[2]+'\n'
            message=message[:-1]
            f.write(message)
        
    st.video("kms.mp4", format='video/mp4', start_time=0)
def page5():
    st.write('网页跳转')
    co1,co2,co3,co4=st.columns([1,1,1,1])
    with co1:
        st.link_button('百度',"https://www.baidu.com/")
        st.link_button('B站',"https://www.bilibili.com/")
        st.link_button('知乎',"https://www.zhihu.com/")
    with co2:
        st.link_button('优酷',"https://www.youku.com/")
        st.link_button('微博',"https://weibo.com/")
        st.link_button('豆瓣',"https://www.douban.com/")
    with co3:
        st.link_button('QQ音乐',"https://y.qq.com/")
        st.link_button('爱奇艺',"https://www.iqiyi.com/")
        st.link_button('腾讯视频',"https://v.qq.com/")
    with co4:
        st.link_button('中国教育在线',"https://www.eol.cn/")
        st.link_button('中国新闻网',"http://www.chinanews.com/")
        st.link_button('编程猫社区',"https://shequ.codemao.cn/" )
        st.link_button('github','https://github.com/')
 
    # go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    # if go == '我的贴吧':
    #     st.link_button('帮我盖楼', 'https://www.baidu.com/')
    # elif go == '我的bilibili':
    #     st.link_button('帮我一键三连', 'https://www.bilibili.com/')
def page6():
    n=0
    st.write('网络知识竞答')
    choices = st.radio(
    '选择：',
    ['第一题', '第二题', '第三题','第四题']
    )
    if choices=='第一题':
        st.write('本up的网名是什么？')
        cb1 = st.checkbox('GARY')
        cb2 = st.checkbox('奏始皇')
        cb3 = st.checkbox('bullsht')
        cb4 = st.checkbox('一只在CAT 3 landing的 \n CATHAY PACIFIC A-350 1000')
        l = [cb1, cb2, cb3, cb4]
        if st.button('确认答案'):
            if True in l:
                st.write('你过关')
                n+=25
            else:
                st.write('该罚！')
    st.write('您的分数：',n)  
    if choices=='第二题':  
        st.write('油管是什么？(单选)')
        cb11 = st.checkbox('‘北溪2’天然气管道')
        cb21 = st.checkbox('Google')
        cb31 = st.checkbox('youtube')
        cb41= st.checkbox('你的吸管')
        l = [cb31]
        if st.button('确认答案'):
            if True in l:
                st.write('你过关')
                n+=25
            else:
                st.write('该罚！')
    st.write('您的分数：',n)       
    if choices=='第三题':     
        st.write('石油会滋生什么？(单选)')
        cb111 = st.checkbox('细菌')
        cb211 = st.checkbox('美菌')
        cb311 = st.checkbox('钱')
        cb411= st.checkbox('金坷垃')
        l = [cb211]
        if st.button('确认答案'):
            if True in l:
                st.write('你过关')
                n+=25
            else:
                st.write('该罚！')
    st.write('您的分数：',n)         
    if choices=='第四题': 
        st.write('波音767重型客机是什么？(单选)')
        cb1111 = st.checkbox('由美国Boeing公司制造的长程宽体客机')
        cb2111 = st.checkbox('Air Canada flight 143 的专属滑翔机')
        cb3111 = st.checkbox('它停产了')
        cb4111= st.checkbox('能够毙敌2000多人的重型巡飞弹')
        l = [cb4111]
        if st.button('确认答案'):
            if True in l:
                st.write('你过关')
                n+=25
            else:
                st.write('该罚！')
             
    st.write('您的分数：',n)
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array=img.load()
    for x in range(width):
        for y in range(height):
            r=img_array[x,y][rc]
            g=img_array[x,y][gc]
            b=img_array[x,y][bc]
            img_array[x,y]=(g,r,b)
    return img


if page=="兴趣推荐":
    page1()
elif page=='图片处理工具':
    page2()
elif page=='词典':
    page3()
elif page=='留言区':
    page4()
elif page=='网页跳转':
    page5()
elif page=='知识答题':
    page6()