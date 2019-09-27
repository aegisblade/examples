const path = require('path');

const {localLibraryFunc} = require("my_local_library");
const {aegisblade} = require('aegisblade');

/**
 * In this example the `runWithLocalLibrary()` function will be run on a
 * server using AegisBlade. 
 */
async function runWithLocalLibrary() {
    return localLibraryFunc();
}

// Any target function to be run on AegisBlade must be exported.
module.exports = {runWithLocalLibrary};

/**
 * The `main()` function will run on your local machine
 * and start the job running the `runWithLocalLibrary()` function
 * on a server using AegisBlade.
 */
async function main() {
    // Defining the jobConfig libraries value is required for the 
    //   library to be uploaded as a part of the application. Try
    //   removing the `libraries` value and observe the error.
    let jobConfig = {
        libraries: [path.join(__dirname, "../my_local_library")]
    };

    let job = await aegisblade.run(runWithLocalLibrary, [], jobConfig);
    
    console.log(`Job Id: ${job.id}`);
    console.log("Waiting for the job to finish running...");

    let jobReturnValue = await job.getReturnValue();
    console.log(`Job Return Value: ${jobReturnValue}`);
    console.log(`Job Logs: ${await job.getLogs()}`);
}

//  Using the `require.main === module` idiom to only run main when this script
//    is called directly is especially important when using AegisBlade to prevent
//    infinite loops of jobs creating jobs.
if (require.main === module) {
    (async () => {
        try {
            await main();
        } catch (err) {
            console.error(err);
        }
    })();
}


