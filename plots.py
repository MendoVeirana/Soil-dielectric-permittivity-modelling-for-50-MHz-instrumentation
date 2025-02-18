""" This module defines some plot style"""

import numpy as np 
import matplotlib.pyplot as plt


def fig2(a, b, c):
    a.grid(True)
    a.legend(loc='upper left', fontsize = 18)
    a.tick_params(axis='y', labelsize=15) 
    a.tick_params(axis='x', labelsize=15) 
    a.set_ylabel('$m$: cementation', fontsize = 18) 
    #a.set_yticks(np.arange(0, -120, -3))
    a.grid(True) 
    a.set_ylim(0, 7)  
    #a.set_xlim(0, 70)
    a.set_xticks(np.arange(0, 100, 10))
    #a.set_yticks(np.arange(3.2, 4.75, 0.4))

    b.grid(True)
    b.legend(loc='upper right', fontsize = 18)
    b.tick_params(axis='y', labelsize=15) 
    b.tick_params(axis='x', labelsize=15) 
    b.set_ylabel('$α$: alpha exponent ', fontsize = 18) 
    #b.set_yticks(np.arange(0, -120, -3))
    b.grid(True) 
    b.set_ylim(0.3, 0.8)  
    #b.set_xlim(0, 70)
    b.set_xticks(np.arange(0, 100, 10))
    #b.set_yticks(np.arange(3.2, 4.75, 0.4))

    c.grid(True)
    c.legend(loc='upper left', fontsize = 18)
    c.tick_params(axis='y', labelsize=15) 
    c.tick_params(axis='x', labelsize=15) 
    c.set_ylabel('$L$: depolarisation factor', fontsize = 18) 
    c.set_xlabel('Clay content [%]', fontsize = 18) 
    #c.set_yticks(np.arange(0, -120, -3))
    c.grid(True) 
    c.set_ylim(0, 1)  
    #c.set_xlim(0, 70)
    c.set_xticks(np.arange(0, 100, 10))
    #c.set_yticks(np.arange(3.2, 4.75, 0.4))


def fig6(ax4):
    ax4.grid(True)
    #ax4.legend(loc='upper left', fontsize = 12)
    #ax4.set_title(" " , fontweight='bold', fontsize=25) 
    ax4.tick_params(axis='y', labelsize=20) 
    ax4.tick_params(axis='x', labelsize=20) 
    ax4.set_ylabel('$ε_{s}$ [-] (soil dried at 105 C)', fontsize = 22) 
    ax4.set_xlabel('$ε_{s}$ [-] (soil dried at 150 C)', fontsize = 22) 
    #ax1.set_yticks(np.arange(0, -120, -3))
    ax4.grid(True) 
    #ax4.set_ylim(3.2, 4.5)  
    #ax4.set_xlim(3.2, 4.5)
    ax4.set_xticks(np.arange(3.2, 4.75, 0.4))
    ax4.set_yticks(np.arange(3.2, 4.75, 0.4))

    
def fig7(ax1, ax2, ax3):  
    ax1.grid(True)
    # ax1.set_title(" " , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=20) 
    ax1.tick_params(axis='x', labelsize=20) 
    ax1.set_ylabel('$ε_{s}$ [-]', fontsize = 22) 
    # ax1.set_ylim(0, 6) 
    ax1.set_xlabel('Clay content [%]', fontsize = 22) 

    ax2.grid(True)
    # ax2.legend(loc='lower right', fontsize = 12) 
    # ax2.set_title(" " , fontweight='bold', fontsize=20) 
    ax2.tick_params(axis='y', labelsize=20) 
    ax2.tick_params(axis='x', labelsize=20) 
    ax2.set_xlabel('$ε_{s}$ [-] ', fontsize = 22) 
    ax2.set_ylabel('$ϴ_{bw}$ [%]', fontsize = 22) 
    # ax2.set_ylim(0, 1.8) 
    # ax2.set_xlim(0, 40) 
    ax2.set_yticks(np.arange(0, 1.8, 0.4))
    
    ax3.legend(loc='lower right', fontsize = 14) 
    # ax3.legend(loc='lower right', fontsize = 12) 
    # ax3.set_title(" " , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=20) 
    ax3.tick_params(axis='x', labelsize=20) 
    ax3.set_xlabel('Clay content [%]', fontsize = 22) 
    ax3.set_ylabel('$ϴ_{bw}$ [%]', fontsize = 22) 
    ax3.grid(True) 
    # ax3.set_ylim(3.3, 4) 
    # ax3.set_xlim(3.25, 4.2)
    ax3.set_yticks(np.arange(0, 1.8, 0.4))
 

