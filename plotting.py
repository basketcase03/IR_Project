import matplotlib.pyplot as plt

def plot(cos_sim,doc1_name,doc2_name):
    rad=1
    diam=2*rad*(1-cos_sim)

    circle1=plt.Circle((0,0),rad,alpha=.5)
    circle2=plt.Circle((diam,0),rad,alpha=.5)

    plt.ylim([-1.1, 1.1])
    plt.xlim([-1.1, 1.1 + diam])

    fig=plt.gcf()
    fig.gca().add_artist(circle1)
    fig.gca().add_artist(circle2)
    plt.text(0-rad, 0,doc1_name, size=15, color='black')
    plt.text(diam+rad/2, 0,doc2_name, size=15, color='black')
    plt.show()

#plot(0.67,"doc1","doc2")
