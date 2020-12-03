import matplotlib.pylab as plt
import numpy as np

fig, axes = plt.subplots(1, figsize=(20, 10))
import pandas as pd

fig, axes = plt.subplots(figsize=(13, 13))


def add_values(bp, ax):
    """ This actually adds the numbers to the various points of the boxplots"""
    for element in ['whiskers', 'medians', 'caps']:
        for line in bp[element]:
            # Get the position of the element. y is the label you want
            (x_l, y), (x_r, _) = line.get_xydata()
            # Make sure datapoints exist
            # (I've been working with intervals, should not be problem for this case)
            if not np.isnan(y):
                x_line_center = x_l + (x_r - x_l) / 2
                y_line_center = y  # Since it's a line and it's horisontal
                # overlay the value:  on the line, from center to right
                ax.text(x_line_center, y_line_center,  # Position
                        '%.3f' % y,  # Value (3f = 3 decimal float)
                        verticalalignment='center',  # Centered vertically with line
                        fontsize=16, backgroundcolor="white")


direct_face = [0.5311297668334876, 0.4553624717798787, 0.7858408045907288, 0.47613975899004135, 0.7062234332425068, 0.0,
               0.3930146402428138, 0.5355569832601634, 0.30651158445440957, 0.44127108762019723, 0.8146274278325885,
               0.45193320866123043, 0.43353979876335624, 0.2953050190851304, 0.19763511641566098, 0.5085100794536739,
               0.6556438168088653, 0.016674568837788183, 0.05594927436707412, 0.5436828238049434, 0.4177006245013618,
               0.1882975350717286, 0.07911358182737527, 0.1647508485695542, 0.6848456990152945, 0.45464635665988]
weighted_face = [0.5311297668334876, 0.4553624717798787, 0.539830799234353, 0.47613975899004135, 0.5020660211938706,
                 0.17150513094938302, 0.3930146402428138, 0.5355569832601634, 0.30651158445440957, 0.4786408489484886,
                 0.23371065518054573, 0.45193320866123043, 0.43353979876335624, 0.2953050190851304, 0.19763511641566098,
                 0.5085100794536739, 0.33549267840354424, 0.12660747914985204, 0.05594927436707412, 0.5436828238049434,
                 0.4177006245013618, 0.1882975350717286, 0.07911358182737527, 0.1647508485695542, 0.16843003251812422,
                 0.45464635665988]
ppd = [0.5311297668334876, 0.4553624717798787, 0.539830799234353, 0.47613975899004135, 0.5020660211938706,
       0.17150513094938302, 0.3930146402428138, 0.5355569832601634, 0.30651158445440957, 0.4786408489484886,
       0.23371065518054573, 0.45193320866123043, 0.43353979876335624, 0.2953050190851304, 0.19763511641566098,
       0.5085100794536739, 0.33549267840354424, 0.12660747914985204, 0.05594927436707412, 0.5436828238049434,
       0.4177006245013618, 0.1882975350717286, 0.07911358182737527, 0.1647508485695542, 0.16843003251812422,
       0.45464635665988]
vote = [0.5018534000031547, 0.4832872788697225, 0.6056104774831351, 0.4818285763135679, 0.0, 0.15836297532107782,
        0.38411744357000777, 0.4889810308160032, 0.32477727182736094, 0.5365773754619881, 0.2491620348763206,
        0.5938070136674979, 0.2663725747173873, 0.3502683897493565, 0.0, 0.5246412666996536, 0.31008651478229476,
        0.2532914894802325, 0.0, 0.6685425038753425, 0.4326997064607142, 0.2872003759100533, 0.011269971825070437,
        0.1723103300471496, 0.15947262587032446, 0.48510211643671397]
direct_face_high_thresh = [0.5311297668334876, 0.4553624717798787, 0.7858408045907288, 0.47613975899004135,
                           0.7062234332425068, 0.17150513094938302, 0.3930146402428138, 0.5355569832601634,
                           0.30651158445440957, 0.44127108762019723, 0.23371065518054573, 0.6445464982778416,
                           0.43353979876335624, 0.2953050190851304, 0.19763511641566098, 0.5085100794536739,
                           0.6556438168088653, 0.12660747914985204, 0.05594927436707412, 0.5436828238049434,
                           0.4177006245013618, 0.1882975350717286, 0.07911358182737527, 0.1647508485695542,
                           0.6848456990152945, 0.45464635665988]
new_weighted_face = [0.6623991764872265, 0.4694009069463577, 0.6430084745762712, 0.7577799483191355,
                     0.08048239721733282, 0.20589508310249308, 0.26897388325959753, 0.47730305955428715,
                     0.17837339257579074, 0.6578789952480535, 0.17496599263301083, 0.4556113482299774,
                     0.49498739655390706, 0.4762068439561667, 0.19698745998518422, 0.5612173913043478,
                     0.43581505030012757, 0.7492183115529544, 0.2647568970971648, 0.655353255491787, 0.5273889332731252,
                     0.27765959033138327, 0.45904608117591134, 0.1737556297561733, 0.2512091555212425,
                     0.32811392943176987]
new_direct_face = [0.6623991764872265, 0.5212350396207959, 0.7858408045907288, 0.7577799483191355, 0.7062234332425068,
                   0.20589508310249308, 0.26897388325959753, 0.47730305955428715, 0.1726291126509952,
                   0.44127108762019723, 0.17496599263301083, 0.6445464982778416, 0.34892554183308205,
                   0.4762068439561667, 0.19698745998518422, 0.5612173913043478, 0.6556438168088653, 0.6258451885108455,
                   0.2948087582886704, 0.655353255491787, 0.5273889332731252, 0.27765959033138327, 0.45904608117591134,
                   0.1737556297561733, 0.6848456990152945, 0.32811392943176987]
new_ppd = [0.6623991764872265, 0.5212350396207959, 0.5518054098908571, 0.7577799483191355, 0.08048239721733282,
           0.20589508310249308, 0.26897388325959753, 0.47730305955428715, 0.1726291126509952, 0.6578789952480535,
           0.17496599263301083, 0.38317880794701986, 0.34892554183308205, 0.4762068439561667, 0.19698745998518422,
           0.5612173913043478, 0.43581505030012757, 0.6258451885108455, 0.2948087582886704, 0.655353255491787,
           0.5273889332731252, 0.27765959033138327, 0.45904608117591134, 0.1737556297561733, 0.11531200490783577,
           0.32811392943176987]

df = pd.DataFrame({'Strategy 1': vote,
                   'Strategy 2': new_ppd,
                   'Strategy 3': new_direct_face,
                   # 'Strategy 3 Worst Case': direct_face,
                   'Strategy 4': new_weighted_face})

bp_dict = df.boxplot(grid=True, figsize=(25, 10), ax=axes, return_type='dict')
add_values(bp_dict, axes)
plt.ylabel('IoU', fontsize=15)
plt.yticks(fontsize=15)
plt.xticks(rotation=45, fontsize=15)
plt.xlabel('Strategies', fontsize=15)
plt.show()