def fig8(p1, p2):  
    p1.grid(True)
    p1.legend(loc='upper right', fontsize = 15) 
    p1.tick_params(axis='y', labelsize=20) 
    p1.tick_params(axis='x', labelsize=20) 
    p1.set_ylabel('${ε_b}$ [-] ', fontsize = 22) 
    p1.set_ylim(0, 35) 
    p1.set_xlabel('Clay content [%]', fontsize = 22) 

    p2.grid(True)
    p2.legend(loc='upper left', fontsize = 15) 
    p2.tick_params(axis='y', labelsize=20) 
    p2.tick_params(axis='x', labelsize=20) 
    p2.set_xlabel('${ϴ}$ [%]', fontsize = 22) 
    #p2.set_ylabel('${ϴ_bw}$ [%]', fontsize = 22) 
    p2.set_ylim(0, 35) 
    p2.set_xlim(0, 50) 
    #p2.set_yticks(np.arange(0, 1.8, 0.4))
    #p2.set_xticks(np.arange(3.2, 4.75, 0.4))


def fig9(ax9):
    ax9.set_xlabel("${ϴ}$ [%]",   fontsize=20)
    ax9.set_ylabel("${ε_b}$ [-]",  fontsize=20)
    ax9.tick_params(axis='y', labelsize=16) 
    ax9.tick_params(axis='x', labelsize=16) 

    ax9.legend(loc='best', fontsize=10)
    ax9.grid()
    
    
def fig10(ax1, ax2, ax3, ax4): 
    #ax1.set_title("" , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=20) 
    ax1.tick_params(axis='x', labelsize=18) 
    ax1.set_xlabel('', fontsize = 16) 
    ax1.set_ylabel('${α}$', fontsize = 22) 
    ax1.grid(True) 
    ax1.set_ylim(0, 1.6)  
    ax1.set_xlim(0, 40) 
    ax1.legend(loc='upper left', fontsize = 20) 
 
    #ax2.set_title("" , fontweight='bold', fontsize=25) 
    ax2.tick_params(axis='y', labelsize=18) 
    ax2.tick_params(axis='x', labelsize=18) 
    ax2.set_xlabel('', fontsize = 16) 
    #ax2.set_ylabel('', fontsize = 16) 
    ax2.grid(True) 
    ax2.set_ylim(0, 1.6)  
    ax2.set_xlim(0, 35) 
    ax2.legend(loc='upper left', fontsize = 20)

    #ax3.set_title("" , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=20) 
    ax3.tick_params(axis='x', labelsize=20) 
    ax3.set_xlabel('Clay content [%]', fontsize = 22) 
    ax3.set_ylabel('${m}$', fontsize = 22) 
    ax3.grid(True) 
    ax3.set_ylim(0.5, 2.2)  
    ax3.set_xlim(0, 40)
    ax3.legend(loc='upper right', fontsize = 20) 
    
    #ax4.set_title(" " , fontweight='bold', fontsize=25) 
    ax4.tick_params(axis='y', labelsize=18) 
    ax4.tick_params(axis='x', labelsize=20) 
    ax4.set_xlabel('CEC [meq/100g]', fontsize = 22) 
    #ax4.set_ylabel('', fontsize = 16) 
    ax4.grid(True) 
    ax4.set_ylim(0.5, 2.2)  
    ax4.set_xlim(0, 35)
    ax4.legend(loc='upper right', fontsize = 20)
 

