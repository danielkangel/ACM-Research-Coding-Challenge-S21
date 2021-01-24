from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram

record = SeqIO.read("Genome.gb", "genbank")

# initializes the diagram
gd_diagram = GenomeDiagram.Diagram("Tomato curly stunt virus, complete genome.")

# initializes the first and second track, which are used to display the genome spread out/colored
first_track = gd_diagram.new_track(3, name="Initial Track", height=0.75)
second_track = gd_diagram.new_track(4, name="Overlay Track", height=0.75)
first_feature_set = first_track.new_set()
second_feature_set = second_track.new_set()

# initializes the outer track which is used for labeling the length of the genome
label_track = gd_diagram.new_track(5, name="Label Track", scale_smalltick_interval=50, scale_largetick_interval=200,
                                   start=0, end=len(record), scale_fontsize=10, axis_labels=True)
label_feature_set = label_track.new_set()

# initializes a blank spacer track
blank_track = gd_diagram.new_track(2, name="Blank Spacer Track", hide=True)
blank_feature_set = blank_track.new_set()

# initializes the center track, which shows the two basic directions of the genome
final_track = gd_diagram.new_track(1, name="Inside Overlay")
final_feature_set = final_track.new_set()

# initializes the counter variable used for accessing the color list and checking each track
color_check = 0

col = ["red", "green", "purple", "orange", "blue"]

# adds features to both the spread out tracks and center tracks based off of the counter variable
for feature in record.features:
    if feature.type == "gene":
        # places each bar into one of the two tracks
        color = col[color_check % 5]
        if color_check % 2 == 0:
            first_feature_set.add_feature(feature, color=color, label=True, sigil="ARROW", label_size=14,
                                          label_angle=-90, arrowshaft_height=1)
        else:
            second_feature_set.add_feature(feature, color=color, label=True, sigil="ARROW", label_size=14,
                                           arrowshaft_height=1, label_angle=-90)
        if color_check < 2:
            final_feature_set.add_feature(feature, color="darkslategrey")
        else:
            final_feature_set.add_feature(feature, color="lightslategrey")
        color_check += 1

# check the levels to make sure data was placed in the correct track
# print(gd_diagram.get_levels())

# drawing and writing the diagram
gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(30 * cm, 30 * cm),
    start=0,
    end=len(record),
    circle_core=0.3,
)
gd_diagram.write("tomato_curly_stunt_virus.png", "PNG")
