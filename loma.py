#!/usr/bin/python3
#   Copyright (C) 2019 Lucas Lee Jing Yi
#   Author: Lucas Lee Jing Yi <lucasljyy@gmail.com>
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
import matplotlib.pyplot as plot
import math
def mapSize(x, y):
    return (math.ceil((math.log10((x+3)**2))/math.log10(2))*((3*(y+2))%5))**5;
def plt(indepIs,lab,x,y):
    indep1=[];
    dep=[];
    for indep in range(10):
        if(indepIs =='y'):
            z=mapSize(x,indep);
        else:
            z=mapSize(indep,y);
        dep.append(z);
        indep1.append(indep);
    plot.plot(indep1,dep, label=lab);
x= int(input("Second last digit of admin no.(X)?:"));
y= int(input("Last digit of admin no.(Y)?:"));
print("Optimal Map Size is: " + str(mapSize(x,y)));
plt('x', 'var x',x,y);
plt('y', 'var y',x,y);
plot.xlabel('Variable');
plot.ylabel('Map Size');
plot.title("LOMA");
plot.legend();
plot.show();
    
    