def fig11(ax1, ax2, ax3, ax4): 

    ax1.set_title("" , fontweight='bold', fontsize=25) 
    ax1.tick_params(axis='y', labelsize=20) 
    ax1.tick_params(axis='x', labelsize=18) 
    ax1.set_xlabel('', fontsize = 20) 
    ax1.set_ylabel('${L_w}$ from Eq. 9', fontsize = 22) 
    ax1.grid(True) 
    ax1.set_xlim(0, 35) 
    ax1.legend(loc='upper right', fontsize = 20)
    ax1.set_ylim(-0.3, 0.8)  
    
    ax2.tick_params(axis='y', labelsize=18) 
    ax2.tick_params(axis='x', labelsize=18) 
    ax2.set_xlabel('', fontsize = 22) 
    ax2.set_ylabel('${L}$ from Eq. 11', fontsize = 22) 
    ax2.grid(True) 
    ax2.set_xlim(0, 35) 
    ax2.legend(loc='upper right', fontsize = 20)
    ax2.set_ylim(-0.3, 0.8)  

    ax3.set_title("" , fontweight='bold', fontsize=25) 
    ax3.tick_params(axis='y', labelsize=18) 
    ax3.tick_params(axis='x', labelsize=18) 
    ax3.set_xlabel('CEC [meq/100g]', fontsize = 22) 
    ax3.set_ylabel('${L}$ from Eq. A8', fontsize = 22) 
    ax3.grid(True)   
    ax3.set_xlim(0, 35) 
    ax3.legend(loc='upper right', fontsize = 20)
    ax3.set_ylim(-0.3, 0.8)  
    
    ax4.tick_params(axis='y', labelsize=18) 
    ax4.tick_params(axis='x', labelsize=20) 
    ax4.set_xlabel('CEC [meq/100g]', fontsize = 22) 
    ax4.set_ylabel('${L}$ from Eq. A10', fontsize = 22) 
    ax4.grid(True)   
    ax4.set_xlim(0, 35) 
    ax4.legend(loc='upper right', fontsize = 20)
    ax4.set_ylim(-0.3, 0.8) 

    
def fig13(fx1, fx2, fx3, fx4, fx5, fx6):
    lb=20
    
    fx1.tick_params(axis='y', labelsize=lb) 
    fx1.tick_params(axis='x', labelsize=lb) 
    #fx1.set_ylabel('ε predicted', fontsize = 20) 
    #fx1.set_xlabel('ε observed (field)', fontsize = 20) 
    fx1.grid(True) 
    fx1.set_ylim(0, 51)  
    fx1.set_xlim(0, 51)  
    #fx1.legend(loc='upper left', fontsize = 12) 

    fx2.tick_params(axis='y', labelsize=lb) 
    fx2.tick_params(axis='x', labelsize=lb) 
    #fx2.set_ylabel('ε predicted', fontsize = 20) 
    #fx2.set_xlabel('ε observed (field)', fontsize = 20) 
    fx2.grid(True) 
    fx2.set_ylim(0, 51)  
    fx2.set_xlim(0, 51)  
    #fx2.legend(loc='upper left', fontsize = 12) 
    
    fx3.tick_params(axis='y', labelsize=lb) 
    fx3.tick_params(axis='x', labelsize=lb) 
    #fx3.set_ylabel('ε predicted', fontsize = 20) 
    #fx3.set_xlabel('ε observed (field)', fontsize = 20) 
    fx3.grid(True) 
    fx3.set_ylim(0, 51)   
    fx3.set_xlim(0, 51)  
    fx3.legend(loc='upper left', fontsize = 15)
    
    fx4.tick_params(axis='y', labelsize=lb) 
    fx4.tick_params(axis='x', labelsize=lb) 
    #fx4.set_ylabel('ε predicted', fontsize = 20) 
    #fx4.set_xlabel('ε observed (field)', fontsize = 20) 
    fx4.grid(True) 
    fx4.set_ylim(0, 51)  
    fx4.set_xlim(0, 51)  
    #fx4.legend(loc='upper left', fontsize = 12)

    fx5.grid(True) 
    #fx5.set_ylabel('ε predicted', fontsize = 20) 
    fx5.set_xlabel('${ε_b}$ observed in field', fontsize = 22) 
    #fx5.legend(loc='upper left', fontsize = 10) 
    fx5.tick_params(axis='y', labelsize=lb) 
    fx5.tick_params(axis='x', labelsize=lb) 
    fx5.set_ylim(0, 51)  
    fx5.set_xlim(0, 51)  
    
    fx6.grid(True) 
    #fx6.set_ylabel('ε predicted', fontsize = 20) 
    fx6.set_xlabel('${ε_b}$ observed in field', fontsize = 22) 
    #fx6.legend(loc='upper left', fontsize = 10) 
    #fx6.set_title(" Roth2" , fontweight='bold', fontsize=25) 
    fx6.tick_params(axis='y', labelsize=lb) 
    fx6.tick_params(axis='x', labelsize=lb) 
    fx6.set_ylim(0, 51)  
    fx6.set_xlim(0, 51) 

    
