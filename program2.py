import time
r = 255
g = 0
b = 0


while(1):
	# ball string
	string = "*                                                  "
	# move it to right end
	for y in range(len(string)-1):
		print(f"\033[38;2;{r};{g};{b}m",end="")
		newStr = ""
		# shif right
		for i in range(len(string)): 
			newStr += string[i-1]
		# escape code to keep on same line
		print(newStr,r,g,b," ",end='\n \033[F \033[0m')
		# keeps places of the ball
		string = newStr
		if ((r>=255 and b<=0) and g<255):
			g+=1
		if ((b>=255 and r<=0) and g>0):
			g-=1
		# blue
		if (g>=255 and r<=0 and b<255):
			b+=1
		if (r>=255 and g<=0 and b>0):
			b-=1
		# red
		if (g>=255 and b<=0 and r>0):
			r-=1
		if (b>=255 and g<=0 and r<255):
			r+=1
		# lerp fuction 
		time.sleep(0.05+0.09*(abs(len(string)/2-y))/len(string))

	# move it to left end
	for y in range(len(string)-1):
		print(f"\033[38;2;{r};{g};{b}m",end="")
		newStr = ""
		# shif left
		for i in range(len(string)):
			newStr += string[i-len(string)+1]
		print(newStr,r,g,b," ",end='\n \033[F \033[0m')
		string = newStr
		if ((r>=255 and b<=0) and g<255):
			g+=1
		if ((b>=255 and r<=0) and g>0):
			g-=1
		# blue
		if (g>=255 and r<=0 and b<255):
			b+=1
		if (r>=255 and g<=0 and b>0):
			b-=1
		# red
		if (g>=255 and b<=0 and r>0):
			r-=1
		if (b>=255 and g<=0 and r<255):
			r+=1
		# lerp fuction 
		time.sleep(0.05+0.09*(abs(len(string)/2-y))/len(string))

# reset all modes (styles and colors)
# Do not remove!!!!
print("\033[0m", end="")
