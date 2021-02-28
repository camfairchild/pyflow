# Installation
Run `pip install -r requirements.txt`

# Usage
Run `python run.py`

This opens a file called ./this.txt in the current directory. 
If it exists, it shows the contents

The pyflow syntax uses the keyword `to` to indicate an arrow from one element to the next

Connecting elements is as simple as `elem1 to elem2`
Which generates the following plant-this.png

![example png](https://github.com/camfairchild/pyflow/blob/main/example.png?raw=true)

Pyflow uses newlines to make new connections and you can only make one connection per line.

When you click to generate a flowchart, 
the file is saved and a flowchart is generated as `./plant-this.png`

