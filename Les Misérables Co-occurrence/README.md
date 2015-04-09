*************************************************************************************************
This matrix diagram visualizes similarities between the research papers.

Each colored cell represents two research papers that are similar to each other based on the keywords associated with them; darker cells indicates papers that have many keywords in common.

Use the drop-down menu to reorder the matrix and explore the data. 
*************************************************************************************************
Files:
1) formatAdjacencyMatrix.py : Used to create the JSON file from input data.
2) index.html               : D3 visualization
3) input.json               : Created by formatAdjacencyMatrix.py script and used by index.html for visualization
4) testData.txt             : Sample test data (we only used the first 150 lines to generate visualizations in the images)
*************************************************************************************************
The input test data is in the below format:
AUvxBUt1anePV-W5QJ0Q,PS
AUvxBUt1anePV-W5QJ0Q,Nafion
AUvxBUt1anePV-W5QJ0Q,DNA
AUvxCKxGSueeRLZ6tbI5,PMMA
AUvxCKxGSueeRLZ6tbI5,Nafion

where AUvxBUt1anePV-W5QJ0Q and AUvxCKxGSueeRLZ6tbI5 are the research paper IDs and PS, Nafion, DNA, PMMA are the keywords associated with them respectively. 
*************************************************************************************************
Usage          : python3 formatAdjacencyMatrix.py testData.txt input.json cluster-factor 
                 This command will generate the input JSON file for the D3 visualization.

cluster-factor : A numerical value which decides how many nodes are placed in one group

Example        : python3 formatAdjacencyMatrix.py testData.txt input.json 5

This example creates the JSON file with 5 nodes in each group
*************************************************************************************************
JSON Format:
{"nodes": [{"name": "AUvxBUt1anePV-W5QJ0Q", "group": 1}, {"name": "AUvxCKxGSueeRLZ6tbI5", "group": 1}], "links": [{"value": 1, "source": 1, "target": 0}, {"value": 1, "source": 0, "target": 1}]}

Nodes: Nodes represents the data points forming rows and columns of the visualization matrix (here document name).
Group: Used to logically group the documents into groups. This visualization uses 1 colour per group for visualization.
Links: Represents the links or or cells to be coloured in the matrix.
Source: Row number in the matrix (The python script used to generate JSON will sort the input data points and assign each of them a unique 
        ID)
Target: Column number in the matrix (The python script used to generate JSON will sort the input data points and assign each of them a
        unique ID)
Value: Defines the nsity of colour in the source-target cell of matrix. Here its the number of keyword match between source and target
       document.
*************************************************************************************************       
