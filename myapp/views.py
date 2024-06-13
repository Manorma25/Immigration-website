from django.shortcuts import render,redirect
from myapp.models import FAQ 
from myapp.models import myreview
from myapp.models import helpsupport
from myapp.models import Contact
from myapp.models import user_register
from myapp.models import visa_type
from myapp.models import blogs
from myapp.models import country
from myapp.models import con_visa_details
from myapp.models import coaching
from myapp.models import eligible
from django.conf import settings
from django.core.mail import send_mail
import datetime
from datetime import date
from newsapi.newsapi_client import NewsApiClient
import pandas as pd
#import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import country_converter as coco

# Create your views here.


def log(request):
    if request.method=="POST":
        email=request.POST.get('em')
        password=request.POST.get('pw')
        expert=user_register.objects.filter(em = email,pw = password)
        k=len(expert)
        if k>0:
            request.session['em']=email
            return redirect('/Dashboard')
        else:
          
            return render(request,'login1.html',{'msg':"Invalid Candidate"})
    else:
        return render(request,"login1.html")


def reg(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('cpassword')
        if user_register.objects.filter(em=email).exists():
           return render(request,'register1.html',{'ms':1})
        else:
            if password==confirm_password:
                x=user_register()
                x.nm=name
                x.em=email
                x.pw=password
                x.cpw=confirm_password
                x.save()
               
                return render(request,'register1.html',{'ms':2})
            else:
               return render(request,'register1.html',{'ms':3})
    else:
        return render(request,'register1.html')


def contact(request):
    if request.method=="POST":
        x=Contact()
        x.first_name=request.POST.get('fn')
        x.last_name=request.POST.get('ln')
        x.phone=request.POST.get('ph')
        x.email=request.POST.get('email')
        x.subject=request.POST.get('sub')
        x.website=request.POST.get('web')
        x.message=request.POST.get('msg')
        x.save()
        return render(request,'contactus.html',{'succ':1})
    else:
        return render(request,'contactus.html')
    
def change(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    if request.method=='POST':
        re=user_register.objects.get(em=request.session['em'])
        opassword=request.POST.get('o_password')
        npassword=request.POST.get('n_password')
        cpassword=request.POST.get('c_password')
        
        if(npassword==cpassword):
            pa=re.pw
            print(pa)
            if(opassword==pa):
                re.pw=npassword
                re.save()
                rest="Password Changed"
                return render(request,'change password.html',{'rest':rest})
            else:
                res="Invalid current Password"
                return render(request,'change password.html',{'res':res})
        else:
            res="Confirm password and new password don't match" 
            return render(request,'change password.html',{'res':res})

    else:
        return render(request,'change password.html')       


def foot(request):
    return render(request,'footer copy.html')

def forgot(request):
    if (request.method=='POST'):
        em=request.POST.get('email')
        user=user_register.objects.filter(em=em)
        if(len(user)>0):
            password=user[0].pw
            subject="Password"
            message="Welcome! Your password is"+password
            email_from=settings.EMAIL_HOST_USER
            recipient_list=[em]
            send_mail(subject,message,email_from,recipient_list)
            res="Your password sent to your respective email account"
            return render(request,'forgot.html',{'rest':res})
        else:
            rest='This Email Id is not registered'
            return render(request,'forgot.html',{'res':rest})
    else:
        return render(request,'forgot.html')

 
def hs(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    if request.method=="POST":
        x=helpsupport()
        x.title=request.POST.get('title')
        x.message=request.POST.get('msg')
        x.save()
        return render(request,'help&support.html',{'succ':"data succ added"})
    else:
        return render(request,'help&support.html')
    
def index(request):
    data=visa_type.objects.all()
    res_coach=coaching.objects.all()
    res_blog=blogs.objects.all()
    if request.method=="POST":
        x=eligible()
        x.fname=request.POST.get('fn')
        x.lname=request.POST.get('ln')
        x.email=request.POST.get('em')
        x.phone=request.POST.get('ph')
        x.status=request.POST.get('marital status')
        x.ocuupation=request.POST.get('occupation')
        x.cont=request.POST.get('country')
        x.visa=request.POST.get('visa')
        x.save()

        name=x.fname
        email=x.email
        subject="Eligible"
        email_from=settings.EMAIL_HOST_USER
        message="You are eligible"+name
        receiver=[email]
        send_mail(subject,email_from,message,receiver)
        rest="Check your email for confirmation"
        return render(request,'index.html',{rest:'rest','data':data,'res_coach':res_coach,'res_blog':res_blog})

    return render(request,'index.html',{'data':data,'res_coach':res_coach,'res_blog':res_blog})

def side(request):
    return render(request,'sidebar.html')

def base(request):
    return render(request,'base.html')

def faq(request):
    data=FAQ.objects.all()
    return render(request,'view_faq.html',{'data':data})


def review(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    if request.method=="POST":
        x=myreview()
        x.title=request.POST.get('title')
        x.message=request.POST.get('msg')
        x.save()
        return render(request,'review.html',{'succ':"data succ added"})
    else:
        return render(request,'review.html')
    
def edit(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    user=user_register.objects.get(em=request.session['em'])
    if request.method=="POST":
       user=user_register.objects.get(em=request.session['em'])
       user.nm=request.POST.get('name')
       user.birthday=request.POST.get('birthday')
       user.state=request.POST.get('state')
       user.country=request.POST.get('country')
       user.pincode=request.POST.get('pincode')
       user.contact=request.POST.get('contact')
       user.gender=request.POST.get('gender')
       user.qualifications=request.POST.get('qualifications')
       user.address=request.POST.get('address')
       user.hobbies=request.POST.get('hobby')

       user.save()
       return redirect('/User')
    else:
        return render(request,'edit_profile.html',{'user':user})
       

def u_profile(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    user=user_register.objects.get(em=request.session['em'])
    if request.method=="POST":
       print("yes")
       user.image=request.FILES['file1']
       user.save()
       return render(request,'user_profile.html',{'user':user,'msg':'success'})

    else:   
     return render(request,'user_profile.html',{'user':user})
    
"""
def handle_uploades_file():
   destination=open() """   

"""def Userprof(request):
     if not request.session.has_key('email'):
          return redirect('/Login')
     user=register.objects.get(email=request.session['email'])
     if request.method == "POST":
          print("yes")
          user.profile=request.FILES['file1']
          user.save()
          ----x=request.FILES['file1']
          print("=====================",x)
          import os
          import numpy as np 
          s=os.getcwd(x)
          print(s)----
          return render(request,'userprofile.html',{'user':user,'msg':'success'})

     else:
          return render(request,'userprofile.html',{'user':user})  """  
      

def logout(request):
    if not request.session.has_key('em'):
        return redirect('/Login')
    del request.session['em']
    return redirect('/Login')  

def blog(request):
    data=blogs.objects.all()
    return render(request,'blog.html',{'data':data})
       
       
def detail_blog(request,id):
    data=blogs.objects.get(id=id)
    return render(request,'detail_blog.html',{'data':data}) 

def visa(request):
    data=visa_type.objects.all()
    return render(request,'visa.html',{'data':data})

def visa_detail(request,id):
    data=visa_type.objects.get(id=id)
    return render(request,'visa_detail.html',{'data':data})

def coach(request):
    data=coaching.objects.all()
    return render(request,'coach.html',{'data':data})

def coach_details(request,id):
    item=coaching.objects.all()
    data=coaching.objects.get(id=id)
    return render(request,'coach_details.html',{'data':data,'item':item})

def cont(request):
    data=country.objects.all()
    return render(request,'country.html',{'data':data})

def cont_details(request,name):
    data=con_visa_details.objects.filter(country_name=name)
    return render(request,'country_details.html',{'data':data})

def cont_details2(request,name):
    data=con_visa_details.objects.get(headings=name)
    return render(request,'country_details2.html',{'data':data})

def news(request):
    newsapi=NewsApiClient(api_key='f4320b784efe46a29853f60a42802b92')
    json_data=newsapi.get_everything(q='Abroad students',
    language='en',
    from_param=str(date.today()-datetime.timedelta(days=29)),
    to=str(date.today()),
    page_size=24,
    page=2,
    sort_by='relevancy'
 )
    
    k=json_data['articles']
    return render(request,'news.html',{'k':k})



def happiness(request):
    return render(request,'happiness_analysis.html')

def happy1(request):
    if request.method=='POST':
        df=pd.read_csv('happiness.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        fig=px.line(dfa, x="Year", y="Happiness Index",title='happiness-index')
        graph=fig.to_html()
        return render(request,'happy1.html',{'graph':graph})
    else:
        return render(request,'happy1.html')
    
    
def happy2(request):
    if request.method=='POST':
        df=pd.read_csv('happiness.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        year1=int(request.POST.get('Syear'))
        year2=int(request.POST.get('Eyear'))
        dff=dfa[(dfa['Year']>=year1)&(dfa['Year']<=year2)]
        fig=px.line(dff, x="Year", y="Happiness Index",title='Happiness Index',text='Year')
        fig.update_traces(textposition="top right")
        graph=fig.to_html()
        return render(request,'happy2.html',{'graph':graph})
    else:
        return render(request,'happy2.html')
    

def happy3(request):
   if request.method=='POST':  
    df=pd.read_csv('happiness.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Happiness Index'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Happiness Index'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Happiness Index in both countries',
                      xaxis_title='Year',
                      yaxis_title='Happiness Index')
    graph=fig.to_html
    return render(request,'happy3.html',{'graph':graph})
   else:
      return render(request,'happy3.html')
    
def happy4(request):
  if request.method=='POST':  
    df=pd.read_csv('happiness.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Happiness Index'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Happiness Index'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Happiness Index in both countries',
                      xaxis_title='Year',
                      yaxis_title='gross-national-income')
    graph=fig.to_html
    return render(request,'happy4.html',{'graph':graph})
  else:
      return render(request,'happy4.html')
    

def happy5(request):
  if request.method=='POST':  
    df=pd.read_csv('happiness.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Happiness Index'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Happiness Index'],
                             mode='lines+markers',name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'],y=df3['Happiness Index'],
                             mode='lines+markers',name=c3))
    fig.update_layout(title='Happiness Index in following countries',
                      xaxis_title='Year',
                      yaxis_title='happiness-index')
    graph=fig.to_html()
    return render(request,'happy5.html',{'graph':graph})
  else:
    return render(request,'happy5.html')
   

def happy6(request):
   if request.method=='POST':  
    df=pd.read_csv('happiness.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    df3=df3[(df3['Year']>=year1)&(df3['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Happiness Index'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Happiness Index'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Happiness Index'],
                              mode='lines+markers', name=c3))
    fig.update_layout(title='Happiness Index in following countries',
                      xaxis_title='Year',
                      yaxis_title='happiness-index')
    graph=fig.to_html()
    
    return render(request,'happy6.html',{'graph':graph})
   else:
    return render(request,'happy6.html')

def happy7(request):
    if request.method=='POST':
        df=pd.read_csv('happiness.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Happiness Index')
        n=int(request.POST.get('cn'))
        dfmax=df1.tail(n)
        fig=px.bar(dfmax, x='Entity', y='Happiness Index', text_auto='.2s',
                   title="Happiness Index in no of countries")
        graph=fig.to_html()
        return render(request,'happy7.html',{'graph':graph})
    else:
        return render(request,'happy7.html')
    

def happy8(request):
    if request.method=='POST':
        df=pd.read_csv('happiness.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Happiness Index')
        n=int(request.POST.get('cn'))
        dfmin=df1.head(n)
        fig=px.bar(dfmin, x='Entity', y='Happiness Index', text_auto='.2s',
                   title="Happiness Index in no of countries")
        graph=fig.to_html()
        return render(request,'happy8.html',{'graph':graph})
    else:
        return render(request,'happy8.html')

def happy9(request):
    if request.method=='POST':
        df=pd.read_csv('happiness.csv')
        cc=coco.CountryConverter()
        df['Entity-codes']=coco.convert(names=df['Code'], to='ISO3')
        print(df['Entity-codes'])
        fig=px.scatter_geo(df, locations="Entity-codes", color="Year",
                           hover_name="Entity", size="Happiness Index",
                           animation_frame="Year",
                           projection="natural earth")
        year=request.POST.get('year')
        graph=fig.to_html()
        return render(request,'happy9.html',{'graph':graph})
    else:
        return render(request,'happy9.html')
    

def happy10(request):
    if request.method=='POST':
       df=pd.read_csv('happiness.csv')
       country=request.POST.get('country')
       dfc=df[df['Entity']==country]
       year1=int(request.POST.get('Syear'))
       year2=int(request.POST.get('Eyear'))
       dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
       fig=px.scatter(dfc, x="Year", y="Happiness Index",
                      size="Happiness Index", color="Year",
                      hover_name="Entity", log_x=True, size_max=60, title="Happiness Index")
       graph=fig.to_html()
       return render(request,'happy10.html',{'graph':graph})
    else:
       return render(request,'happy10.html')
    

def gross(request):
    return render(request,'gross_analysis.html')

def gross1(request):
     if request.method=='POST':
        df=pd.read_csv('gross-national-income-per-capita.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        fig=px.line(dfa, x="Year", y="GNI per capita, PPP (constant 2017 international $)",title='GNI PER CAPITA')
        graph=fig.to_html()
        return render(request,'gross1.html',{'graph':graph})
     else:
        return render(request,'gross1.html')

def gross2(request):
     if request.method=='POST':
        df=pd.read_csv('gross-national-income-per-capita.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        year1=int(request.POST.get('Syear'))
        year2=int(request.POST.get('Eyear'))
        dff=dfa[(dfa['Year']>=year1) & (dfa['Year']<=year2)]
        fig=px.line(dff, x="Year", y="GNI per capita, PPP (constant 2017 international $)",title='GNI national income',text='Year')
        fig.update_traces(textposition="top right")
        graph=fig.to_html()
        return render(request,'gross2.html',{'graph':graph})
     else:
        return render(request,'gross2.html')
    

def gross3(request):
  if request.method=='POST':  
    df=pd.read_csv('gross-national-income-per-capita.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines',name=c2))
   
    fig.update_layout(title='Gross National Income per Capita in both countries',
                      xaxis_title='Year',
                      yaxis_title='gross-national-income')
    graph=fig.to_html
    return render(request,'gross3.html',{'graph':graph})
  else:
      return render(request,'gross3.html')

def gross4(request):
  if request.method=='POST':  
    df=pd.read_csv('gross-national-income-per-capita.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Gross National Income per Capita in both countries',
                      xaxis_title='Year',
                      yaxis_title='gross-national-income')
    graph=fig.to_html
    return render(request,'gross4.html',{'graph':graph})
  else:
      return render(request,'gross4.html')
    
def gross5(request):
   if request.method=='POST':  
    df=pd.read_csv('gross-national-income-per-capita.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines+markers',name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'],y=df3['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines+markers',name=c3))
    fig.update_layout(title='Gross National Income in following countries',
                      xaxis_title='Year',
                      yaxis_title='gross-national-income')
    graph=fig.to_html()
    return render(request,'gross5.html',{'graph':graph})
   else:
    return render(request,'gross5.html')
    

def gross6(request):
  if request.method=='POST':  
    df=pd.read_csv('gross-national-income-per-capita.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    df3=df3[(df3['Year']>=year1)&(df3['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['GNI per capita, PPP (constant 2017 international $)'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['GNI per capita, PPP (constant 2017 international $)'],
                              mode='lines+markers', name=c3))
    fig.update_layout(title='Gross National Income in following countries',
                      xaxis_title='Year',
                      yaxis_title='gross-national-income')
    graph=fig.to_html()
    
    return render(request,'gross6.html',{'graph':graph})
  else:
    return render(request,'gross6.html')
      

def gross7(request):
    if request.method=='POST':
        df=pd.read_csv('gross-national-income-per-capita.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='GNI per capita, PPP (constant 2017 international $)')
        n=int(request.POST.get('cn'))
        dfmax=df1.tail(n)
        fig=go.Figure()
        fig=px.bar(dfmax, x='Entity', y='GNI per capita, PPP (constant 2017 international $)', text_auto='.2s', title="Gross National Income in no of countries")
        #country=request.POST.get('country')
        graph=fig.to_html()
        return render(request,'gross7.html',{'graph':graph})
    else:
        return render(request,'gross7.html')

def gross8(request):
    if request.method=='POST':
        df=pd.read_csv('gross-national-income-per-capita.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='GNI per capita, PPP (constant 2017 international $)')
        n=int(request.POST.get('cn'))
        dfmin=df1.head(n)
        fig=px.bar(dfmin, x='Entity', y='GNI per capita, PPP (constant 2017 international $)', text_auto='.2s',
                   title="Gross National Income in no of countries")
        
        graph=fig.to_html()
        return render(request,'gross8.html',{'graph':graph})
    else:
        return render(request,'gross8.html')
    

def gross9(request):
    if request.method=='POST':
        df=pd.read_csv('gross-national-income-per-capita.csv')
        
        df['Entity-codes']=coco.convert(names=df['Code'], to='ISO3')
        print(df['Entity-codes'])
        fig=px.scatter_geo(df, locations="Entity-codes", color="Year",
                           hover_name="Entity", size="GNI per capita, PPP (constant 2017 international $)",
                           animation_frame="Year",
                           projection="natural earth")
        
        graph=fig.to_html()
        return render(request,'gross9.html',{'graph':graph})
    else:
        return render(request,'gross9.html')

def gross10(request):
   if request.method=='POST':
       df=pd.read_csv('gross-national-income-per-capita.csv')
       country=request.POST.get('country')
       dfc=df[df['Entity']==country]
       year1=int(request.POST.get('Syear'))
       year2=int(request.POST.get('Eyear'))
       dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
       fig=px.scatter(dfc, x="Year", y="GNI per capita, PPP (constant 2017 international $)",
                      size="GNI per capita, PPP (constant 2017 international $)", color="Year",
                      hover_name="Entity", log_x=True, size_max=60, title="Gross National Income")
       graph=fig.to_html()
       return render(request,'gross10.html',{'graph':graph})
   else:
       return render(request,'gross10.html')


def human(request):
    return render(request,'human_development_analysis.html')

def human1(request):
    if request.method=='POST':
        print("hello")
        df=pd.read_csv('human-development-index.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        fig=px.line(dfa, x="Year", y="Human Development Index",title='humna-development-index')
        graph=fig.to_html()
        return render(request,'human1.html',{'graph':graph})
    else:
        print("else block")
        return render(request,'human1.html')
    
def human2(request):
    if request.method=='POST':
        df=pd.read_csv('human-development-index.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        year1=int(request.POST.get('Syear'))
        year2=int(request.POST.get('Eyear'))
        dff=dfa[(dfa['Year']>=year1)&(dfa['Year']<=year2)]
        fig=px.line(dff, x="Year", y="Human Development Index",title='Human Development Index',text='Year')
        fig.update_traces(textposition="top right")
        graph=fig.to_html()
        return render(request,'human2.html',{'graph':graph})
    else:
        return render(request,'human2.html')
    
    
def human3(request):
  if request.method=='POST':  
    df=pd.read_csv('human-development-index.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Human Development Index'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Human Development Index'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Human in both countries',
                      xaxis_title='Year',
                      yaxis_title='Human Development Index')
    graph=fig.to_html
    return render(request,'human3.html',{'graph':graph})
  else:
      return render(request,'human3.html')
   

def human4(request):
   if request.method=='POST':  
    df=pd.read_csv('human-development-index.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Human Development Index'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Human Development Index'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Human Development in both countries',
                      xaxis_title='Year',
                      yaxis_title='human-development-index')
    graph=fig.to_html
    return render(request,'human4.html',{'graph':graph})
   else:
      return render(request,'human4.html')
    

def human5(request):
   if request.method=='POST':  
    df=pd.read_csv('human-development-index.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Human Development Index'],
                             mode='lines+markers', name=c3))
    fig.update_layout(title='Human Development Index in following countries',
                      xaxis_title='Year',
                      yaxis_title='human-development-index')
    graph=fig.to_html()
    return render(request,'human5.html',{'graph':graph})
   else:
    return render(request,'human5.html')
    

def human6(request):
  if request.method=='POST':  
    df=pd.read_csv('human-development-index.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    df3=df3[(df3['Year']>=year1)&(df3['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Human Development Index'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Human Development Index'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Human Development Index'],
                              mode='lines+markers', name=c3))
    fig.update_layout(title='Human Development Index in following countries',
                      xaxis_title='Year',
                      yaxis_title='human-development-index')
    graph=fig.to_html()
    
    return render(request,'human6.html',{'graph':graph})
  else:
    return render(request,'human6.html')
    
    

def human7(request):
    if request.method=='POST':
        df=pd.read_csv('human-development-index.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Human Development Index')
        n=int(request.POST.get('cn'))
        dfmax=df1.tail(n)
        fig=px.bar(dfmax, x='Entity', y='Human Development Index', text_auto='.2s',
                   title="Human Development Index in no of countries")
       
        graph=fig.to_html()
        return render(request,'human7.html',{'graph':graph})
    else:
        return render(request,'human7.html')
   

def human8(request):
    if request.method=='POST':
        df=pd.read_csv('human-development-index.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Human Development Index')
        n=int(request.POST.get('cn'))
        dfmin=df1.head(n)
        fig=px.bar(dfmin, x='Entity', y='Human Development Index', text_auto='.2s',
                   title="Human Development Index in no of countries")
        
        graph=fig.to_html()
        return render(request,'human8.html',{'graph':graph})
    else:
        return render(request,'human8.html')

def human9(request):
    if request.method=='POST':
        df=pd.read_csv('human-development-index.csv')
        cc=coco.CountryConverter()
        df['Entity-codes']=coco.convert(names=df['Code'], to='ISO3')
        print(df['Entity-codes'])
        fig=px.scatter_geo(df, locations="Entity-codes", color="Entity",
                           hover_name="Entity", size="Human Development Index",
                           animation_frame="Year",
                           projection="natural earth")
        year=request.POST.get('country')
        graph=fig.to_html()
        return render(request,'human9.html',{'graph':graph})
    else:
        return render(request,'human9.html')

def human10(request):
    if request.method=='POST':
       df=pd.read_csv('human-development-index.csv')
       country=request.POST.get('country')
       dfc=df[df['Entity']==country]
       year1=int(request.POST.get('Syear'))
       year2=int(request.POST.get('Eyear'))
       dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
       fig=px.scatter(dfc, x="Year", y="Human Development Index",
                      size="Human Development Index", color="Year",
                      hover_name="Entity", log_x=True, size_max=60, title="Human Development Index")
       graph=fig.to_html()
       return render(request,'human10.html',{'graph':graph})
    else:
       return render(request,'human10.html')
    


def life(request):
    return render(request,'life_expectancy_analysis.html')

def life1(request):
    if request.method=='POST':
        df=pd.read_csv('life-expectancy.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        fig=px.line(dfa, x="Year", y="Life expectancy at birth (historical)",
                    title='Life Expectancy')
        graph=fig.to_html()
        return render(request,'life1.html',{'graph':graph})
    else:
        print("else block")
        return render(request,'life1.html')
    

def life2(request):
    if request.method=='POST':
        df=pd.read_csv('life-expectancy.csv')
        print(df.columns)
        Entity=request.POST.get('country')
        dfa=df[df['Entity']==Entity]
        year1=int(request.POST.get('Syear'))
        year2=int(request.POST.get('Eyear'))
        dff=dfa[(dfa['Year']>=year1)&(dfa['Year']<=year2)]
        fig=px.line(dff, x="Year", y="Life expectancy at birth (historical)",title='life_expectancy',text='Year')
        fig.update_traces(textposition="top right")
        graph=fig.to_html()
        return render(request,'life2.html',{'graph':graph})
    else:
        return render(request,'life2.html')
    
    

def life3(request):
 if request.method=='POST':  
    df=pd.read_csv('life-expectancy.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'], mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'], mode='lines+markers', name=c2))
   
    fig.update_layout(title='Life expectancy in both countries',
                      xaxis_title='Year',
                      yaxis_title='life-expectancy')
    graph=fig.to_html
    return render(request,'life3.html',{'graph':graph})
 else:
      return render(request,'life3.html')
    

def life4(request):
   if request.method=='POST':  
    df=pd.read_csv('life-expectancy.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'],y=df1['Life expectancy at birth (historical)'],
                             mode='lines',name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'],y=df2['Life expectancy at birth (historical)'],
                             mode='lines+markers',name=c2))
   
    fig.update_layout(title='Life expectancy in both countries',
                      xaxis_title='Year',
                      yaxis_title='life_expectancy')
    graph=fig.to_html
    return render(request,'life4.html',{'graph':graph})
   else:
      return render(request,'life4.html')
    

def life5(request):
   if request.method=='POST':  
    df=pd.read_csv('life-expectancy.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Life expectancy at birth (historical)'],
                             mode='lines+markers', name=c3))
    fig.update_layout(title='Life expectancy in following countries',
                      xaxis_title='Year',
                      yaxis_title='life-expectancy')
    graph=fig.to_html()
    return render(request,'life5.html',{'graph':graph})
   else:
    return render(request,'life5.html')
    

def life6(request):
   if request.method=='POST':  
    df=pd.read_csv('life-expectancy.csv')
    c1=request.POST.get('Fcountry')
    c2=request.POST.get('Scountry')
    c3=request.POST.get('Tcountry')
    df1=df[df['Entity']==c1]
    df2=df[df['Entity']==c2]
    df3=df[df['Entity']==c3]
    year1=int(request.POST.get('Syear'))
    year2=int(request.POST.get('Eyear'))
    df1=df1[(df1['Year']>=year1)&(df1['Year']<=year2)]
    df2=df2[(df2['Year']>=year1)&(df2['Year']<=year2)]
    df3=df3[(df3['Year']>=year1)&(df3['Year']<=year2)]
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=df1['Year'], y=df1['Life expectancy at birth (historical)'],
                             mode='lines', name=c1))
    fig.add_trace(go.Scatter(x=df2['Year'], y=df2['Life expectancy at birth (historical)'],
                             mode='lines+markers', name=c2))
    fig.add_trace(go.Scatter(x=df3['Year'], y=df3['Life expectancy at birth (historical)'],
                              mode='lines+markers', name=c3))
    fig.update_layout(title='Life Expectancy Index in following countries',
                      xaxis_title='Year',
                      yaxis_title='life-expectancy')
    graph=fig.to_html()
    
    return render(request,'life6.html',{'graph':graph})
   else:
    return render(request,'life6.html')
    
    

def life7(request):
    if request.method=='POST':
        df=pd.read_csv('life-expectancy.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Life expectancy at birth (historical)')
        n=int(request.POST.get('cn'))
        dfmax=df1.tail(n)
        fig=px.bar(dfmax, x='Entity', y='Life expectancy at birth (historical)', text_auto='.2s',
                   title="Life Expectancy in no of countries")
        
        graph=fig.to_html()
        return render(request,'life7.html',{'graph':graph})
    else:
        return render(request,'life7.html')
    

def life8(request):
    if request.method=='POST':
        df=pd.read_csv('life-expectancy.csv')
        year=int(request.POST.get('year'))
        df1=df[df["Year"]==year]
        df1=df1.sort_values(by='Life expectancy at birth (historical)')
        n=int(request.POST.get('cn'))
        dfmin=df1.head(n)
        fig=px.bar(dfmin, x='Entity', y='Life expectancy at birth (historical)', text_auto='.2s',
                   title="Life Expectancy in no of countries")
        
        graph=fig.to_html()
        return render(request,'life8.html',{'graph':graph})
    else:
        return render(request,'life8.html')
    
def life9(request):
    if request.method=='POST':
        df=pd.read_csv('life-expectancy.csv')
        cc=coco.CountryConverter()
        df['Entity-codes']=coco.convert(names=df['Code'], to='ISO3')
        print(df['Entity-codes'])
        fig=px.scatter_geo(df, locations="Entity-codes", color="Entity",
                           hover_name="Entity", size="Life expectancy at birth (historical)",
                           animation_frame="Year",
                           projection="natural earth")
        
        graph=fig.to_html()
        return render(request,'life9.html',{'graph':graph})
    else:
        return render(request,'life9.html')
    

def life10(request):
    if request.method=='POST':
       df=pd.read_csv('life-expectancy.csv')
       country=request.POST.get('country')
       dfc=df[df['Entity']==country]
       year1=int(request.POST.get('Syear'))
       year2=int(request.POST.get('Eyear'))
       dfc=dfc[(dfc['Year']>=year1) & (dfc['Year']<=year2)]
       fig=px.scatter(dfc, x="Year", y="Life expectancy at birth (historical)",
                      size="Life expectancy at birth (historical)", color="Year",
                      hover_name="Entity", log_x=True, size_max=60, title="Life Expectancy")
       graph=fig.to_html()
       return render(request,'life10.html',{'graph':graph})
    else:
       return render(request,'life10.html')
    

def dash(request):
   return render(request,'dashboard.html')
   

    
    






    