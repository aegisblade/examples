
/**
 * `localLibraryFunc()` is exported from this package, to be used
 * in my_application. Using local libraries requires a special job
 * configuration, shown in this example.
 */
function localLibraryFunc() {
    return "my_local_library_func_return_value";
}

module.exports = {localLibraryFunc};