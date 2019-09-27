import socket

from aegisblade import aegisblade
from aegisblade import JobConfig, Capability


def helloworld():
    """
    In this example we will deploy & run this function
        inside of AegisBlade.
    """
    hostname = socket.gethostname()

    print("The server's hostname is {0}".format(hostname))

    return "Hello World from {0}".format(hostname)


def main():
    """
    The main() function will run on your local machine
    and start two jobs on AegisBlade with the above functions.
    """

    # Calling aegisblade.run() will start the job on a server managed by AegisBlade.
    # AegisBlade will handle provisioning hosts, deploying your code, and running it.
    job = aegisblade.run(lambda: helloworld())

    # Return values are serialized and can be fetched when the job is finished.
    #
    # Calling .get_return_value() will wait for the job to finish, 
    #   then get the return value.
    job_return_value = job.get_return_value()

    print("RETURN VALUE")
    print(job_return_value)

    assert "Hello World" in job_return_value

    # Logs are stored and can also be fetched after the job is finished.
    job_logs = job.get_logs()

    print("LOGS:")
    print(job_logs)

    assert "hostname" in job_logs


# Using the __name__ == "__main__" idiom to only run main when this script
#   is called directly is especially important when using AegisBlade.
#
# This script may be imported by the AegisBlade runtime, and without the 
#   protective check of __name__, main() would be called inside the job 
#   potentially causing an infinite loop of jobs starting more jobs.
if __name__ == "__main__":
    main()
