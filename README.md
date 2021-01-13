# ACM Research Coding Challenge (Spring 2021)

## Initial Reaction

Prior to this challenge, I had never worked with a genbank file before. I became familiar with the format through an [annotated file](https://www.ncbi.nlm.nih.gov/genbank/samplerecord/#CDSB) first.

Aditionally, I looked at standard circular genome diagrams to get an idea for what I will be creating.

## GenomeDiagram from Biopython

I chose the GenomeDiagram subpackage from Biopython to create my diagram due to my prior experience with Python and the thorough [documentation](https://biopython.org/docs/dev/api/Bio.Graphics.GenomeDiagram.html#module-Bio.Graphics.GenomeDiagram). Also, Biopython has a friendly [tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec336) for the subpackage.

After I implemented a basic circular diagram, I noticed that the levels were wrong. Data was overlapping in the diagram, thus making it hard to view the start and endpoints. I created a new track/level in the diagram and added colors to further differentiate the data. 

## Diagram

![Tomato curly stunt virus circular diagram](tomato_curly_stunt_virus.png)

