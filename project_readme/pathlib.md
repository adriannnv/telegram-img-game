# pathlib - Notes

## What is it?
`pathlib` is a python library that handles file system paths. It is an alternative to os.path and turns paths into objects and not strings like it did in the old way of handling things.
Instead of joining paths using os.path.join you now use / and it will automatically join them just like directories... It also is cross platform so / gets translated to \ on Windows.
Path objects have their own methods and can use String methods too, if they can't a simple cast to str(pathInstanceName) will work wonders.