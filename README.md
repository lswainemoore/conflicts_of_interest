# Text Mining to Find Interactions between Political Contributions and Political Speech
## Senior Project by Lincoln Swaine-Moore

### Abstract

This project aims to demonstrate an approach for identifying conflicts of interest in political speech—that is, instances where politicians voice opinions (e.g. via Twitter, speech on the congressional floor, or simply voting on a bill) that are related to industries from which they have received donations. This involves training models to recognize text as related to a particular industry, then running those models on political speech, and highlighting instances where politicians speak about the top industries to have funded them. The primary goal of this project in this semester is to investigate whether it is possible to train these models to be effective, and to document the methodology of this investigation.
A large portion of the time spent on this project was dedicated to the data collection process. Several types of data were necessary: donations data, political speech on which to test the models, and—crucially—labeled training data. The last source proved the most difficult to gather.
Preliminary results from the model-training process suggest that it is possible to train models to categorize the training data fairly accurately. The trained models demonstrate some basic success identifying political speech (in the form of tweets) that is related to industries, though they are far from perfect. Filtering results using the collected donations data then permits identification of instances where politicians discuss subjects related to top donor industries. 
These results suggest that with further refinement, it should be possible to reliably recognize political speech as related to particular industries, and, using these classifications alongside donation data, to identify potential conflicts of interest.

### This repository 
...contains the code demonstrating the way in which I gathered my data (data itself not included in this repo), and the basic modeling work I've done so far.

See lincoln_swaine-moore_cpsc490_presentation.pdf and lincoln_swaine-moore_cpsc490_report.pdf for more details.
