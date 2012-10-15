'''
Simple HTML parser.

2008
Yu Tomita
yu.t@gatech.edu


Two main functions

- getDataByTag(str,tags,nth=1,includeTag=False)
  Get string surrounded by specified tags.

- removeTags(str)
  Remove html tags (e.g. <div...>) from string
'''


# find if each words in all[] are in str.
# returns False if any of the words is missing.
def strAllin(str,all):
	for a in all:
		if a not in str:
			return False
	return True

# returns i,j 
# where i=index of starting tag, j=index of content
# <div id="blah">content...</div>
# i              j
def getTagIndex(str,tags,nth=1):
	numC = len(str)
	numSpecifier = len(tags.split())
	tag = tags.split()[0]
	numT = len(tag)
	c=1
	i=0
	while i<numC:
		if str[i:i+numT+1]=='<%s'%tag:
			j=i
			while str[j]!='>':
				j=j+1
			j=j+1
			wholetag = str[i:j]
			if len(tags.split())==1:
				if c<nth:
					c+=1
					i=j
				else:	return i,j
			for spec in tags.split()[1:]:
				if strAllin(wholetag,tags.split()[1:]):
					if c<nth:
						c+=1
						i=j
						break
					return i,j		
		i=i+1
	return None,None


# tags should be like 'div id content' (tag first, inclusive)
# returns content data surrounded by that tag, 
# found 1st time, without specified tags by default.
def getDataByTag(str,tags,nth=1,includeTag=False):
	i,j = getTagIndex(str,tags,nth)
	if i==None:
		return None
	startTag = '<%s'%tags.split()[0]
	endTag = '</%s>'%tags.split()[0]
	numC = len(str)
	c = j
	inners = 0
	j2 = 0
	if '/' in tags: #closing tag
		i,i2 = i,j
		j,j2 = 0,0
		c=numC
	while c<numC:
		if str[c:c+len(startTag)]==startTag:
			inners+=1
			c=c+len(startTag)
		if str[c:c+len(endTag)]==endTag:
			if inners==0:
				j2=c
				i2=c+len(endTag)
				break
			inners-=1
			c=c+len(endTag)
		c+=1
	if includeTag:
		return str[i:i2]
	return str[j:j2]	

# removes HTML tags (<...>) from str
def removeTags(str):
	ans = ''
	i=0 
	while i<len(str):
		if str[i]=='<':
			while str[i]!='>':
				i=i+1
		elif str[i]=='>':
			i+=1
			#ans+=' '
		else:
			ans+=str[i]
			i+=1
	return ans 
