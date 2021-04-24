from SIRmodel import SIR
import matplotlib.pyplot as plt

# STD: April 22, 2021
N = 674635
I = 687
R = 660 + 25018 + 1  # recovered + vaccination + dead
S = N - I

def simulateWithNoQuarantine():
    model = SIR(S, I, R, 1, 1./30)
    ds = [[], [], [], []]  # [date, S, I, R]

    for i in range(360):
        model.update()
        ds[0].append(i)
        ds[1].append(model.S)
        ds[2].append(model.I)
        ds[3].append(model.R)

    plt.title("Simulation with no quarantine")
    plt.ylabel("Number of People")
    plt.xlabel("Date")
    plt.plot(ds[0], ds[1], label="Susceptible")
    plt.plot(ds[0], ds[2], label="Infectible")
    plt.plot(ds[0], ds[3], label="Recovery/Removed")
    
    plt.legend()
    plt.show()

def simulateWithLooseQuarantine():
    model = SIR(S, I, R, 0.5, 1./30)
    ds = [[], [], [], []]  # [date, S, I, R]

    for i in range(360):
        model.update()
        ds[0].append(i)
        ds[1].append(model.S)
        ds[2].append(model.I)
        ds[3].append(model.R)

    plt.title("Simulation with loose quarantine")
    plt.ylabel("Number of People")
    plt.xlabel("Date")
    plt.plot(ds[0], ds[1], label="Susceptible")
    plt.plot(ds[0], ds[2], label="Infectible")
    plt.plot(ds[0], ds[3], label="Recovery/Removed")
    
    plt.legend()
    plt.show()

def simulateWithNormalQuarantine():
    model = SIR(S, I, R, 0.2, 1./20)
    ds = [[], [], [], []]  # [date, S, I, R]

    for i in range(360):
        model.update()
        ds[0].append(i)
        ds[1].append(model.S)
        ds[2].append(model.I)
        ds[3].append(model.R)
        
    plt.title("Simulation with normal quarantine")
    plt.ylabel("Number of People")
    plt.xlabel("Date")
    plt.plot(ds[0], ds[1], label="Susceptible")
    plt.plot(ds[0], ds[2], label="Infectible")
    plt.plot(ds[0], ds[3], label="Recovery/Removed")
    
    plt.legend()
    plt.show()
    
def simulateWithKoreanQuarantine():
    model = SIR(S, I, R, 0.1, 1./30)
    ds = [[], [], [], []]  # [date, S, I, R]

    for i in range(360):
        model.update()
        ds[0].append(i)
        ds[1].append(model.S)
        ds[2].append(model.I)
        ds[3].append(model.R)

    plt.title("Simulation with hard quarantine")
    plt.ylabel("Number of People")
    plt.xlabel("Date")
    plt.plot(ds[0], ds[1], label="Susceptible")
    plt.plot(ds[0], ds[2], label="Infectible")
    plt.plot(ds[0], ds[3], label="Recovery/Removed")
    
    plt.legend()
    plt.show()

def simulateWithLockdown():
    model = SIR(S, I, R, 0.05, 1./30)  # assume everyone stay at home.
    ds = [[], [], [], []]  # [date, S, I, R]

    for i in range(360):
        model.update()
        ds[0].append(i)
        ds[1].append(model.S)
        ds[2].append(model.I)
        ds[3].append(model.R)
        
    plt.title("Simulation with lockdown")
    plt.ylabel("Number of People")
    plt.xlabel("Date")
    plt.plot(ds[0], ds[1], label="Susceptible")
    plt.plot(ds[0], ds[2], label="Infectible")
    plt.plot(ds[0], ds[3], label="Recovery/Removed")
    
    plt.legend()
    plt.show()
