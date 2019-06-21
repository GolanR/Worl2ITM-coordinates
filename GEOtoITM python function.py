# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 09:06:33 2019

@author: Roni Golan

This code includes a function that analiticaly converts world coordinates (lng, lat)  to ITM coordinates (x, y) and another function that iteratively converts world coordinates to ITM 
Notes: the accuracy is far from perfect, with about 20 meters error in Haifa, for example. Good enough for my purposes.
       accuracy increases as you get closer to x0,y0 
 
"""

def GEOtoITM (lng, lat):
    import math   
     #אליפסואיד GRS80
    a_grs80=6378137
    e2_grs80=0.006694380021

    
    #הערכים הגיאוגרפיים של הנקודה הראשית
    #phi0=31 44' 03''.817
    phi0_malot=31
    phi0_dakot=44
    phi0_shniot=3.817
    
    phi0=phi0_malot+phi0_dakot/60+phi0_shniot/3600
    
    #lambda=35 12' 16''.261*/
    lambda0_malot=35
    lambda0_dakot=12
    lambda0_shniot=16.261
    
    lambda0=lambda0_malot+lambda0_dakot/60+lambda0_shniot/3600
    	
    #הערכים יישרי הזוית של הנקודה הראשית
    x0=219529.584 #/*E0*/
    y0=626907.390 #/*N0*/

    # מקדם קנה המידה על המרידיאן המרכזי
    m0=1.0000067

#לפי משוואות המיפוי מרקטור רוחבי לחישוב קורדינטות מישוריות מקורדינטות גיאוגרפיות
    """
    y=y0+m0NJ(1+D2+D3)
    x=x0+(Sm-Sm0)+m0N(J^2)t(1+C2+C3)/2 
    
        כאשר
    
    N=a_grs80/sqrt(1-e^2_grs80*sin^2phi)
    J=(lambda-lambda0)cos(phi)
    D2=J^2 
    """
    CA=1.005052500
    CB=0.002531553
    CC=0.000002657
    CD=0.000000003
    Sm0=3512424.3388
    
    Sm=m0*a_grs80*(1-e2_grs80)*(CA*lat*math.pi/180-CB*math.sin(2*lat*math.pi/180)+CC*math.sin(4*lat*math.pi/180)-CD*math.sin(6*lat*math.pi/180))
    t=math.tan(lat*math.pi/180)
    niu2=e2_grs80*(math.cos(lat*math.pi/180)**2)/(1-e2_grs80)
    N=a_grs80/((1-e2_grs80*(math.sin(lat*math.pi/180)**2))**(0.5))
    J=(lng-lambda0)*math.pi/180*math.cos(lat*math.pi/180)
    D2=(J**2)*(1-(t**2)+niu2)/6
    D3=(J**4)*(5-18*(t**2)+14*niu2+(t**4)-58*(t**2)*niu2)/120
    C2=(J**2)*(5-(t**2)+9*niu2+4*(niu2**2))/12
    C3=(J**4)*(61-58*(t**2)+270*niu2+(t**4)-330*(t**2)*niu2)/360
    
    x=x0+m0*N*J*(1+D2+D3)
    y=y0+(Sm-Sm0)+m0*N*(J**2)*t*(1+C2+C3)/2
    ret=[x,y]
    return (ret)
"""
הרעיןו כאן הוא למצוא איטרטיבית את הנקודות העולמיות  
"""
def ITMtoGEO(x,y,thresh=10):
    """
    #iteratively, to avoid complex calculations 
    lat_a=33.3 #סוריה
    lng_a=36.0

    lat_b=33.3 # ים תיכון צפון
    lng_b=34.0

    lat_c=29.5 #סיני
    lng_c=34.0

    lat_d=29.5 #ים סוף
    lng_d=35.0
    """
    lat_i=32.0
    lng_i=35.0
    
    dist=3*thresh    
    while dist>thresh:
        a=GEOtoITM(lat=lat_i, lng=lng_i)
        
        dist_x=a[0]-x
        dist_y=a[1]-y
        dist=((dist_x**2)+(dist_y**2))**(0.5)
        lng_i=lng_i-(dist_x/1000000)
        lat_i=lat_i-(dist_y/1000000)
        print("DX: ", dist_x)
    ret=[lng_i,lat_i]
    return (ret)        
      
