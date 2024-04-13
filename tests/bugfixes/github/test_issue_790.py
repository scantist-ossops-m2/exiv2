import system_tests

# Due to an integer overflow bug (#790), this test triggers an 8GB
# memory allocation.  So the test will fail with a std::bad_alloc
# exception if less than 8GB is available.  On Linux, you can use
# `ulimit -v 8000000` to reduce the available memory to slightly less
# than 8GB.

class integer_overflow_in_PngImage_readMetadata(
        metaclass=system_tests.CaseMeta):

    url = "https://github.com/Exiv2/exiv2/issues/790"

    filename = system_tests.path(
        "$data_path/issue_790_poc2.png"
    )
    commands = ["$exiv2 $filename"]
    stdout = [""]
    stderr = [  """Exiv2 exception in print action for file $filename:
Failed to read image data
"""
]
    retval = [1]
