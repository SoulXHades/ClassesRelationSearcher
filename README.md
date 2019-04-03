# ClassesRelationSearcher
A Python script that search for class names in current class's code. 
If it exist, it means there is a relationship (dependency, association, etc) with that class.

It was built by me to ease the need to search for existence of other classes in a class file when I was doing class diagram.

Currently, it search using the keyword 'in'. Thus, if you have words that are substring of the classes you are looking for,
it might appear as false positive. No pure word for word comparison is used as there might be cases like Android Development's
Intent where the classes are declared as 'Intent intent = new Intent(<class name>.this, <class name1>.class);'.
So use of 'in' keyword allows verstility.

The point of this script is to ease the need to use CTRL+F to search for many classes such as 15 or even more classes. 
Hence, with this script, the number of classes you need to search for, will be lesser.
