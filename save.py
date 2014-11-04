# I just collect the data. I even didn't filter all the data now. Maybe some part you cannot understand. It doesn't matter.
import ConfigParser
from TwitterAPI import TwitterAPI,TwitterRestPager
import sys
import time
import ast,re
from collections import Counter

def get_twitter(config_file):
    config = ConfigParser.ConfigParser()
    config.read(config_file)
    twitter = TwitterAPI(
                   config.get('twitter', 'consumer_key'),
                   config.get('twitter', 'consumer_secret'),
                   config.get('twitter', 'access_token'),
                   config.get('twitter', 'access_token_secret'))
    return twitter
# twitter = get_twitter('twitter1.cfg')
# print 'Established Twitter connection.'

def get_data(string,filename):
	pager = TwitterRestPager(twitter,'search/tweets',{'q':'#TheWalkingDead','count':200})
	i=0
	f=open(filename,'w')
	for item in pager.get_iterator(new_tweets=True):
		f.write(str(item)+'\n')
		i=i+1
		print i
	f.close



# get_data('#TheWalkingDead','TheWalkingDead2.txt')
# print 'ok'
def get_date(filename):
	count=0
	f=open(filename,'r')
	print filename
	for i in f:
		i=ast.literal_eval(i)
		if i.has_key('created_at'):
			if count==0:
				print i['created_at']
			# print i['created_at']
			# print count
			count=count+1

	print i['created_at']
	print count-1
# get_date('TheWalkingDead20.txt')#111899 tweets
# get_date('TheWalkingDead21-25.txt')#88085 tweets
# get_date('TheWalkingDead26.txt')#21297tweets
# get_date('TheWalkingDead27-03.txt')#626699 tweets
# total have 847,980 tweets
# get_date('total.txt')



def get_text(filename,counttext):
	f=open(filename,'r')
	f1=open('text.txt','a+')
	a=set()
	for i in f:
		i=ast.literal_eval(i)
		if i.has_key('text') and i.has_key('lang') and i['lang']=='en':
			i['text']=i['text'].encode('utf-8')
			f1.write(i['text']+'\n')
			a.add(i['text'])
			print counttext
			counttext=counttext+1
		else:
			i.clear()
			print 'clear one tweets'
	f.close()
	f1.close()
	print "set have:",len(a)
	print "counttext:",counttext
	return counttext
# a=get_text('TheWalkingDead.txt',0)
# b=get_text('TheWalkingDead26.txt',a-1)
# get_text('TheWalkingDead20.txt',b-1)

def get_lang(filename):
	f=open(filename,'r')
	countlang=set()
	f1=open('lang.txt','w')
	c=0
	lang={}
	for i in f:
		i=ast.literal_eval(i)
		if i['lang']:
			countlang.add(i['lang'])
			f1.write(i['lang'].encode('utf-8')+':::'+i['text'].encode('utf-8')+'\n'+'\n')
	print len(countlang)
	for i in countlang:
		lang[i]=0
	f.close()
	print 'finish'
	return lang
# lang=get_lang('TheWalkingDead20.txt')

def count_lang(filename):
	f=open(filename,'r')
	c=0
	lang=get_lang(filename)
	for i in f:
		i=ast.literal_eval(i)
		if i.has_key('lang'):
			print i['lang']
			lang1[i['lang']]+=1
	f.close()
	print 'finish'
	return lang1
# print lang
# lang1=count_lang('total.txt',lang)
# print lang1

def text_split(filename):
	f=open(filename,'r')
	token=[]
	for line in f:
		token.append(line.lower().split())
	return token
# token=text_split('text.txt')
# print len(token)
# print token[6]
def add(filename):
	f=open(filename,'r')
	f1=open('total.txt','a+')
	for line in f:
		f1.write(line)
	f.close()
	f1.close()
# add('TheWalkingDead.txt')
# add('TheWalkingDead26.txt')
# add('TheWalkingDead20.txt')
def get_userinfo(filename):
	f=open(filename,'r')
	f1=open('userinfo.txt','a+')
	for i in f:
		i=ast.literal_eval(i)
		if i['lang'] and i['lang']=='en':
			a=str(i['user']['name'].encode('utf-8'))+":"+str(i['user']['screen_name'].encode('utf-8'))+":"+str(i['user']['description'].encode('utf-8'))
			print a
			f1.write(a+'\n')
	f.close()
	f1.close()
# get_userinfo("total.txt")






