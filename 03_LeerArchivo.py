import matplotlib.pyplot as plt
from scipy.signal import *
from numpy import *
from Respuestas import NewMark_a_constante, Diferencia_Central, Rectangular
import numpy as np 

# --------------------------------------------
#        LECTURA DE ARCHIVO
# --------------------------------------------

fnameG = open("Los Gatos.txt", "r")
fnameT = open("Tarzana.txt", "r")
accg    = []
acct    = []
time_g  = []
time_t  = []

for line in fnameG:   
    sl = line.split()
    for i in sl: 
        accg.append(float(i)/(100))
  
for line in fnameT:   
    sl = line.split()
    for i in sl: 
        acct.append(float(i)/(100))

accg = array(accg)
acct = array(acct)


Fs = 50
h  = 1/Fs

time_g = linspace(0, ((len(accg)-1)*h) , len(accg))
time_t = linspace(0, ((len(acct)-1)*h) , len(acct))


# U_total = u_g + u

# m(ddu_g + ddu) + cdu + ku = 0 
# m(ddu) + cdu + ku = -m ddu_g

# --> u(t)




# --------------------------------------------
#              GRAFICAR SISMOS 
# --------------------------------------------
 
  
plt.figure(figsize=(12, 8), dpi= 190, facecolor='w', edgecolor='k')

plt.plot(time_t, array(acct)/9.8, color= "c", linewidth=1.0, linestyle='-', label ="Tarzana")
plt.plot(time_g, array(accg)/9.8, color= "RoyalBlue" , linewidth=1.0, linestyle='-', label ="Gatos")
plt.gca().set(xlim=(0.0, 30.0), ylim=(-2.0, 2.0),
              xlabel='Tiempo [s]', ylabel='Aceleración g')

plt.xticks(fontsize=12); plt.yticks(fontsize=12)
plt.title("Historia de aceleración de Los Gatos y Tarzana ", fontsize=16)
plt.legend(fontsize=14)   
plt.grid()
plt.savefig("Registro Gatos y Tarzana",  dpi = 800  )
plt.show() 



# --------------------------------------------
#           PROPIEDADES SISTEMAS 
# --------------------------------------------

g = 9.806

properties1 = {}
properties1["m"]     = 1500          #Kg
properties1["k"]     = 4200.0*g      #kg /s2
properties1["c"]     = 50.0  *g      #Kg /s
properties1["u0"]    = 0
properties1["du0"]   = 0

Wn1 = (properties1["k"]/properties1["m"] )**0.5
T1  = 2*np.pi/Wn1
ξ1   = properties1["c"]/(2*properties1["m"]*Wn1) 
# Wn1, T1,  ξ1


properties2 = {}
properties2["m"]    = 130.0          #Kg
properties2["k"]    = 4200.0*g       #kg /s2 
properties2["c"]    = 15.0*g         #Kg /s
properties2["u0"]   = 0.0
properties2["du0"]  = 0.0

Wn2 = (properties2["k"]/properties2["m"] )**0.5
T2  = 2*np.pi/Wn2
ξ2   = properties2["c"]/(2*properties2["m"]*Wn2) 
# Wn2, T2,  ξ2


properties3 = {}
properties3["m"]     = 0.2533 
properties3["k"]     = 10.0
properties3["c"]     = 0.1592
properties3["u0"]    = 0
properties3["du0"]   = 0






# pj = [0.0 , 5.0 ,  8.6602 ,  10.0 ,  8.6603  ,  5.0 ,  0.0 ,  0.0 , 0.0 , 0.0 , 0.0  ]
# time_e = linspace(0, ((len(pj)-1)*0.1) , len(pj))



# ug_New ,  vg_New, ag_New =  NewMark_a_constante(properties3, (pj),time_e)
# ug_Cen, vg_Cen, ag_Cen   =  Diferencia_Central(properties3, (pj),time_e)
# ug_Rec ,  vg_Rec, ag_Rec =  Rectangular(properties3, (pj),time_e)

# plt.plot(time_e,  ag_New   , color= "black"     , linewidth=1.2, alpha = 0.8, linestyle='-'  , label = "Gato NewMark u(t) - S1")
# plt.plot(time_e,  ag_Cen, color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Gato Central u(t) - S1")
# plt.plot(time_e,  ag_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Gato Rectangular u(t) - S1")

# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Respuesta de Aceleración Sistema 1 - Los Gatos", fontsize=14)
# plt.legend(fontsize=11) 
# plt.grid()
# plt.show() 



# --------------------------------------------
#              Sistema 1 - GATO
# --------------------------------------------
# #NEWMARK

