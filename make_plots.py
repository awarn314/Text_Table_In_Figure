import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('Data.csv')

personality_grps=['Executing','Influencing','Relationship Building','Strategix Thinking']
executing_grp=['Achiever','Arranger','Belief','Consistency','Deliberative','Discipline','Focus','Responsibility','Restorative']
influencing_grp=['Activator', 'Command','Communication','Competition','Maximizer','Self-Assurance', 'Significance','Woo']
Rel_Building_grp=['Adaptability','Connectedness','Developer','Empathy','Harmony','Includer','Individualization','Positivity','Relator']
strat_thinking_grp=['Analytical','Context','Futuristic','Ideation','Input','Intellection','Learner','Strategic']
total_list=executing_grp+influencing_grp+Rel_Building_grp+strat_thinking_grp
ll_bin=np.zeros(len(total_list))

People = df['First Name'].tolist()
People_Last = df['Last Name'].tolist()
Themes = ["Theme 1", "Theme 2", "Theme 3", "Theme 4", "Theme 5"]

m1=0
for th in Themes:
    m2=max(df['Theme 1'].str.len())
    if m2>m1:
        m1=m2

data=[]
for i,j in zip(People,People_Last):
    info=df.loc[(df['First Name'] == i) & (df['Last Name'] == j)]
    temp_list=info[Themes].values.tolist()
    pers_res=temp_list[0]
    pers_res2=[]
    for pers in pers_res:
        len_pers=len(pers)
        offset=m1-len_pers
        pers += ' ' * offset
        pers_res2.append(pers)
    data.append(pers_res2)
    
n = len(Themes)*len(People)
ncols = len(Themes)
nrows = len(People)

fig, ax = plt.subplots(figsize=(10, 7))

# Get height and width
X, Y = fig.get_dpi() * fig.get_size_inches()
h = Y / (nrows + 1)
w = X / ncols

for i in range(len(People)):
    for j in range(len(Themes)):
        row = len(People)-i-1
        col = j
        y = Y - (row * h) - h
        xi_text = w * (col+.1)
        plabel=data[i][j]
        if plabel.rstrip() in strat_thinking_grp:
            cc='red'
            dd='black'
        elif plabel.rstrip() in influencing_grp:
            cc='yellow'
            dd='black'
        elif plabel.rstrip() in Rel_Building_grp:
            cc='blue'
            dd='white'
        else:
            cc='purple'
            dd='white'
        ll_bin[total_list.index(plabel.rstrip())]=ll_bin[total_list.index(plabel.rstrip())]+1
        ax.text(xi_text, y, plabel, fontsize=(h * 0.25), color=dd,
                horizontalalignment='left',
                verticalalignment='center', 
                bbox=dict(facecolor=cc))
ax.set_xlim(0, X)
ax.set_ylim(0, Y)
ax.set_xticks(np.linspace(0.15*w,w * (len(Themes) + 0.3-1),len(Themes)))
ax.set_yticks(np.linspace(Y - ((len(People)-1) * h) - h,Y-h,len(People)))
ax.set_yticklabels(People, fontsize=(h * 0.25))
ax.set_xticklabels(Themes, fontsize=(h * 0.25))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
plt.tight_layout()
fig.subplots_adjust(left=.2, right=.9,
                    top=.9, bottom=.1,
                    hspace=0.2, wspace=0.2)
plt.show()
plt.savefig('Result.png')