def fig14(x1, x2):

    x1.legend(loc='upper right', fontsize = 16) 
    x1.tick_params(axis='y', labelsize=20) 
    x1.tick_params(axis='x', labelsize=20) 
    #x1.set_xlabel('${α}$ [-]', fontsize = 22) 
    x1.set_ylabel('${m}$ [-]', fontsize = 22) 
    x1.grid(True) 
    #x1.set_ylim(3.3, 4) 
    #x1.set_xlim(3.25, 4.2)

    x2.legend(loc='upper right', fontsize = 16)
    x2.tick_params(axis='y', labelsize=20) 
    x2.tick_params(axis='x', labelsize=20) 
    x2.set_xlabel('${α}$ [-]', fontsize = 22) 
    x2.set_ylabel('${L}$ [-]', fontsize = 22) 
    #x2.set_yticks(np.arange(0, -120, -3))
    x2.grid(True) 
    #x2.set_ylim(3.2, 4.5)  
    #x2.set_xlim(3.2, 4.5)


def fig15(r1, r2, r3, r4, r5, r6, yp):
    r1.tick_params(axis='y', labelsize=14) 
    r1.tick_params(axis='x', labelsize=14) 
    r1.set_xlabel('${ϴ}$ [%]', fontsize = 18) 
    r1.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r1.grid(True) 
    r1.set_ylim(0, 60)  
    #r1.set_xlim(1, 50) 
    #r1.legend(loc='upper left', fontsize = 10)
                   
    r2.tick_params(axis='y', labelsize=14) 
    r2.tick_params(axis='x', labelsize=14) 
    r2.set_xlabel("${B_d}$ [g/cm3]", fontsize = 18) 
    r2.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r2.grid(True) 
    r2.set_ylim(0, 60)  
    #r2.set_xlim(1, 50) 
    #r2.legend(loc='upper left', fontsize = 10)
    
    r3.tick_params(axis='y', labelsize=14) 
    r3.tick_params(axis='x', labelsize=14) 
    r3.set_xlabel('${P_d}$ [g/cm3]', fontsize = 18) 
    r3.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r3.grid(True) 
    r3.set_ylim(0, 60)  
    #r1.set_xlim(1, 50) 
    #r3.legend(loc='upper left', fontsize = 10)
                   
    r4.tick_params(axis='y', labelsize=14) 
    r4.tick_params(axis='x', labelsize=14) 
    r4.set_xlabel('${ε_s}$ [-]', fontsize = 18) 
    r4.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r4.grid(True) 
    r4.set_ylim(0, 60)  
    #r1.set_xlim(1, 50) 
    #r4.legend(loc='upper left', fontsize = 10)
    
    r5.tick_params(axis='y', labelsize=14) 
    r5.tick_params(axis='x', labelsize=14) 
    r5.set_xlabel('${ε_w}$ [-]', fontsize = 18) 
    r5.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r5.grid(True) 
    r5.set_ylim(0, 60)  
    #r5.set_xlim(1, 50) 
    #r5.legend(loc='upper left', fontsize = 10)
   
    r6.tick_params(axis='y', labelsize=14) 
    r6.tick_params(axis='x', labelsize=14) 
    r6.set_xlabel('${CEC}$ [meq/100g]', fontsize = 18) 
    r6.set_ylabel("${ε_b}$ [-]", fontsize = 18) 
    r6.grid(True) 
    r6.set_ylim(0, 60)  
    #r6.set_xlim(1, 50) 
    #r6.legend(loc='upper left', fontsize = 10)