# plt.figure(figsize=(16, 9), dpi= 190, facecolor='w', edgecolor='k')

# ug_New, vg_New, ag_New         =  NewMark_a_constante(properties1, (-accg*properties1["m"] ),time_g)
# #plt.plot(time_g,  ug_New   , color= "black"     , linewidth=1.2, alpha = 0.8, linestyle='-'  , label = "Gato NewMark u(t) - S1")
# #plt.plot(time_g,  vg_New   , color= "black"     , linewidth=1.2, alpha = 0.8, linestyle='-'  , label = "Gato NewMark v(t) - S1")
# plt.plot(time_g,  ag_New + accg, color= "black"     , linewidth=1.2, alpha = 0.8, linestyle='-'  , label = "Gato NewMark a(t) -S1")


# #CENTRAL
# ug_Cen, vg_Cen, ag_Cen =   Diferencia_Central(properties1, (-accg*properties1["m"] ),time_g)
# #plt.plot(time_g, ug_Cen, color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Gato Central u(t) - S1")
# #plt.plot(time_g, vg_Cen, color= "blue", linewidth=1, linestyle='--',alpha = 1, label = "Gato Central v(t) - S1")
# plt.plot(time_g, ag_Cen + accg, color= "blue", linewidth=1, linestyle='--',alpha = 1, label = "Gato Central a(t) - S1")


# #RECTANGULAR
# ug_Rec ,  vg_Rec, ag_Rec = Rectangular(properties1, (-accg*properties1["m"] ),time_g)
# #plt.plot(time_g,  ug_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Gato Rectangular u(t) - S1")
# #plt.plot(time_g,  vg_Rec  , color= "cyan"    , linewidth=0.75   ,linestyle='--' ,alpha = 1  , label = "Gato Rectangular v(t) - S1")
# #plt.plot(time_g,  ag_Rec + accg, color= "cyan"  , linewidth=0.75   ,linestyle='--' ,alpha = 1  , label = "Gato Rectangular a(t) - S1")



# plt.gca().set(xlim=(0.0, 30.0), ylim=(-24.0, 24.0),
#               xlabel='Tiempo [s]', ylabel='Aceleración [m/s2]')

# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Respuesta de Aceleración Sistema 1 - Los Gatos", fontsize=14)
# plt.legend(fontsize=11) 
# plt.hlines(0, 0, 70, color = "black")
# plt.grid()

# plt.savefig("Z_5 Respuesta de Aceleración Sistema 1 - Los Gatos",  dpi = 800  )
# plt.show() 




# --------------------------------------------
#              Sistema 2 - GATO
# --------------------------------------------
# plt.figure(figsize=(16, 9), dpi= 190, facecolor='w', edgecolor='k')

# #NEWMARK
# ug_New, vg_New, ag_New         =  NewMark_a_constante(properties2, (-accg*properties2["m"] ),time_g)
# #plt.plot(time_g,  ug_New   , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-'   , label = "Gato NewMark u(t) - S2")
# #plt.plot(time_g,  vg_New   , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-'   , label = "Gato NewMark v(t) - S2")
# plt.plot(time_g,  ag_New + accg   , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-'   , label = "Gato NewMark a(t) - S2")

# #CENTRAL
# ug_Cen, vg_Cen, ag_Cen =   Diferencia_Central(properties2, (-accg*properties2["m"] ),time_g)
# #plt.plot(time_g, ug_Cen, color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Gato Central u(t) - S2")
# #plt.plot(time_g, vg_Cen, color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Gato Central v(t) - S2")
# plt.plot(time_g, ag_Cen+ accg, color= "blue", linewidth=1.5, linestyle='--', label = "Gato Central a(t) - S2")


# #RECTANGULAR
# ug_Rec ,  vg_Rec, ag_Rec = Rectangular(properties2, (-accg*properties2["m"] ),time_g)
# #plt.plot(time_g,  ug_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Gato Rectangular u(t) - S2")
# #plt.plot(time_g,  vg_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Gato Rectangular v(t) - S2")
# #plt.plot(time_g,  ag_Rec + accg  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Gato Rectangular a(t) - S2")


# plt.gca().set(xlim=(0.0, 30.0), ylim=(-7.5, 7.5),
#               xlabel='Tiempo [s]', ylabel='Aceleración [m/s2]')

# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Respuesta de Aceleración Sistema 2 - Los Gatos", fontsize=14)
# plt.legend(fontsize=11) 
# plt.hlines(0, 0, 70, color = "black")
# plt.grid()

# plt.savefig("Z_6 Respuesta de Aceleración Sistema 2 - Los Gatos",  dpi = 800  )
# plt.show() 




