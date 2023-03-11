import neopixel
import random
from machine import Pin
import time
b1=Pin(1,Pin.IN,Pin.PULL_UP)
b2=Pin(2,Pin.IN,Pin.PULL_UP)
b3=Pin(3,Pin.IN,Pin.PULL_UP)
b4=Pin(4,Pin.IN,Pin.PULL_UP)

n = 300
p = 5
arr=[[  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
         13,  14],
       [ 34,  33,  32,  31,  30,  29,  28,  27,  26,  25,  24,  23,  22,
         21,  20],
       [ 40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,  52,
         53,  54],
       [ 74,  73,  72,  71,  70,  69,  68,  67,  66,  65,  64,  63,  62,
         61,  60],
       [ 80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,  91,  92,
         93,  94],
       [114, 113, 112, 111, 110, 109, 108, 107, 106, 105, 104, 103, 102,
        101, 100],
       [120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
        133, 134],
       [154, 153, 152, 151, 150, 149, 148, 147, 146, 145, 144, 143, 142,
        141, 140],
       [160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
        173, 174],
       [194, 193, 192, 191, 190, 189, 188, 187, 186, 185, 184, 183, 182,
        181, 180],
       [200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
        213, 214],
       [234, 233, 232, 231, 230, 229, 228, 227, 226, 225, 224, 223, 222,
        221, 220],
       [240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252,
        253, 254],
       [274, 273, 272, 271, 270, 269, 268, 267, 266, 265, 264, 263, 262,
        261, 260],
       [280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292,
        293, 294]]

np = neopixel.NeoPixel(Pin(p), n)

def clear():
    for i in range(n):
        np[i]=(0,0,0)
    np.write()
    time.sleep(0.001)
def led(r,c,s=1):
    if s==0:
        np[arr[r][c]]=(0,0,0)
        np.write()
    else:
        np[arr[r][c]]=(225,0,0)
        np.write()
def ledg(r,c,s=1):
    if s==0:
        np[arr[r][c]]=(0,0,0)
        np.write()
    else:
        np[arr[r][c]]=(0,255,0)
        np.write()

positions=[arr[11][3],arr[11][7],arr[11][11],arr[7][3],arr[7][7],arr[7][11],arr[3][3],arr[3][7],arr[3][11]]

def xs(r,c):
    lit=[[r,c],[r-1,c-1],[r+1,c+1],[r+1,c-1],[r-1,c+1]]
    for i in range(len(lit)):
        led(lit[i][0],lit[i][1])
def os(r,c):
    lit=[[r+1,c],[r-1,c],[r,c+1],[r,c-1],[r-1,c-1],[r+1,c+1],[r+1,c-1],[r-1,c+1]]
    for i in range(len(lit)):
        led(lit[i][0],lit[i][1])

for i in range (1,14):
    np[arr[1][i]]=(0,0,225)
    np[arr[i][1]]=(0,0,225)
    np[arr[13][i]]=(0,0,225)
    np[arr[i][13]]=(0,0,225)
    np[arr[5][i]]=(0,0,225)
    np[arr[9][i]]=(0,0,225)
    np[arr[i][5]]=(0,0,225)
    np[arr[i][9]]=(0,0,225)
np.write()

inp=0
r=c=7
ledg(r,c)
flag=0

win=[[0,0,0],[0,0,0],[0,0,0]]
dntstp=[]

while (inp!=9):
  # clear_output(wait=True)
  inp=int(input("Now: "))
  if(arr[r][c] not in dntstp):
    ledg(r,c,0)
  else:
    led(r,c)
  if (inp==4):
    c=c-4
  elif (inp==6):
    c=c+4
  elif (inp==8):
    r=r+4
  elif (inp==2):
    r=r-4
  elif (inp==5):
    if flag==0:
      flag=1
      xs(r,c)
      dntstp.append(arr[r][c])
      test=positions.index(arr[r][c])
      win[int((test)/3)][(test)%3]=1
    else:
      flag=0
      os(r,c)
      test=positions.index(arr[r][c])
      win[int((test)/3)][(test)%3]=5
  sumr=0
  sumc=0
  sumd1=0
  sumd2=0
  for i in range(3):
    for j in range(3):
      sumr=sumr+win[i][j]
      sumc=sumc+win[j][i]
    sumd1=sumd1+win[i][i]
    sumd2=sumd2+win[i][2-i]
  wincheck=[sumr,sumc,sumd1,sumd2]
  if (3 in wincheck):
    clear()
    for i in range (2,13):
      np[arr[i][i]]=(255,0,0)
      np[arr[i][14-i]]=(255,0,0)
    np.write()
    break
  elif (15 in wincheck):
    clear()
    for i in range(2,13):
      np[arr[i][2]]=(255,0,0)
      np[arr[2][i]]=(255,0,0)
      np[arr[i][12]]=(255,0,0)
      np[arr[12][i]]=(255,0,0)
    np.write()
    break
  ledg(r,c)