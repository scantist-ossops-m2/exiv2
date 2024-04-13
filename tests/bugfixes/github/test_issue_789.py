import system_tests


class SIGSEGV_in_PngImage_readMetadata(
        metaclass=system_tests.CaseMeta):

    url = "https://github.com/Exiv2/exiv2/issues/756"

    filename = system_tests.path(
        "$data_path/issue_789_poc1.png"
    )
    commands = ["$exiv2 $filename"]
    stdout = [""]
    stderr = [""]
    retval = [1]

    compare_stderr = system_tests.check_no_ASAN_UBSAN_errors
