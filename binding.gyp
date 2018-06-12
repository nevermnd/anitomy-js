{
    "targets": [
        {
            "target_name": "anitomy-js",
            "sources": [
                "lib/anitomy/anitomy/anitomy.cpp",
                "lib/anitomy/anitomy/anitomy.h",
                "lib/anitomy/anitomy/element.cpp",
                "lib/anitomy/anitomy/element.h",
                "lib/anitomy/anitomy/keyword.cpp",
                "lib/anitomy/anitomy/keyword.h",
                "lib/anitomy/anitomy/options.h",
                "lib/anitomy/anitomy/parser.cpp",
                "lib/anitomy/anitomy/parser.h",
                "lib/anitomy/anitomy/parser_helper.cpp",
                "lib/anitomy/anitomy/parser_number.cpp",
                "lib/anitomy/anitomy/string.cpp",
                "lib/anitomy/anitomy/string.h",
                "lib/anitomy/anitomy/token.cpp",
                "lib/anitomy/anitomy/token.h",
                "lib/anitomy/anitomy/tokenizer.cpp",
                "lib/anitomy/anitomy/tokenizer.h",
                "src/anitomy_js.h",
                "src/anitomy_js.cpp",
                "src/worker.h",
                "src/worker.cpp",
                "src/addon.cpp"
            ],
            "xcode_settings": {
                "OTHER_CFLAGS": [
                    "-mmacosx-version-min=10.7",
                    "-stdlib=libc++",
                    "-std=c++14"
                ]
            },
            "cflags": [
                "-std=c++14"
            ],
            "cflags_cc!": [
                "-fno-rtti",
                "-fno-exceptions"
            ],
            "include_dirs": [
                "<!(node -e \"require('nan')\")",
                "lib/anitomy"
            ]
        }
    ]
}
