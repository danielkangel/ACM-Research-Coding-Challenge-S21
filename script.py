from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio import SeqIO
from Bio.Graphics import GenomeDiagram

record = SeqIO.read("Genome.gb", "genbank")

# creates the diagram object, two track objects, and two feature objects.
gd_diagram = GenomeDiagram.Diagram("Tomato curly stunt virus, complete genome.")
gd_track_for_features = gd_diagram.new_track(1, name="Annotated Features")
gd_track_for_features_2 = gd_diagram.new_track(2, name= "Annotated Features")
gd_feature_set = gd_track_for_features.new_set()
gd_feature_set_2 = gd_track_for_features_2.new_set()

# initializes the counter variable used for accessing the color list and checking each track
color_check = 0

col = ["red", "green", "purple", "orange", "blue"]

for feature in record.features:
    if feature.type == "gene":
        #places each bar into one of the two tracks
        if color_check % 2 == 0:
            color = col[color_check % 5]
            gd_feature_set.add_feature(feature, color=color, label=True, sigil="ARROW", label_size=18, label_angle=-90, arrowshaft_height=1)
        else:
            color = col[color_check % 5]
            gd_feature_set_2.add_feature(feature, color=color, label=True, sigil="ARROW", label_size=18, arrowshaft_height=1, label_angle=-90)
        color_check +=1

# check the levels to make sure data was placed in the correct track
print(gd_diagram.get_levels())


# drawing and writing the diagram
gd_diagram.draw(
    format="circular",
    circular=True,
    pagesize=(30 * cm, 30 * cm),
    start=0,
    end=len(record),
    circle_core=0.65,
)
gd_diagram.write("tomato_curly_stunt_virus.png", "PNG")
