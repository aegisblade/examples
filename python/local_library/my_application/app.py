import os

from aegisblade import aegisblade, JobConfig

from my_local_package.main import local_library_function

def do_work():
    """This function will run on a server and call into the local_library_function
    from the local package my_local_package."""
    return local_library_function("work")

def app_main():
    """
    The app_main() function will run on your local machine
    and use AegisBlade to run the do_work() function on a server.
    """
    # Construct the path to the library on our local disk
    local_library_path = os.path.join(
        os.path.abspath(
            os.path.dirname(os.path.realpath(__file__))),
        "../my_local_library/")

    # Create a job configuration that references the local library
    #   and references the appropriate package.
    job_config = JobConfig() \
        .add_library("my_local_package", local_library_path)

    # Build the application and run a job
    job = aegisblade.run(lambda: do_work(), job_config)

    # Ensure we get the results we expect
    assert "local_library_work" in job.get_return_value()

if __name__ == "__main__":
    app_main()

