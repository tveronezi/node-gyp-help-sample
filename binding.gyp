{
  "variables": {
    "so_dir": "<(module_root_dir)/wrong_dir"
  },
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