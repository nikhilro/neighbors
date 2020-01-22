# neighbors
Given the coordinates for a place, find other places from a list within X km distance of that

# Run

**Please use python3 to run the program.** 
**Run all commands at the top level directory.**

`python3 -m neighbors --help` # to get different options for running

`python3 -m neighbors -i customer.txt -c 37.788802 -122.4025067` # example

`python3 -m unittest discover -v` # run tests

## Thoughts as I was coding

##### *Things I didn't do because a) limited time b) don't wanna over-engineer*

* We could have a InputArg struct. Then have CLIGenerator and CLIValidator classes that would be generated from the same array of InputArg struct which would contain all information needed to construct them.

* We could have Abstract classes that define hooks for child classes to override. Would be possible to achieve [non-virtual interface (NVI) pattern](https://en.wikipedia.org/wiki/Non-virtual_interface_pattern) then. Of course, it's python so one can do whatever they want. Eg. YAMLReader would inherit from AbstractReader and then we can support multiple readers in future.

* Most of the classes are constructed for somewhat "one of" use of their instances; this is nice because instance state remains fresh - easier to make assumptions/guarantees in future. Eg. an instance of OrthodermicAnalyzer is only useful for one reference point; for a different point, we'll need a new instance. There is an argument to be made for making functions "one of" use. So, orthodermicAnalyzerInstance.find_admissible_items(reference) can be used for different references. Same for jsonWriterInstance.write_items(items) for different items. Not too sure, open to arguments to superiority of one way over another. 

* Easy to add more customizability by specifying additional option in CLI that override constants etc.

* Formatter/Transformer could be another step. Right now, JSONWriter just takes "keys" that we want to dump

* Testing rig is set up but not much testing :( ...