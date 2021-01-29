# node-gyp-help-sample

Hi community, I need help finding out what's going on here.

I'm looking for a way to override a variable defined by my `binding.gyp` file. The trick with
`export GYP_DEFINES="so_dir=good_directory_here"` does not seem to work when the variable is defined in that file.

```
# overriding the value of the "so_dir" variable
export GYP_DEFINES="so_dir=good_directory_here"
npm install
...
g++: error: /home/tveronezi/Documents/sources/trend_vpn/node-gyp-help-sample/wrong_dir/external.so: No such file or directory
...
```

Note that the variable `so_dir` still points to the value defined in the `binding.gyp` file.

If I remove the variable definition out of the `binding.gyp` file and try it again, the `so_dir` will have the value
from the `GYP_DEFINES` environment variable.

`binding.gyp` without `variables`:

```
{
  "targets": [
    {
      "target_name": "mycode",
      "sources": [
        "src/mycode.cc",
      ],
      "libraries": [
        "<(so_dir)/external.so",
      ]
    }
  ]
}
```

```
export GYP_DEFINES="so_dir=good_directory_here"
npm install
...
g++: error: good_directory_here/external.so: No such file or directory
...
```

Can you help?