# Lucas ahora vas con la velocidad del sistema 1 

# --------------------------------------------
#              Sistema 1  TARZANA -B
# --------------------------------------------

# plt.figure(figsize=(16, 9), dpi= 190, facecolor='w', edgecolor='k')

# # NEWMARK
# ut_New, vt_New, at_New   =  NewMark_a_constante(properties1, (-acct*properties1["m"] ),time_t)
# plt.plot(time_t,  ut_New    , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark u(t) - S1")
# #plt.plot(time_t,  vt_New    , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark v(t) - S1")
# #plt.plot(time_t,  at_New+acct    , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark a(t) - S1")


# # CENTRAL
# ut_Cen, vt_Cen, at_Cen =   Diferencia_Central(properties1, (-acct*properties1["m"] ),time_t)
# plt.plot(time_t, ut_Cen,  color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central u(t) - S1")
# #plt.plot(time_t, vt_Cen,  color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central v(t) - S1")
# #plt.plot(time_t, at_Cen+acct,  color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central a(t) - S1")


# # RECTANGULAR
# ut_Rec ,  vt_Rec, at_Rec = Rectangular(properties1, (-acct*properties1["m"] ),time_t)
# plt.plot(time_t,  ut_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular u(t) - S1")
# #plt.plot(time_t,  vt_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular v(t) - S1")
# #plt.plot(time_t[:-1],  at_Rec[1:]+acct[:-1] , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular a(t) - S1")



# # plt.gca().set(xlim=(0.0, 60.0), ylim=(-8.0, 8.0),
# #               xlabel='Tiempo [s]', ylabel='Acelerción [m/s2]')
# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Respuesta de Aceleración Sistema 1 - Tarzana", fontsize=14)
# plt.legend(fontsize=11) 
# plt.grid()
# plt.hlines(0, 0, 70, color = "black")

# #plt.savefig("Z_11 Respuesta de Aceleración Sistema 1 - Tarzana",  dpi = 800  )
# plt.show() 




# # --------------------------------------------
# #               Sistema 2  TARZANA
# # --------------------------------------------

# plt.figure(figsize=(16, 9), dpi= 190, facecolor='w', edgecolor='k')

# # # NEWMARK
# ut_New, vt_New, at_New   =  NewMark_a_constante(properties2, (-acct*properties2["m"] ),time_t)
# #plt.plot(time_t,  ut_New     , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark u(t) - S2")
# #plt.plot(time_t,  vt_New   , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark v(t) - S2")
# plt.plot(time_t,  at_New +acct   , color= "black"   , linewidth=1.2, alpha = 0.8, linestyle='-' , label = "Tarzana NewMark a(t) - S2")


# # CENTRAL
# ut_Cen, vt_Cen, at_Cen =   Diferencia_Central(properties2, (-acct*properties2["m"] ),time_t)
# #plt.plot(time_t, ut_Cen,   color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central u(t) - S2")
# #plt.plot(time_t, vt_Cen,  color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central v(t) - S2")
# plt.plot(time_t, at_Cen + acct, color= "blue", linewidth=1, linestyle='--',alpha = 1 , label = "Tarzana Central a(t) - S2")


# # RECTANGULAR
# ut_Rec ,  vt_Rec, at_Rec = Rectangular(properties2, (-acct*properties2["m"] ),time_t)
# #plt.plot(time_t,  ut_Rec , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular u(t) - S2")
# #plt.plot(time_t,  vt_Rec  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular v(t) - S2")
# #plt.plot(time_t[:-1],  at_Rec[1:]+ acct[:-1]  , color= "cyan"   , linewidth=0.75   ,linestyle= "--" ,alpha = 1  , label = "Tarzana Rectangular a(t) - S2")


# plt.gca().set(xlim=(0.0, 60.0), ylim=(-55.0, 55.0),
#               xlabel='Tiempo [s]', ylabel='Aceleración [m/s2]')
# plt.xticks(fontsize=12); plt.yticks(fontsize=12)
# plt.title("Respuesta de Aceleración Sistema 2 - Tarzana", fontsize=14)
# plt.legend(fontsize=11) 
# plt.hlines(0, 0, 70, color = "black")
# plt.grid()

# plt.savefig("Z_12 Respuesta de Aceleración Sistema 2 - Tarzana",  dpi = 800  )
# plt.show() 








# #Sistema 1 - ξ = 0.005
# TS  = linspace(0.045, 3 , 500)
# ξ = 3.0/100


# Sd_t  = zeros((len(TS), 1))
# Sv_t  = zeros((len(TS), 1))
# Sa_t  = zeros((len(TS), 1))
# Spv_t = zeros((len(TS), 1))
# Spa_t = zeros((len(TS), 1))

# Sd_g  = zeros((len(TS), 1))
# Sv_g  = zeros((len(TS), 1))
# Sa_g  = zeros((len(TS), 1))
# Spv_g = zeros((len(TS), 1))
# Spa_g = zeros((len(TS), 1))


# for i in range(len(TS)):
    
#     T = TS[i]
    
#     wn = 2*(3.141592)/T    
#     m  = 1  
#     cr = 2*m*wn
#     c  = ξ*cr
#     k  = m*wn**2
       
#     properties_T = {}
#     properties_T["m"]     = m           #Kg
#     properties_T["k"]     = k          #kg /s2
#     properties_T["c"]     = c          #Kg /s
#     properties_T["u0"]    = 0
#     properties_T["du0"]   = 0
    
#     ug_New, vg_New, ag_New   =  NewMark_a_constante(properties_T, (-accg*properties_T["m"] ),time_g)
#     ut_New, vt_New, at_New   =  NewMark_a_constante(properties_T, (-acct*properties_T["m"] ),time_t)
    
    
#     u_max_g = max(absolute(ug_New))
#     v_max_g = max(absolute(vg_New))
#     a_max_g = max(absolute(ag_New+accg))
    
#     u_max_t = max(absolute(ut_New))
#     v_max_t = max(absolute(vt_New))
#     a_max_t = max(absolute(at_New+acct))
    
    
#     Sd_g[i]  = u_max_g
#     Sv_g[i]  = v_max_g
#     Sa_g[i]  = a_max_g
#     Spv_g[i] = u_max_g*wn
#     Spa_g[i] = u_max_g*wn**2
    
#     Sd_t[i]  = u_max_t
#     Sv_t[i]  = v_max_t
#     Sa_t[i]  = a_max_t
#     Spv_t[i] = (u_max_t)*(wn)
#     Spa_t[i] = (u_max_t)*(wn**2)



# plt.figure(figsize=(12, 8), dpi= 200, facecolor='w', edgecolor='k')

# #plt.plot(TS,  Sd_g  , color= "RoyalBlue"         , linewidth=1.5   ,linestyle='--'    , label = "Sd ξ = 0.05 - Gatos")
# #plt.plot(TS,  Sd_g  , color= "red"         , linewidth=1.5   ,linestyle='-'    , label = "Sd ξ =0.032 - Gatos")
# plt.plot(TS,  Sa_g/9.8  , color= "RoyalBlue"        , linewidth=3 , alpha = 0.5  ,linestyle='-'     , label = "  Sa ξ = 0.03 - Gatos")
# #plt.plot(TS,  Spv_g , color= "RoyalBlue"          , linewidth=1.5    ,linestyle='-'   , label = "Spv ξ = 0.03 - Gatos")
# plt.plot(TS,  Spa_g/9.8 , color= "blue"      , linewidth=1.5    ,linestyle='--'   , label = "Spa ξ = 0.03 - Gatos")




# #plt.plot(TS,  Sd_t  , color= "c"              , linewidth=1.5   ,linestyle='--'   , label = "Sd ξ = 0.05 - Tarzana")
# #plt.plot(TS,  Sv_t  , color= "c"             , linewidth=1.5   ,linestyle='-'   , label = "  Sv ξ = 0.3 -  Tarzana")
# plt.plot(TS,  Sa_t/9.8  , color= "c"      , linewidth=3   , alpha = 0.5 , linestyle='-'   , label = "  Sa ξ = 0.03 - Tarzana")
# #plt.plot(TS,  Spv_t , color= "c"          , linewidth=1.5    ,linestyle='-'   , label = "Spv ξ = 0.03 -  Tarzana")
# plt.plot(TS,  Spa_t/9.8 , color= "teal"     , linewidth=1.5    ,linestyle='--'   , label = "Spa ξ = 0.03 - Tarzana")



# plt.gca().set(xlim=(0.0, 3.), ylim=(0.0, 7.0),
#               xlabel='Periodo T [s]', ylabel='Spa, Sa (ξ,T) g')

# plt.xticks(fontsize=8); plt.yticks(fontsize=8)
# plt.title("Espectro de Aceleración", fontsize=14)
# plt.legend(fontsize=11)   
# plt.hlines(0, 0, 0, color = "black")
# # plt.vlines(0.353 , 0, 70 , color= "black"              , linewidth=1.0 )
# # plt.vlines(1.199 , 0, 70 , color= "black"              , linewidth=1.0 )
# plt.grid(True)
# plt.savefig("ERROR HOY",  dpi = 800  )
# plt.show() 














